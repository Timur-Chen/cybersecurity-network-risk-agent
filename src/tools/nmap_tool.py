import shutil
import subprocess

from utils.validators import validate_target


def run_safe_nmap_scan(target: str) -> str:
    """
    Run a safe Nmap scan against localhost or a private lab target.

    This function calls the external Nmap command-line tool and returns
    XML output as a string. If Nmap is not installed, the user can still
    use the safer --file mode with an existing XML scan result.

    Args:
        target: Localhost or private IP address.

    Returns:
        Nmap XML output as a string.

    Raises:
        RuntimeError: If Nmap is not installed or the scan fails.
        ValueError: If the target is not allowed.
    """
    validated_target = validate_target(target)

    if shutil.which("nmap") is None:
        raise RuntimeError(
            "Nmap is not installed or is not available in the system PATH. "
            "Use --file mode with an existing Nmap XML scan file instead."
        )

    command = ["nmap", "-sV", "-oX", "-", validated_target]

    completed_process = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=90,
        check=False,
    )

    if completed_process.returncode != 0:
        raise RuntimeError(
            f"Nmap scan failed: {completed_process.stderr.strip()}"
        )

    return completed_process.stdout