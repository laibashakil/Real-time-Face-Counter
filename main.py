import cv2
import streamlit as st
import numpy as np
import base64
import uuid

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_objects(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    return image, len(faces)

def resize_frame(frame, width=None, height=None):
    if width is not None and height is not None:
        return cv2.resize(frame, (width, height))
    elif width is not None:
        aspect_ratio = frame.shape[1] / frame.shape[0]
        return cv2.resize(frame, (width, int(width / aspect_ratio)))
    elif height is not None:
        aspect_ratio = frame.shape[1] / frame.shape[0]
        return cv2.resize(frame, (int(height * aspect_ratio), height))
    else:
        return frame

def main():
    st.title("Real-time Face Detection App")
    
    # HTML template to display the webcam feed
    HTML_TEMPLATE = """
    <img src="data:image/jpeg;base64,{}" style="width:100%;">
    """
    
    # Streamlit placeholder for displaying the webcam feed
    placeholder = st.empty()
    
    cap = cv2.VideoCapture(0)
    num_faces = 0
    
    # Boolean variable to control the loop
    running = True
    
    while running:
        ret, frame = cap.read()
        if not ret:
            st.write("Error: Unable to capture frame from webcam.")
            break
        
        # Resize the frame to fit the Streamlit app window
        resized_frame = resize_frame(frame, width=640)
        
        detected_frame, curr_num_faces = detect_objects(resized_frame)
        num_faces = curr_num_faces
        
        cv2.putText(detected_frame, f'Number of Faces: {num_faces}', (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
        
        # Convert the frame to JPEG format
        _, frame_buffer = cv2.imencode(".jpg", detected_frame)
        frame_bytes = frame_buffer.tobytes()
        frame_base64 = base64.b64encode(frame_bytes).decode()
        
        # Update the webcam feed in the HTML template
        placeholder.markdown(HTML_TEMPLATE.format(frame_base64), unsafe_allow_html=True)
    
    cap.release()
    cv2.destroyAllWindows()
    
    # Display final count of detected faces
    st.markdown("### Live Feed Ended")
    st.write(f"Final count of detected faces: {num_faces}")

if __name__ == "__main__":
    main()