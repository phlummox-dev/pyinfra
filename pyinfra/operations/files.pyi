import typing
import pyinfra

def download(
    src,
    dest,
    user=None,
    group=None,
    mode=None,
    cache_time=None,
    force=False,
    sha256sum=None,
    sha1sum=None,
    md5sum=None,
    _sudo: typing.Optional[bool] = None,
    _sudo_user: typing.Optional[bool] = None,
    _use_sudo_login: typing.Optional[bool] = None,
    _use_sudo_password: typing.Optional[bool] = None,
    _preserve_sudo_env: typing.Optional[bool] = None,
    _su_user: typing.Optional[str] = None,
    _use_su_login: typing.Optional[bool] = None,
    _preserve_su_env: typing.Optional[bool] = None,
    _su_shell: typing.Optional[str] = None,
    _doas: typing.Optional[bool] = None,
    _doas_user: typing.Optional[str] = None,
    _shell_executable: typing.Optional[str] = None,
    _chdir: typing.Optional[str] = None,
    _env: typing.Optional[typing.Mapping[str, str]] = None,
    _success_exit_codes: typing.Optional[typing.Iterable[int]] = None,
    _timeout: typing.Optional[int] = None,
    _get_pty: typing.Optional[bool] = None,
    _stdin: typing.Optional[typing.Union[str, list, tuple]] = None,
    name: typing.Optional[str] = None,
    _ignore_errors: typing.Optional[bool] = None,
    _precondition: typing.Optional[str] = None,
    _postcondition: typing.Optional[str] = None,
    _on_success: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _on_error: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _parallel: typing.Optional[int] = None,
    _run_once: typing.Optional[bool] = None,
    _serial: typing.Optional[bool] = None,
): ...
def line(
    path,
    line,
    present=True,
    replace=None,
    flags=None,
    backup=False,
    interpolate_variables=False,
    escape_regex_characters=False,
    assume_present=False,
    _sudo: typing.Optional[bool] = None,
    _sudo_user: typing.Optional[bool] = None,
    _use_sudo_login: typing.Optional[bool] = None,
    _use_sudo_password: typing.Optional[bool] = None,
    _preserve_sudo_env: typing.Optional[bool] = None,
    _su_user: typing.Optional[str] = None,
    _use_su_login: typing.Optional[bool] = None,
    _preserve_su_env: typing.Optional[bool] = None,
    _su_shell: typing.Optional[str] = None,
    _doas: typing.Optional[bool] = None,
    _doas_user: typing.Optional[str] = None,
    _shell_executable: typing.Optional[str] = None,
    _chdir: typing.Optional[str] = None,
    _env: typing.Optional[typing.Mapping[str, str]] = None,
    _success_exit_codes: typing.Optional[typing.Iterable[int]] = None,
    _timeout: typing.Optional[int] = None,
    _get_pty: typing.Optional[bool] = None,
    _stdin: typing.Optional[typing.Union[str, list, tuple]] = None,
    name: typing.Optional[str] = None,
    _ignore_errors: typing.Optional[bool] = None,
    _precondition: typing.Optional[str] = None,
    _postcondition: typing.Optional[str] = None,
    _on_success: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _on_error: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _parallel: typing.Optional[int] = None,
    _run_once: typing.Optional[bool] = None,
    _serial: typing.Optional[bool] = None,
): ...
def replace(
    path,
    text=None,
    replace=None,
    flags=None,
    backup=False,
    interpolate_variables=False,
    match=None,  # deprecated
    _sudo: typing.Optional[bool] = None,
    _sudo_user: typing.Optional[bool] = None,
    _use_sudo_login: typing.Optional[bool] = None,
    _use_sudo_password: typing.Optional[bool] = None,
    _preserve_sudo_env: typing.Optional[bool] = None,
    _su_user: typing.Optional[str] = None,
    _use_su_login: typing.Optional[bool] = None,
    _preserve_su_env: typing.Optional[bool] = None,
    _su_shell: typing.Optional[str] = None,
    _doas: typing.Optional[bool] = None,
    _doas_user: typing.Optional[str] = None,
    _shell_executable: typing.Optional[str] = None,
    _chdir: typing.Optional[str] = None,
    _env: typing.Optional[typing.Mapping[str, str]] = None,
    _success_exit_codes: typing.Optional[typing.Iterable[int]] = None,
    _timeout: typing.Optional[int] = None,
    _get_pty: typing.Optional[bool] = None,
    _stdin: typing.Optional[typing.Union[str, list, tuple]] = None,
    name: typing.Optional[str] = None,
    _ignore_errors: typing.Optional[bool] = None,
    _precondition: typing.Optional[str] = None,
    _postcondition: typing.Optional[str] = None,
    _on_success: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _on_error: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _parallel: typing.Optional[int] = None,
    _run_once: typing.Optional[bool] = None,
    _serial: typing.Optional[bool] = None,
): ...
def sync(
    src,
    dest,
    user=None,
    group=None,
    mode=None,
    delete=False,
    exclude=None,
    exclude_dir=None,
    add_deploy_dir=True,
    _sudo: typing.Optional[bool] = None,
    _sudo_user: typing.Optional[bool] = None,
    _use_sudo_login: typing.Optional[bool] = None,
    _use_sudo_password: typing.Optional[bool] = None,
    _preserve_sudo_env: typing.Optional[bool] = None,
    _su_user: typing.Optional[str] = None,
    _use_su_login: typing.Optional[bool] = None,
    _preserve_su_env: typing.Optional[bool] = None,
    _su_shell: typing.Optional[str] = None,
    _doas: typing.Optional[bool] = None,
    _doas_user: typing.Optional[str] = None,
    _shell_executable: typing.Optional[str] = None,
    _chdir: typing.Optional[str] = None,
    _env: typing.Optional[typing.Mapping[str, str]] = None,
    _success_exit_codes: typing.Optional[typing.Iterable[int]] = None,
    _timeout: typing.Optional[int] = None,
    _get_pty: typing.Optional[bool] = None,
    _stdin: typing.Optional[typing.Union[str, list, tuple]] = None,
    name: typing.Optional[str] = None,
    _ignore_errors: typing.Optional[bool] = None,
    _precondition: typing.Optional[str] = None,
    _postcondition: typing.Optional[str] = None,
    _on_success: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _on_error: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _parallel: typing.Optional[int] = None,
    _run_once: typing.Optional[bool] = None,
    _serial: typing.Optional[bool] = None,
): ...
def rsync(
    src,
    dest,
    flags=["-ax", "--delete"],
    _sudo: typing.Optional[bool] = None,
    _sudo_user: typing.Optional[bool] = None,
    _use_sudo_login: typing.Optional[bool] = None,
    _use_sudo_password: typing.Optional[bool] = None,
    _preserve_sudo_env: typing.Optional[bool] = None,
    _su_user: typing.Optional[str] = None,
    _use_su_login: typing.Optional[bool] = None,
    _preserve_su_env: typing.Optional[bool] = None,
    _su_shell: typing.Optional[str] = None,
    _doas: typing.Optional[bool] = None,
    _doas_user: typing.Optional[str] = None,
    _shell_executable: typing.Optional[str] = None,
    _chdir: typing.Optional[str] = None,
    _env: typing.Optional[typing.Mapping[str, str]] = None,
    _success_exit_codes: typing.Optional[typing.Iterable[int]] = None,
    _timeout: typing.Optional[int] = None,
    _get_pty: typing.Optional[bool] = None,
    _stdin: typing.Optional[typing.Union[str, list, tuple]] = None,
    name: typing.Optional[str] = None,
    _ignore_errors: typing.Optional[bool] = None,
    _precondition: typing.Optional[str] = None,
    _postcondition: typing.Optional[str] = None,
    _on_success: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _on_error: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _parallel: typing.Optional[int] = None,
    _run_once: typing.Optional[bool] = None,
    _serial: typing.Optional[bool] = None,
): ...
def get(
    src,
    dest,
    add_deploy_dir=True,
    create_local_dir=False,
    force=False,
    _sudo: typing.Optional[bool] = None,
    _sudo_user: typing.Optional[bool] = None,
    _use_sudo_login: typing.Optional[bool] = None,
    _use_sudo_password: typing.Optional[bool] = None,
    _preserve_sudo_env: typing.Optional[bool] = None,
    _su_user: typing.Optional[str] = None,
    _use_su_login: typing.Optional[bool] = None,
    _preserve_su_env: typing.Optional[bool] = None,
    _su_shell: typing.Optional[str] = None,
    _doas: typing.Optional[bool] = None,
    _doas_user: typing.Optional[str] = None,
    _shell_executable: typing.Optional[str] = None,
    _chdir: typing.Optional[str] = None,
    _env: typing.Optional[typing.Mapping[str, str]] = None,
    _success_exit_codes: typing.Optional[typing.Iterable[int]] = None,
    _timeout: typing.Optional[int] = None,
    _get_pty: typing.Optional[bool] = None,
    _stdin: typing.Optional[typing.Union[str, list, tuple]] = None,
    name: typing.Optional[str] = None,
    _ignore_errors: typing.Optional[bool] = None,
    _precondition: typing.Optional[str] = None,
    _postcondition: typing.Optional[str] = None,
    _on_success: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _on_error: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _parallel: typing.Optional[int] = None,
    _run_once: typing.Optional[bool] = None,
    _serial: typing.Optional[bool] = None,
): ...
def put(
    src,
    dest,
    user=None,
    group=None,
    mode=None,
    add_deploy_dir=True,
    create_remote_dir=True,
    force=False,
    assume_exists=False,
    _sudo: typing.Optional[bool] = None,
    _sudo_user: typing.Optional[bool] = None,
    _use_sudo_login: typing.Optional[bool] = None,
    _use_sudo_password: typing.Optional[bool] = None,
    _preserve_sudo_env: typing.Optional[bool] = None,
    _su_user: typing.Optional[str] = None,
    _use_su_login: typing.Optional[bool] = None,
    _preserve_su_env: typing.Optional[bool] = None,
    _su_shell: typing.Optional[str] = None,
    _doas: typing.Optional[bool] = None,
    _doas_user: typing.Optional[str] = None,
    _shell_executable: typing.Optional[str] = None,
    _chdir: typing.Optional[str] = None,
    _env: typing.Optional[typing.Mapping[str, str]] = None,
    _success_exit_codes: typing.Optional[typing.Iterable[int]] = None,
    _timeout: typing.Optional[int] = None,
    _get_pty: typing.Optional[bool] = None,
    _stdin: typing.Optional[typing.Union[str, list, tuple]] = None,
    name: typing.Optional[str] = None,
    _ignore_errors: typing.Optional[bool] = None,
    _precondition: typing.Optional[str] = None,
    _postcondition: typing.Optional[str] = None,
    _on_success: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _on_error: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _parallel: typing.Optional[int] = None,
    _run_once: typing.Optional[bool] = None,
    _serial: typing.Optional[bool] = None,
): ...
def template(
    src,
    dest,
    user=None,
    group=None,
    mode=None,
    create_remote_dir=True,
    _sudo: typing.Optional[bool] = None,
    _sudo_user: typing.Optional[bool] = None,
    _use_sudo_login: typing.Optional[bool] = None,
    _use_sudo_password: typing.Optional[bool] = None,
    _preserve_sudo_env: typing.Optional[bool] = None,
    _su_user: typing.Optional[str] = None,
    _use_su_login: typing.Optional[bool] = None,
    _preserve_su_env: typing.Optional[bool] = None,
    _su_shell: typing.Optional[str] = None,
    _doas: typing.Optional[bool] = None,
    _doas_user: typing.Optional[str] = None,
    _shell_executable: typing.Optional[str] = None,
    _chdir: typing.Optional[str] = None,
    _env: typing.Optional[typing.Mapping[str, str]] = None,
    _success_exit_codes: typing.Optional[typing.Iterable[int]] = None,
    _timeout: typing.Optional[int] = None,
    _get_pty: typing.Optional[bool] = None,
    _stdin: typing.Optional[typing.Union[str, list, tuple]] = None,
    name: typing.Optional[str] = None,
    _ignore_errors: typing.Optional[bool] = None,
    _precondition: typing.Optional[str] = None,
    _postcondition: typing.Optional[str] = None,
    _on_success: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _on_error: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _parallel: typing.Optional[int] = None,
    _run_once: typing.Optional[bool] = None,
    _serial: typing.Optional[bool] = None,
    **data
): ...
def link(
    path,
    target=None,
    present=True,
    assume_present=False,
    user=None,
    group=None,
    symbolic=True,
    create_remote_dir=True,
    force=False,
    force_backup=True,
    force_backup_dir=None,
    _sudo: typing.Optional[bool] = None,
    _sudo_user: typing.Optional[bool] = None,
    _use_sudo_login: typing.Optional[bool] = None,
    _use_sudo_password: typing.Optional[bool] = None,
    _preserve_sudo_env: typing.Optional[bool] = None,
    _su_user: typing.Optional[str] = None,
    _use_su_login: typing.Optional[bool] = None,
    _preserve_su_env: typing.Optional[bool] = None,
    _su_shell: typing.Optional[str] = None,
    _doas: typing.Optional[bool] = None,
    _doas_user: typing.Optional[str] = None,
    _shell_executable: typing.Optional[str] = None,
    _chdir: typing.Optional[str] = None,
    _env: typing.Optional[typing.Mapping[str, str]] = None,
    _success_exit_codes: typing.Optional[typing.Iterable[int]] = None,
    _timeout: typing.Optional[int] = None,
    _get_pty: typing.Optional[bool] = None,
    _stdin: typing.Optional[typing.Union[str, list, tuple]] = None,
    name: typing.Optional[str] = None,
    _ignore_errors: typing.Optional[bool] = None,
    _precondition: typing.Optional[str] = None,
    _postcondition: typing.Optional[str] = None,
    _on_success: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _on_error: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _parallel: typing.Optional[int] = None,
    _run_once: typing.Optional[bool] = None,
    _serial: typing.Optional[bool] = None,
): ...
def file(
    path,
    present=True,
    assume_present=False,
    user=None,
    group=None,
    mode=None,
    touch=False,
    create_remote_dir=True,
    force=False,
    force_backup=True,
    force_backup_dir=None,
    _sudo: typing.Optional[bool] = None,
    _sudo_user: typing.Optional[bool] = None,
    _use_sudo_login: typing.Optional[bool] = None,
    _use_sudo_password: typing.Optional[bool] = None,
    _preserve_sudo_env: typing.Optional[bool] = None,
    _su_user: typing.Optional[str] = None,
    _use_su_login: typing.Optional[bool] = None,
    _preserve_su_env: typing.Optional[bool] = None,
    _su_shell: typing.Optional[str] = None,
    _doas: typing.Optional[bool] = None,
    _doas_user: typing.Optional[str] = None,
    _shell_executable: typing.Optional[str] = None,
    _chdir: typing.Optional[str] = None,
    _env: typing.Optional[typing.Mapping[str, str]] = None,
    _success_exit_codes: typing.Optional[typing.Iterable[int]] = None,
    _timeout: typing.Optional[int] = None,
    _get_pty: typing.Optional[bool] = None,
    _stdin: typing.Optional[typing.Union[str, list, tuple]] = None,
    name: typing.Optional[str] = None,
    _ignore_errors: typing.Optional[bool] = None,
    _precondition: typing.Optional[str] = None,
    _postcondition: typing.Optional[str] = None,
    _on_success: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _on_error: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _parallel: typing.Optional[int] = None,
    _run_once: typing.Optional[bool] = None,
    _serial: typing.Optional[bool] = None,
): ...
def directory(
    path,
    present=True,
    assume_present=False,
    user=None,
    group=None,
    mode=None,
    recursive=False,
    force=False,
    force_backup=True,
    force_backup_dir=None,
    _no_check_owner_mode=False,
    _no_fail_on_link=False,
    _sudo: typing.Optional[bool] = None,
    _sudo_user: typing.Optional[bool] = None,
    _use_sudo_login: typing.Optional[bool] = None,
    _use_sudo_password: typing.Optional[bool] = None,
    _preserve_sudo_env: typing.Optional[bool] = None,
    _su_user: typing.Optional[str] = None,
    _use_su_login: typing.Optional[bool] = None,
    _preserve_su_env: typing.Optional[bool] = None,
    _su_shell: typing.Optional[str] = None,
    _doas: typing.Optional[bool] = None,
    _doas_user: typing.Optional[str] = None,
    _shell_executable: typing.Optional[str] = None,
    _chdir: typing.Optional[str] = None,
    _env: typing.Optional[typing.Mapping[str, str]] = None,
    _success_exit_codes: typing.Optional[typing.Iterable[int]] = None,
    _timeout: typing.Optional[int] = None,
    _get_pty: typing.Optional[bool] = None,
    _stdin: typing.Optional[typing.Union[str, list, tuple]] = None,
    name: typing.Optional[str] = None,
    _ignore_errors: typing.Optional[bool] = None,
    _precondition: typing.Optional[str] = None,
    _postcondition: typing.Optional[str] = None,
    _on_success: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _on_error: typing.Optional[
        typing.Callable[[pyinfra.api.state.State, pyinfra.api.host.Host, str], None]
    ] = None,
    _parallel: typing.Optional[int] = None,
    _run_once: typing.Optional[bool] = None,
    _serial: typing.Optional[bool] = None,
): ...
