import cv2
import torch
import numpy as np
import pyzed.sl as sl
from ultralytics import YOLO

# Load YOLOv8 models
bottle_model = YOLO("bottle.pt")
mallet_model = YOLO("mallet.pt")

# Initialize the ZED2i camera
zed = sl.Camera()
init_params = sl.InitParameters()
init_params.camera_resolution = sl.RESOLUTION.HD720
init_params.depth_mode = sl.DEPTH_MODE.NONE  # No depth required for 2D detection

if zed.open(init_params) != sl.ERROR_CODE.SUCCESS:
    print("Failed to open ZED camera")
    exit(1)

image = sl.Mat()

while True:
    if zed.grab() == sl.ERROR_CODE.SUCCESS:
        zed.retrieve_image(image, sl.VIEW.LEFT)
        frame = image.get_data()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)  # Convert to OpenCV format

        # Run YOLO object detection on both models
        bottle_results = bottle_model(frame)
        mallet_results = mallet_model(frame)

        # Function to draw bounding boxes
        def draw_results(results, frame, color):
            for result in results:
                boxes = result.boxes.xyxy.cpu().numpy()  # Extract bounding boxes
                confidences = result.boxes.conf.cpu().numpy()  # Extract confidences
                for i, box in enumerate(boxes):
                    x1, y1, x2, y2 = map(int, box)
                    confidence = confidences[i]
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                    cv2.putText(frame, f"{result.names[0]} {confidence:.2f}",
                                (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        draw_results(bottle_results, frame, (0, 255, 0))  # Green for bottle
        draw_results(mallet_results, frame, (0, 0, 255))  # Red for mallet

        # Display the result
        cv2.imshow("ZED2i Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

zed.close()
cv2.destroyAllWindows()
