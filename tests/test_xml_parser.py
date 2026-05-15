import sys
from pathlib import Path

sys.path.append("src")

from tools.xml_parser import parse_nmap_xml_file


def test_parse_sample_nmap_xml_file():
    """
    Test that the XML parser can read a valid Nmap XML file
    and extract open services correctly.
    """
    file_path = Path("examples/sample_scan.xml")

    result = parse_nmap_xml_file(str(file_path))

    assert result["target"] == "127.0.0.1"
    assert result["open_port_count"] == 3

    services = result["services"]
    ports = [service["port"] for service in services]
    service_names = [service["service"] for service in services]

    assert 22 in ports
    assert 80 in ports
    assert 3306 in ports

    assert "ssh" in service_names
    assert "http" in service_names
    assert "mysql" in service_names