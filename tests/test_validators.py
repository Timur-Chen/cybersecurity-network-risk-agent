import sys
from pathlib import Path

import pytest

sys.path.append("src")

from utils.validators import validate_target, validate_xml_file


def test_validate_existing_xml_file():
    """
    Test that a valid XML file path is accepted.
    """
    file_path = "examples/sample_scan.xml"

    result = validate_xml_file(file_path)

    assert isinstance(result, Path)
    assert result.exists()


def test_validate_missing_file_rejected():
    """
    Test that a missing XML file is rejected.
    """
    with pytest.raises(ValueError, match="File does not exist"):
        validate_xml_file("examples/missing_file.xml")


def test_validate_wrong_file_extension_rejected(tmp_path):
    """
    Test that non-XML files are rejected.
    """
    test_file = tmp_path / "scan.txt"
    test_file.write_text("not xml content", encoding="utf-8")

    with pytest.raises(ValueError, match="Only XML scan result files are supported"):
        validate_xml_file(str(test_file))


def test_validate_empty_xml_file_rejected(tmp_path):
    """
    Test that an empty XML file is rejected.
    """
    test_file = tmp_path / "empty.xml"
    test_file.write_text("", encoding="utf-8")

    with pytest.raises(ValueError, match="The XML file is empty"):
        validate_xml_file(str(test_file))


def test_validate_localhost_target_allowed():
    """
    Test that localhost is allowed for optional live scanning.
    """
    result = validate_target("127.0.0.1")

    assert result == "127.0.0.1"


def test_validate_private_ip_allowed():
    """
    Test that a private IP address is allowed for optional live scanning.
    """
    result = validate_target("192.168.1.10")

    assert result == "192.168.1.10"


def test_validate_public_ip_rejected():
    """
    Test that a public IP address is rejected for safety.
    """
    with pytest.raises(ValueError, match="Only localhost or private IP addresses are allowed"):
        validate_target("8.8.8.8")