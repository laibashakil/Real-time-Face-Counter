# Real-Time Face Counter
This Python application utilizes OpenCV to detect and count faces in real-time via your webcam.

**Features:**

-   Detects faces using the Haar Cascade classifier.
-   Draws bounding boxes around detected faces.
-   Displays the number of faces detected on the frame.

**Getting Started:**

1.  **Install Requirements:**  Ensure you have OpenCV installed (`pip install opencv-python`).
2.  **Run the App:**  Clone this repository and execute  `python main.py`.
3.  **Webcam Access:**  Grant permission to the app to access your webcam.
4.  **Face Detection:**  Point your webcam towards yourself for automatic face detection.

**How it Works:**

1.  The code loads the pre-trained Haar Cascade classifier for face detection.
2.  It captures video frames from your webcam.
3.  Each frame is converted to grayscale for optimal detection.
4.  The classifier identifies potential faces and returns bounding box coordinates.
5.  Bounding boxes are drawn around detected faces on the original frame.
6.  The number of detected faces is displayed on the frame.
7.  The processed frame is shown on your screen.

**Customization:**

-   You can experiment with different values for  `scaleFactor`  and  `minNeighbors`  in the  `detect_objects`  function to adjust the detection sensitivity.
-   Explore other Haar Cascade classifiers for detecting different objects by modifying the path in the  `face_cascade`  variable.

**Contribution:**

We welcome contributions to improve this project. Feel free to fork the repository and submit pull requests with enhancements or bug fixes.

**License:**

This project is licensed under the MIT License. See the LICENSE file for details.

**Additional Notes:**

-   This example uses a basic Haar Cascade classifier, which may not be perfect in all lighting conditions or scenarios.
-   For more advanced face detection, consider exploring deeper learning techniques.
