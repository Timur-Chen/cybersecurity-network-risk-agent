import json
import sys
from pathlib import Path

sys.path.append("src")

from utils.report_writer import save_report


def test_save_report_creates_json_file(tmp_path):
    """
    Test that the report writer saves a JSON report file.
    """
    result = {
        "agent": "Cybersecurity Network Risk Analyzer Agent",
        "target": "127.0.0.1",
        "open_port_count": 1,
        "findings": [],
        "overall_risk": {
            "overall_score": 0,
            "overall_level": "Low",
            "conclusion": "Test conclusion",
        },
    }

    report_path = save_report(result, reports_dir=str(tmp_path))

    saved_file = Path(report_path)

    assert saved_file.exists()
    assert saved_file.suffix == ".json"

    with open(saved_file, "r", encoding="utf-8") as file:
        loaded_data = json.load(file)

    assert loaded_data["agent"] == "Cybersecurity Network Risk Analyzer Agent"
    assert loaded_data["target"] == "127.0.0.1"
    assert loaded_data["overall_risk"]["overall_level"] == "Low"