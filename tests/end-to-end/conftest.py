import asyncio
import logging
import re
import subprocess
import sys

from queue import Queue

import pytest

def drainQueue(q):
    """
    convert (finished) queue to list
    """

    res = []
    while q.qsize() > 0:
        res.append(q.get_nowait())
    return res

async def stream_handler(input_stream, output_stream, queue):
    """
    write lines from input_stream to an output stream,
    but also accumulate in a queue.
    """

    if output_stream == sys.stdout:
      marker = "out> "
    elif output_stream == sys.stderr:
      marker = "err> "
    else:
      marker = "> "

    while not input_stream.at_eof():
        output = await input_stream.readline()
        #output_stream.buffer.write(output)
        logging.debug(marker + str(output.strip(), encoding="utf8"))
        queue.put(output)
        output_stream.flush()

async def stream_command(command, outQ, errQ, cwd=None):
    """
    accumulate stdout and stderr in some queues, and get
    exit code from some command, and
    also stream stdout and stderr to their proper locations.
    """

    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd=cwd,
    )

    await asyncio.gather(
        stream_handler(process.stderr, sys.stderr, errQ),
        stream_handler(process.stdout, sys.stdout, outQ),
    )
    # process.communicate() will have no data to read but will close the
    # pipes that are implemented in C, whereas process.wait() will not
    await process.communicate()

    return process.returncode

class Helpers:

    @staticmethod
    def run(command, cwd=None, expected_exit_code=0):

        if type(command) == str:
          command = ["sh", "-c", command]

        some_info = dict(
          command=command,
          cwd=cwd,
          expect_code=expected_exit_code,
        )
        logging.info(f"Helpers.runX: info: {some_info}")

        outQ = Queue()
        errQ = Queue()

        exitCode = asyncio.run(stream_command(command, outQ, errQ, cwd=cwd))

        stdout = b"\n".join(drainQueue(outQ))
        stderr = b"\n".join(drainQueue(errQ))

        if type(stdout) is bytes:
            stdout = stdout.decode("utf-8")
        if type(stderr) is bytes:
            stderr = stderr.decode("utf-8")

        assert exitCode == expected_exit_code, stderr

        return stdout, stderr

    @staticmethod
    def runOLD(command, cwd=None, expected_exit_code=0):

        some_info = dict(
          command=command,
          cwd=cwd,
          expect_code=expected_exit_code,
        )
        logging.info(f"Helpers.run: running popen, w/ info: {some_info}")

        results = subprocess.Popen(
            command,
            shell=True,
            bufsize=1,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=cwd,
        )

        stdout, stderr = results.communicate()

        if type(stdout) is bytes:
            stdout = stdout.decode("utf-8")
        if type(stderr) is bytes:
            stderr = stderr.decode("utf-8")

        assert results.returncode == expected_exit_code, stderr

        return stdout, stderr

    # badly named: it actually looks in stderr, not stdout.
    @staticmethod
    def run_check_output(command, expected_lines=None, **kwargs):
        if expected_lines is None:
            expected_lines = ["Connected", "Starting operation", "Errors: 0"]

        _, stderr = Helpers.run(command, **kwargs)

        for line in expected_lines:
            assert re.search(line, stderr, re.MULTILINE), 'Line "{0}" not found in output!'.format(
                line,
            )


@pytest.fixture(scope="module")
def helpers():
    return Helpers

