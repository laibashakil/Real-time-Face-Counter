# Real-Time Face Counter
 
This GitHub repository contains a Python script that utilizes OpenCV to perform real-time face detection and counting using your webcam. It's perfect for event organizers, researchers, or anyone interested in analyzing crowds or experimenting with computer vision.

![det](https://github.com/laibashakil/Real-time-Face-Counter/assets/96187426/f04c9618-09e1-4fe1-b94c-b6efe5661cba)
### Features:

-   **Real-time detection:** Accurately detects faces in live video streams from your webcam.
-   **Face counting:** Displays the total number of detected faces on the video frame.
-   **OpenCV powered:** Leverages the capabilities of the robust OpenCV library for efficient detection.
-   **User-friendly:** No complex setups, simply run the script and point your camera.
-   **Open-source and customizable:** Modify the code to tailor it to your needs.

### Requirements:

-   Python 3.6+
-   OpenCV (`pip install opencv-python`)

### How to use:

1.  Clone this repository or download the script.
2.  Run the script:  `python main.py`.
3.  Point your webcam towards the area you want to analyze.
4.  The script will display the video feed with bounding boxes around detected faces and the total count.
5.  Press `q` to exit the application.

### Contributing:

We welcome contributions to improve this script! Feel free to fork the repository and submit pull requests with enhancements or bug fixes.

### License:

This project is licensed under the MIT License. See the LICENSE file for details.

### Additional notes:

-   This script uses the Haar Cascade classifier, which may not be perfect in all lighting conditions or scenarios.
-   For more advanced face detection, consider exploring deeper learning techniques.
-   You can experiment with different values for `scaleFactor` and `minNeighbors` in the `detect_objects` function to adjust the detection sensitivity.

### Contact:

For any questions or feedback, please feel free to open an issue on this repository.
