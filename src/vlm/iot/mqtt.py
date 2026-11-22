def publish_event(event, host="localhost", port=1883, topic="vlm/events/anomaly", dry_run=True):
    """Safe by default: print payload; publish only when explicitly requested."""
    payload = event.model_dump_json()
    if dry_run:
        print(f"DRY_RUN topic={topic} payload={payload}")
        return False
    import paho.mqtt.publish as publish
    publish.single(topic, payload=payload, hostname=host, port=port, qos=1)
    return True
