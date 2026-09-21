import runpy

from src.aiops_pipeline import run_pipeline


def test_run_pipeline_returns_detected_and_consumed_anomalies():
    result = run_pipeline("data/service_data.json")

    assert result["records_processed"] == 10
    assert len(result["anomalies_detected"]) == 2
    assert len(result["events_consumed"]) == 2


def test_pipeline_module_prints_cli_summary(capsys):
    runpy.run_module("src.aiops_pipeline", run_name="__main__")

    output = capsys.readouterr().out
    assert "Records processed: 10" in output
    assert "Anomalies detected: 2" in output
    assert "Events consumed: 2" in output
