import xml.etree.ElementTree as ET
from typing import Any

from utils.validators import validate_xml_file


def parse_nmap_xml_file(file_path: str) -> dict[str, Any]:
    """
    Parse an existing Nmap XML scan result file.

    Args:
        file_path: Path to a Nmap XML file.

    Returns:
        A dictionary containing target information and detected open services.
    """
    path = validate_xml_file(file_path)

    try:
        tree = ET.parse(path)
        root = tree.getroot()
    except ET.ParseError as error:
        raise ValueError("Invalid XML content. The file could not be parsed.") from error

    return _parse_nmap_root(root)


def parse_nmap_xml_string(xml_data: str) -> dict[str, Any]:
    """
    Parse Nmap XML content from a string.

    This function can be used if live Nmap scanning is implemented later and
    the Nmap command returns XML output directly.

    Args:
        xml_data: Nmap XML content as a string.

    Returns:
        A dictionary containing target information and detected open services.
    """
    if not xml_data or not xml_data.strip():
        raise ValueError("XML data cannot be empty.")

    try:
        root = ET.fromstring(xml_data)
    except ET.ParseError as error:
        raise ValueError("Invalid XML content. The scan output could not be parsed.") from error

    return _parse_nmap_root(root)


def _parse_nmap_root(root: ET.Element) -> dict[str, Any]:
    """
    Convert parsed Nmap XML data into Python dictionaries and lists.

    Args:
        root: Parsed Nmap XML root element.

    Returns:
        Structured scan data containing target and open services.
    """
    services: list[dict[str, Any]] = []
    target_address = "unknown"

    for host in root.findall("host"):
        address_element = host.find("address")

        if address_element is not None:
            target_address = address_element.get("addr", "unknown")

        for port in host.findall("ports/port"):
            state_element = port.find("state")
            state = "unknown"

            if state_element is not None:
                state = state_element.get("state", "unknown")

            if state != "open":
                continue

            service_element = port.find("service")
            service_name = "unknown"
            product = ""

            if service_element is not None:
                service_name = service_element.get("name", "unknown")
                product = service_element.get("product", "")

            services.append(
                {
                    "host": target_address,
                    "port": int(port.get("portid", 0)),
                    "protocol": port.get("protocol", "tcp"),
                    "state": state,
                    "service": service_name,
                    "product": product,
                }
            )

    return {
        "target": target_address,
        "open_port_count": len(services),
        "services": services,
    }