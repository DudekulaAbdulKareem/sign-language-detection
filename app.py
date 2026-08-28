from ultralytics import YOLO
import cv2
import numpy as np
from flask import Flask, Response, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # Folder to store uploaded images
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load the YOLO model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "best.pt")
model = YOLO(MODEL_PATH)
# Helper function to get frames from webcam and process with YOLO
def generate_frames():
    cap = cv2.VideoCapture(0)  # Open webcam

    while cap.isOpened():
        ret, frame = cap.read()  # Capture frame-by-frame
        if not ret:
            break

        # Run the YOLO model on the frame
        results = model.predict(source=frame, conf=0.3)

        # Draw bounding boxes and labels on the frame
        annotated_frame = results[0].plot()  # YOLO's plot function to add bounding boxes

        # Encode the frame in JPEG format
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame = buffer.tobytes()

        # Yield the frame in byte format for HTML rendering
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

# Route to serve the video stream
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Route for image upload and prediction
@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Save the uploaded file
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Run YOLO model on the uploaded image
            results = model.predict(source=filepath, conf=0.3)
            annotated_image = results[0].plot()  # Annotate the image

            # Save the annotated image for display
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.jpg')
            cv2.imwrite(output_path, annotated_image)

            return redirect(url_for('display_image'))

    return render_template('upload.html')

# Route to display the annotated image after upload
@app.route('/display')
def display_image():
    return render_template('display.html')

# Default route to render the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
