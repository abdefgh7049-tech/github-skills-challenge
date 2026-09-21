from src.aiops_pipeline import run_pipeline


def test_run_pipeline_returns_detected_and_consumed_anomalies():
    result = run_pipeline("data/service_data.json")

    assert result["records_processed"] == 10
    assert len(result["anomalies_detected"]) == 2
    assert len(result["events_consumed"]) == 2
