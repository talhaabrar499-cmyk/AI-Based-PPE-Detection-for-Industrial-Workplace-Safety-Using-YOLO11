# AI-Based PPE Detection for Industrial Workplace Safety Using YOLO11

## 1. Introduction

In this project, I developed a computer vision system to detect Personal Protective Equipment (PPE) in workplace images and videos using YOLO11. The main purpose of this project is to use artificial intelligence to help monitor workplace safety and identify PPE-related issues.

In industrial environments, workers need to wear safety equipment such as helmets and safety vests. Manually checking every worker can take a lot of time, so I wanted to explore how object detection can help automate this process.

## 2. Project Objectives

The main objectives of this project are:

- To use a PPE dataset for training an object detection model.
- To train a YOLO11n model to detect PPE-related objects.
- To evaluate the model using validation results and performance graphs.
- To test the trained model on images and videos.
- To develop a simple web interface using Gradio.
- To identify possible improvements for better detection performance.

## 3. Technologies Used

- Python
- YOLO11n
- Ultralytics
- Roboflow
- OpenCV
- Gradio
- Google Colab
- GitHub

## 4. Dataset

I used a PPE detection dataset downloaded from Roboflow in YOLO format. The dataset contains images and annotations that are used to train and evaluate the model.

The dataset is divided into training, validation, and testing subsets, as defined by the downloaded dataset configuration.

The dataset includes PPE-related classes. The exact class names and number of images can be checked in the dataset configuration and downloaded files.

## 5. Project Workflow

The project follows these steps:

1. Download the dataset from Roboflow.
2. Inspect the dataset and its annotations.
3. Train the YOLO11n model.
4. Evaluate the model using validation results and a confusion matrix.
5. Test the model on custom images.
6. Perform PPE detection on videos.
7. Develop a Gradio interface for image and video detection.
8. Analyze the results and identify possible improvements.

## 6. Model Training

I used the YOLO11n model because it is a lightweight object detection model. The model was trained using the PPE dataset, and its performance was checked using the training and validation outputs.

The training process can be adjusted by changing parameters such as the number of epochs, image size, batch size, and confidence threshold.

## 7. Results

After training the model, I tested it on images and videos to observe how well it detects PPE-related objects. I also examined the training graphs, confusion matrix, and prediction outputs to understand the model's performance.

The actual performance metrics, including precision, recall, mAP@50, and mAP@50-95, should be added after checking the evaluation results produced by my training run.

## 8. Web Application

I created a Gradio interface to make the model easier to use. It allows users to upload images or videos and view the corresponding detection results.

The interface provides a simple way to test the trained model without having to write prediction code manually.

## 9. Improvements and Future Work

There are several improvements that I can make to this project:

- Add more images for underrepresented PPE classes.
- Compare YOLO11n with other model sizes.
- Test different confidence thresholds.
- Evaluate the model under different lighting conditions and camera angles.
- Improve video processing speed.
- Improve the web interface and add more options for users.
- Explore how to identify workers who may be missing required PPE.

These improvements could help make the system more accurate and useful in practical workplace environments.

## 10. Conclusion

Through this project, I learned how to prepare a dataset, train an object detection model, evaluate its performance, and use it for image and video detection. I also learned how to develop a simple web interface using Gradio.

Although the project provides a starting point for automated PPE detection, further testing and improvements are needed before it can be relied upon in real workplace safety monitoring.

## 11. Limitations

The model may make incorrect predictions when objects are small, hidden, or captured under poor lighting conditions. Detecting PPE objects does not automatically confirm whether a worker is following all safety requirements.

Therefore, the system should be treated as a prototype to support safety monitoring, not as a replacement for human inspection.

## 12. Project Files

The repository may contain the following files:

- `Final_Project.ipynb` — Main project notebook.
- `README.md` — Project description and documentation.
- `train.py` — Model training script, if separated from the notebook.
- `predict.py` — Prediction script, if separated from the notebook.
- `requirements.txt` — Required Python libraries.

## Dataset Attribution

The dataset was obtained from Roboflow. Please refer to the original dataset's license and terms before redistributing its images or annotations.
