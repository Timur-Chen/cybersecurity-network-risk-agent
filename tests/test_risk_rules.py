import sys

sys.path.append("src")

from risk_rules import analyze_service_risk, calculate_overall_risk


def test_mysql_port_is_high_risk():
    """
    Test that MySQL on port 3306 is classified as High risk.
    """
    result = analyze_service_risk(3306, "mysql")

    assert result["risk_level"] == "High"
    assert result["score"] == 7
    assert "Database" in result["reason"]


def test_telnet_port_is_critical_risk():
    """
    Test that Telnet on port 23 is classified as Critical risk.
    """
    result = analyze_service_risk(23, "telnet")

    assert result["risk_level"] == "Critical"
    assert result["score"] == 9
    assert "unencrypted" in result["reason"]


def test_unknown_port_uses_default_low_risk_rule():
    """
    Test that an unknown port receives a default Low risk classification.
    """
    result = analyze_service_risk(9999, "unknown-service")

    assert result["risk_level"] == "Low"
    assert result["score"] == 2


def test_overall_risk_uses_highest_score():
    """
    Test that the overall risk level is based on the highest detected risk score.
    """
    findings = [
        {"risk": {"score": 5}},
        {"risk": {"score": 7}},
        {"risk": {"score": 2}},
    ]

    result = calculate_overall_risk(findings)

    assert result["overall_score"] == 7
    assert result["overall_level"] == "High"


def test_overall_risk_with_no_findings_is_low():
    """
    Test that no findings produce a Low overall risk result.
    """
    result = calculate_overall_risk([])

    assert result["overall_score"] == 0
    assert result["overall_level"] == "Low"