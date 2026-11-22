# VLM Lab — Video Understanding × Edge AI × IoT

A modular, local-first monorepo for training and evaluating small Vision-Language Models (VLMs) on public video datasets, and publishing **validated** events to IoT consumers.

> Status: starter scaffold. No dataset, model weights, benchmark scores, or trained checkpoint is included. MQTT demo outputs are *simulations*, not validated anomaly detections.

## Projects
| Project | Purpose | Dataset | Status |
|---|---|---|---|
| [Industrial anomaly](projects/industrial-anomaly/README.md) | Detect anomalous machine processes and explain evidence | IPAD | Planned |
| [Smart-home activities](projects/smart-home-activities/README.md) | Recognize activities and trigger contextual events | Toyota Smarthome | Planned |
| [Security video](projects/security-video/README.md) | Evaluate abnormal-event recognition | ShanghaiTech Campus | Planned |

## Structure
- `src/vlm/data/` — frame extraction and dataset indexing
- `src/vlm/inference/` — local VLM inference adapters
- `src/vlm/training/` — LoRA training experiments (not yet implemented)
- `src/vlm/evaluation/` — classification metrics
- `src/vlm/iot/` — MQTT adapter, event schema
- `configs/` — versioned defaults
- `docs/` — architecture, milestones, reproducibility
- `scripts/` — executable CLI examples

## Quickstart (Windows / Python 3.11 recommended)
```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
python scripts/extract_frames.py --video path/to/clip.mp4 --output data/frames/clip01 --fps 1 --max-frames 30
python scripts/evaluate.py --truth examples/labels.csv --predictions examples/predictions.csv
pytest
```
Linux/macOS: `python3 -m venv .venv && source .venv/bin/activate`.

For optional image inference:
```bash
pip install -e ".[vlm]"
python scripts/infer_image.py --image path/to/frame.jpg --model HuggingFaceTB/SmolVLM-256M-Instruct
```
Inference loads model weights from Hugging Face and may exhaust 4GB VRAM; start with a single resized image, monitor memory and choose CPU if necessary. This is a zero-shot baseline, **not** a fine-tuned anomaly detector.

## Reproducibility
- Download datasets from official providers only, read licensing/access requirements.
- Keep original videos, personally identifying material, datasets and model checkpoints **out of git**.
- Split **by source video/scene**, not random frames, to avoid leakage.
- Track seeds, model revision, labels, clip IDs and hardware metrics.
- For safety-critical scenarios, predictions should trigger alerts, not automatic irreversible actions.

## Roadmap
1. Build IPAD manifest with video-level labels and leakage-safe splits.
2. Zero-shot VLM baseline on sampled frames, compare with image-only baseline.
3. Label verified clips, fine-tune small VLM with LoRA/QLoRA only if memory permits.
4. Evaluate precision/recall/F1, false alarms per hour, latency and GPU memory.
5. Deploy event flow via MQTT with acknowledgement and human review.

See [architecture](docs/architecture.md) and [milestones](docs/roadmap.md).
