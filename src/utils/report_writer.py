import json
from datetime import datetime
from pathlib import Path
from typing import Any


def save_report(result: dict[str, Any], reports_dir: str = "reports") -> str:
    """
    Save the final cybersecurity risk analysis result as a JSON report.

    Args:
        result: Final risk analysis result produced by the agent.
        reports_dir: Directory where report files should be saved.

    Returns:
        Path to the saved JSON report file.
    """
    output_dir = Path(reports_dir)
    output_dir.mkdir(exist_ok=True)

    file_name = f"risk_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    report_path = output_dir / file_name

    with open(report_path, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4)

    return str(report_path)