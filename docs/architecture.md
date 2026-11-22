# Architecture

```text
Public videos -> Manifest -> Leak-safe split -> Frame sampler -> VLM baseline / fine-tuning
                                                            |
                                                     JSON prediction
                                                            |
                                                     Validation + metrics
                                                            |
                                      MQTT publisher (dry run by default)
                                                            |
                                                 Pi 4 MQTT / dashboard
```

## Design rules
- `data` does not import MQTT or inference.
- `inference` accepts images and prompts; returns text, not hardware commands.
- `iot` validates event payloads, uses dry-run by default; never directly controls actuators.
- Track `source_video`, `frame_timestamp`, `model_id`, `prompt_version` and `review_status`.
- MQTT is optional; laptop can produce JSONL for offline evaluation.
