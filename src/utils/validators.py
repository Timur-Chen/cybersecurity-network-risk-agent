from pathlib import Path


def validate_xml_file(file_path: str) -> Path:
    """
    Validate that the provided path exists and points to a non-empty XML file.
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