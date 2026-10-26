
from ultralytics import YOLO
from pathlib import Path

# Load the trained PPE detection model
MODEL_PATH = "runs/ppe_detection/yolo11n/weights/best.pt"

# Image you want to test
IMAGE_PATH = "test_image.jpg"

model = YOLO(MODEL_PATH)

# Run prediction
results = model.predict(
    source=IMAGE_PATH,
    conf=0.25,
    save=True
)

print("Prediction completed!")
print("Check the runs/detect/ folder for the output image.")
