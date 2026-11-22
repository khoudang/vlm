import pytest
from vlm.evaluation.metrics import binary_metrics
from vlm.iot.events import AlertEvent
from vlm.iot.mqtt import publish_event


def test_binary_metrics():
    score = binary_metrics([0,1,1],[0,1,0])
    assert score["tp"] == 1 and score["fn"] == 1
    assert score["precision"] == 1 and score["recall"] == 0.5


def test_invalid_labels():
    with pytest.raises(ValueError):
        binary_metrics([0,2], [0,1])


def test_mqtt_dry_run(capsys):
    sent = publish_event(AlertEvent(source_video="test", event_type="demo", summary="ok", model_id="none"))
    assert sent is False
    assert "DRY_RUN" in capsys.readouterr().out
