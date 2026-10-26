# PPE Detection Using YOLOv11

## Project Overview

This project implements a computer vision system for detecting Personal Protective Equipment (PPE) using the YOLOv11 object detection architecture.

The goal is to identify PPE-related objects in images and support workplace safety monitoring.

## Dataset

- **Source:** Roboflow
- **Project:** PPE Detection
- **Version:** 2
- **Format:** YOLOv11
- **Task:** Object Detection

The dataset was downloaded using the Roboflow Python SDK.

## Technologies Used

- Python
- Ultralytics YOLOv11
- Roboflow
- OpenCV
- Google Colab

## Project Workflow

1. Download the dataset from Roboflow.
2. Inspect and prepare the annotated images.
3. Train the YOLOv11 object detection model.
4. Evaluate model performance.
5. Test predictions on new images.
6. Analyze results and document limitations.

## Installation

```bash
pip install ultralytics roboflow opencv-python
```

## Training

```python
from ultralytics import YOLO

model = YOLO("yolo11n.pt")

model.train(
    data="/path/to/data.yaml",
    epochs=40,
    imgsz=640
)
```

Replace `/path/to/data.yaml` with the actual location of your dataset configuration file.

## Evaluation

Evaluate the trained model using the validation dataset and report precision, recall, mAP@50, and mAP@50-95.

## Results

Training results, evaluation metrics, and prediction examples will be added after experiments are completed.

## Repository Contents

- `README.md` — Project documentation
- `train.py` — Model training script
- `predict.py` — Inference script
- `requirements.txt` — Python dependencies
- `.gitignore` — Files excluded from version control

## Limitations

Detection performance may vary with lighting, image quality, occlusion, and camera angles. The system is intended to support, not replace, workplace safety procedures.

## Dataset Attribution

The dataset was obtained from Roboflow. Refer to the original dataset's licensing terms before redistributing images or annotations.
