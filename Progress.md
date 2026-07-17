# Project Progress Tracker

Project: "How Small Can a Safety-Critical Detector Get?" — PPE compression benchmark + deployed detector

Update this file every session. Check a box when done, add a one-line note if something's blocked.

---

## Phase 0 — Setup

- [x] Project folder scaffolded (`ppe-compliance-detector/`)
- [x] Python venv created + activated
- [x] Core packages installed (`ultralytics`, `onnxruntime`, `opencv-python`, `pandas`, `pyyaml`, `kaggle`)
- [x] Kaggle API token created and placed at `~/.kaggle/kaggle.json`

## Phase 1 — Data

- [x] Downloaded Kaggle "Hard Hat Detection" dataset → `data/raw/`
- [x] Ran `voc_to_yolo.py` → converts XML labels to YOLO `.txt` + splits train/val/test
- [x] Verified `data/merged/images/train` count == `data/merged/labels/train` count
- [x] Confirmed `data/ppe.yaml` written correctly == `working on the colabe`

## Phase 2 — Baseline Model

- [x] Wrote/ran `training/train.py` (YOLOv8n fine-tune, 100 epochs, early stopping)
- [x] Checked training curves (loss + mAP over epochs — did it plateau or still improving?)
- [x] Ran `model.val()` — recorded overall mAP@0.5
- [x] Recorded per-class mAP@0.5 (especially `head` class — the hard/important one)
- [x] Exported baseline to ONNX (`models/baseline.onnx`)

## Phase 3 — Compression Benchmark (the headline deliverable)

- [ ] Quantized variant (INT8 dynamic quantization) — exported + evaluated
- [ ] Pruned variant — exported + evaluated
- [ ] Distilled variant (tiny model trained on YOLOv8s soft labels) — exported + evaluated
- [ ] Ran `benchmark.py` on all 4 variants (size, mAP, CPU latency)
- [ ] Filled in comparison table
- [ ] Wrote 1-2 page findings summary (becomes summit abstract draft)

## Phase 4 — Backend Pipeline

- [ ] FastAPI inference endpoint (`backend/app/inference.py`)
- [ ] Rule engine — person/PPE matching logic (`backend/app/rule_engine.py`)
- [ ] Postgres schema for violations
- [ ] MinIO snapshot storage wired up
- [ ] Alert dispatch (webhook + email)
- [ ] Debounce/cooldown logic
- [ ] Backend Dockerized

## Phase 5 — Frontend Dashboard

- [ ] Live feed view (canvas overlay)
- [ ] Violation log table
- [ ] Stats/charts page
- [ ] WebSocket live updates
- [ ] Full `docker-compose up` works end-to-end

## Phase 6 — Wrap-up

- [ ] README with architecture diagram + benchmark table + demo GIF
- [ ] Postmortem written
- [ ] Summit abstract drafted from findings
- [ ] LinkedIn post drafted

---

## Current blocker / note

(update this line each session so next session picks up instantly)

> Next step: run `python voc_to_yolo.py` from project root, verify train/val/test counts match between images and labels.
