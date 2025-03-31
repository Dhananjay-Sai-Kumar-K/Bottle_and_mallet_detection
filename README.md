# 🍾🔨 Real-time Object Detection with ZED2i and YOLOv8 🚀

This project demonstrates real-time object detection using the ZED2i stereo camera and YOLOv8 models. It detects bottles 🍾 and mallets 🔨 in the camera's field of view.

## 🛠️ Prerequisites

* **ZED SDK:** Install the ZED SDK from [Stereolabs](https://www.stereolabs.com/developers/).
* **Python:** Python 3.x is required.
* **Libraries:** Install the necessary Python libraries:

    ```bash
    pip install opencv-python torch numpy pyzed-wrapper ultralytics
    ```

* **YOLOv8 Models:** Download the `bottle.pt` and `mallet.pt` YOLOv8 models and place them in the same directory as the Python script. You can train your own models or use pre-trained ones if available.

## ⚙️ Setup

1.  **Connect ZED2i Camera:** Connect your ZED2i camera to your computer.
2.  **Install ZED SDK:** Follow the installation instructions provided by Stereolabs.
3.  **Install Python Libraries:** Install the required Python libraries using `pip`.
4.  **Download YOLO Models:** Download `bottle.pt` and `mallet.pt` and ensure they are accessible by the script.

## 🏃‍♂️ Running the Script

1.  **Execute the Python Script:** Run the `main.py` script:

    ```bash
    python main.py
    ```

2.  **View the Results:** The script will open a window displaying the real-time video feed from the ZED2i camera with bounding boxes around detected bottles (green) and mallets (red).
3.  **Exit:** Press the 'q' key to close the window and exit the script.

## 📄 Code Explanation

* **Import Libraries:** The script imports `cv2` (OpenCV), `torch`, `numpy`, `pyzed.sl` (ZED SDK), and `ultralytics.YOLO` (YOLOv8).
* **Load YOLO Models:** The `bottle.pt` and `mallet.pt` YOLOv8 models are loaded.
* **Initialize ZED Camera:** The ZED2i camera is initialized with HD720 resolution and depth mode disabled.
* **Capture and Process Frames:** The script captures frames from the ZED2i camera, converts them to OpenCV format, and runs object detection using both YOLO models.
* **Draw Bounding Boxes:** The `draw_results` function draws bounding boxes around detected objects with labels and confidence scores.
* **Display Results:** The processed frames are displayed in a window.
* **Exit:** The script exits when the 'q' key is pressed.


## 💡 Future Improvements

* **Depth Integration:** Incorporate depth data from the ZED2i camera to obtain 3D coordinates of detected objects.
* **Object Tracking:** Implement object tracking to track the movement of detected objects over time.
* **Performance Optimization:** Optimize the code for real-time performance on resource-constrained devices.
* **More Classes:** Add support for detecting more object classes.
* **Custom Models:** Train custom YOLOv8 models for specific object detection tasks.
* **Record Video:** add the option to record the processed video.
