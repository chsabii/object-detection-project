🏠 Indoor Object Detection Project

🌟 Overview

This project involves the implementation of an indoor object detection system using the YOLOv8 model. The primary goal is to detect and classify various objects within indoor environments, leveraging state-of-the-art deep learning techniques for accurate predictions.

The project is developed under the supervision of The Islamia University of Bahawalpur and includes a comprehensive pipeline for data preparation, model training, evaluation, and deployment using modern web technologies such as FastAPI and Streamlit.

📂 Dataset

The dataset used for this project contains labeled images of various indoor objects. It is structured as follows:

📸 Training Set: Images and corresponding labels for training.

🧪 Validation Set: Images and labels for evaluating the model during training.

🧾 Test Set: Unseen images for final performance assessment.

🪞 Classes:

🚪 Door

🚪 Cabinet Door

🧊 Refrigerator Door

🪟 Window

🪑 Chair

🛋️ Table

🗄️ Cabinet

🛋️ Couch

🚪 Opened Door

🏗️ Pole

🤖 Model

The project utilizes the YOLOv8 Medium (yolov8m) architecture for object detection. The model is fine-tuned on the custom dataset to optimize performance for the specific indoor objects.

🔑 Key Features:

🏋️ Pre-trained weights (yolov8m.pt) for transfer learning.

⚙️ Hyperparameter tuning, including epochs, learning rate, and batch size.

📊 Performance metrics such as mAP (Mean Average Precision), recall, and F1-score for validation.

🛠️ Pipeline

📊 Data Visualization

Bounding boxes and labels are visualized on random samples from the training dataset to ensure data quality.

🎯 Model Training

Training configuration is defined in yolo.yaml.

Parameters:

🕒 Epochs: 160

⏳ Patience: 20

📦 Batch Size: 16

🚀 Learning Rate: 0.0003

🖼️ Image Size: 640px

Results and metrics (e.g., confusion matrix) are saved for analysis.

📈 Evaluation

Validation metrics include:

mAP @ 0.5:0.95

mAP @ 0.5

mAP @ 0.7

🔄 Recall

💡 F1-Score

🔍 Inference

Inference is performed on test images, and results are visualized with bounding boxes and class labels.

🚀 Deployment

🌐 FastAPI Endpoint

The model is deployed as an API endpoint using FastAPI.

Features include:

📤 Uploading images via HTTP requests.

🔎 Returning predictions with object names, confidence scores, and bounding box coordinates.

🖥️ Streamlit Frontend

A user-friendly web interface built with Streamlit.

Allows users to:

📤 Upload images.

🖼️ Visualize detection results in real time.

📊 Results

Training results are visualized through:

📉 Loss curves

📊 Confusion matrix

Final model metrics:

📈 Mean Average Precision @ 0.5:0.95: [value]

🔄 Recall: [value]

💡 F1-Score: [value]

🛠️ Tools and Libraries

YOLOv8: 🤖 Object detection framework.

FastAPI: 🌐 API development.

Streamlit: 🖥️ Frontend interface.

PyCOCOtools, NumPy, Pandas, Matplotlib, OpenCV: 📊 Data processing and visualization.

WandB: 📈 Experiment tracking.

🏫 Supervision

This project is supervised by the esteemed faculty of The Islamia University of Bahawalpur.

🔮 Future Work

📹 Integration with real-time video streams.

🖥️ Deployment on edge devices.

🌐 Expansion to additional object classes and domains.

🙏 Acknowledgments

Special thanks to The Islamia University of Bahawalpur for their support and guidance throughout this project.
