from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
import cv2
import numpy as np

app = FastAPI()
model = YOLO("my_saved_model.pt")

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    
    if len(contents) == 0:
        return {"error": "No content received, please upload a valid image file."}
    
    np_image = np.frombuffer(contents, np.uint8)
    
    image = cv2.imdecode(np_image, cv2.IMREAD_COLOR)
    if image is None:
        return {"error": "Failed to decode the image."}
    
    # Get results from YOLO model
    results = model.predict(image)
    
    # Extract object names, confidence levels, and bounding box coordinates
    object_info = []
    
    # Iterate over the results
    for result in results:
        # Extract bounding boxes (xywh), confidences, and class IDs
        boxes = result.boxes  # Bounding boxes (x_center, y_center, width, height) and other data
        confidences = boxes.conf  # Confidence scores
        class_ids = boxes.cls  # Class IDs
        names = result.names  # Class names

        # Collect information for each detected object
        for i in range(len(boxes)):
            object_info.append({
                "name": names[int(class_ids[i])],  # Get class name
                "confidence": confidences[i].item(),  # Confidence score
                "box": boxes.xywh[i].tolist()  # Bounding box coordinates (x_center, y_center, width, height)
            })
    
    return {"predictions": object_info}
