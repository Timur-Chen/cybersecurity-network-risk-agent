from pathlib import Path
import ipaddress


def validate_xml_file(file_path: str) -> Path:
    """
    Validate that the provided path exists and points to a non-empty XML file.

    Args:
        file_path: Path to a Nmap XML scan result file.

    Returns:
        A Path object for the validated XML file.

    Raises:
        ValueError: If the file path is invalid, unsupported, or empty.
    """
    path = Path(file_path)

    if not path.exists():
        raise ValueError(f"File does not exist: {file_path}")

    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")

    if path.suffix.lower() != ".xml":
        raise ValueError("Only XML scan result files are supported.")

    if path.stat().st_size == 0:
        raise ValueError("The XML file is empty.")

    return path


def validate_target(target: str) -> str:
    """
    Validate that the target is safe for optional live scanning.

    The system only allows localhost and private IP addresses. This prevents
    accidental or unauthorized scanning of public systems.

    Args:
        target: Target host or IP address.

    Returns:
        Validated target string.

    Raises:
        ValueError: If the target is empty, invalid, or not allowed.
    """
    if not target or not target.strip():
        raise ValueError("Target cannot be empty.")

    cleaned_target = target.strip()

    if cleaned_target in {"localhost", "127.0.0.1", "::1"}:
        return cleaned_target

    try:
        ip_address = ipaddress.ip_address(cleaned_target)
    except ValueError as error:
        raise ValueError(
            "Only localhost or private IP addresses are allowed for live scanning."
        ) from error

    if ip_address.is_loopback or ip_address.is_private:
        return cleaned_target

    raise ValueError(
        "Only localhost or private IP addresses are allowed for live scanning."
    )