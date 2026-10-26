
from ultralytics import YOLO
from pathlib import Path

# Path to the downloaded Roboflow dataset
DATA_YAML = "/path/to/your/dataset/data.yaml"

# Load a pretrained YOLOv11 nano model
model = YOLO("yolo11n.pt")

# Train the model
results = model.train(
    data=DATA_YAML,
    epochs=50,
    imgsz=640,
    batch=16,
    project="runs/ppe_detection",
    name="yolo11n"
)

print("Training completed!")
