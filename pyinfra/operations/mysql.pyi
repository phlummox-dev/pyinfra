import typing
import pyinfra

def sql(
    sql,
    database=None,
    # Details for speaking to MySQL via `mysql` CLI
    mysql_user=None,
    mysql_password=None,
    mysql_host=None,
    mysql_port=None,
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
def user(
    user,
    present=True,
    user_hostname="localhost",
    password=None,
    privileges=None,
    # MySQL REQUIRE SSL/TLS options
    require=None,  # SSL or X509
    require_cipher=False,
    require_issuer=False,
    require_subject=False,
    # MySQL WITH resource limit options
    max_connections=None,
    max_queries_per_hour=None,
    max_updates_per_hour=None,
    max_connections_per_hour=None,
    # Details for speaking to MySQL via `mysql` CLI via `mysql` CLI
    mysql_user=None,
    mysql_password=None,
    mysql_host=None,
    mysql_port=None,
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
def database(
    database,
    # Desired database settings
    present=True,
    collate=None,
    charset=None,
    user=None,
    user_hostname="localhost",
    user_privileges="ALL",
    # Details for speaking to MySQL via `mysql` CLI
    mysql_user=None,
    mysql_password=None,
    mysql_host=None,
    mysql_port=None,
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
def privileges(
    user,
    privileges,
    user_hostname="localhost",
    database="*",
    table="*",
    flush=True,
    with_grant_option=False,
    # Details for speaking to MySQL via `mysql` CLI
    mysql_user=None,
    mysql_password=None,
    mysql_host=None,
    mysql_port=None,
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
def dump(
    dest,
    database=None,
    # Details for speaking to MySQL via `mysql` CLI
    mysql_user=None,
    mysql_password=None,
    mysql_host=None,
    mysql_port=None,
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
def load(
    src,
    database=None,
    # Details for speaking to MySQL via `mysql` CLI
    mysql_user=None,
    mysql_password=None,
    mysql_host=None,
    mysql_port=None,
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
