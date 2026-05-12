from typing import Any

from risk_rules import analyze_service_risk, calculate_overall_risk
from tools.xml_parser import parse_nmap_xml_file
from utils.report_writer import save_report


class CybersecurityRiskAgent:
    """
    Main agent that coordinates the cybersecurity risk analysis workflow.

    The agent receives user input, calls the required tool, interprets scan data,
    applies risk rules, and returns a structured cybersecurity risk report.
    """

    def __init__(self, save_reports: bool = True):
        """
        Initialize the agent.

        Args:
            save_reports: If True, the final report will be saved as a JSON file.
        """
        self.save_reports = save_reports

    def analyze_scan_file(self, file_path: str) -> dict[str, Any]:
        """
        Analyze an existing Nmap XML scan result file.

        Args:
            file_path: Path to a Nmap XML scan result file.

        Returns:
            Final structured cybersecurity risk report.
        """
        scan_data = parse_nmap_xml_file(file_path)
        return self._build_report(scan_data, input_type="scan_file", input_value=file_path)

    def _build_report(
        self,
        scan_data: dict[str, Any],
        input_type: str,
        input_value: str,
    ) -> dict[str, Any]:
        """
        Build the final risk report from parsed scan data.

        Args:
            scan_data: Parsed scan data returned by the XML parser tool.
            input_type: Type of input used by the user.
            input_value: Original user input value.

        Returns:
            Final report dictionary.
        """
        findings: list[dict[str, Any]] = []

        for service in scan_data["services"]:
            risk = analyze_service_risk(
                port=service["port"],
                service_name=service["service"],
            )

            findings.append(
                {
                    "host": service["host"],
                    "port": service["port"],
                    "protocol": service["protocol"],
                    "service": service["service"],
                    "state": service["state"],
                    "product": service["product"],
                    "risk": risk,
                }
            )

        overall_risk = calculate_overall_risk(findings)

        result = {
            "agent": "Cybersecurity Network Risk Analyzer Agent",
            "input_type": input_type,
            "input_value": input_value,
            "target": scan_data["target"],
            "open_port_count": scan_data["open_port_count"],
            "findings": findings,
            "overall_risk": overall_risk,
        }

        if self.save_reports:
            report_path = save_report(result)
            result["saved_report"] = report_path

        return result