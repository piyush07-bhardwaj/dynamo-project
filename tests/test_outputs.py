import json
from pathlib import Path


def test_report_is_valid_json_object():
    """Success criterion 1: write a valid JSON object to /app/report.json."""
    report_path = Path("/app/report.json")
    assert report_path.exists(), "report.json was not created"

    report = json.loads(report_path.read_text())
    assert isinstance(report, dict), "report.json must contain a JSON object"
    assert set(report) == {"total_requests", "unique_ips", "top_path"}, (
        "report.json must contain total_requests, unique_ips, and top_path"
    )


def test_report_matches_access_log():
    """Success criterion 2: the JSON summary must accurately reflect /app/access.log."""
    report = json.loads(Path("/app/report.json").read_text())
    assert report == {
        "total_requests": 6,
        "unique_ips": 3,
        "top_path": "/index.html",
    }