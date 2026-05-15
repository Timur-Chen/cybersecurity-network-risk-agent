import sys

sys.path.append("src")

from agent import CybersecurityRiskAgent


def test_agent_analyzes_sample_scan_file_without_saving():
    """
    Test the main agent workflow using the sample Nmap XML file.
    """
    agent = CybersecurityRiskAgent(save_reports=False)

    result = agent.analyze_scan_file("examples/sample_scan.xml")

    assert result["agent"] == "Cybersecurity Network Risk Analyzer Agent"
    assert result["input_type"] == "scan_file"
    assert result["target"] == "127.0.0.1"
    assert result["open_port_count"] == 3

    assert result["overall_risk"]["overall_level"] == "High"
    assert result["overall_risk"]["overall_score"] == 7

    assert "saved_report" not in result


def test_agent_detects_expected_services():
    """
    Test that the agent includes expected services in the final findings.
    """
    agent = CybersecurityRiskAgent(save_reports=False)

    result = agent.analyze_scan_file("examples/sample_scan.xml")

    services = [finding["service"] for finding in result["findings"]]

    assert "ssh" in services
    assert "http" in services
    assert "mysql" in services