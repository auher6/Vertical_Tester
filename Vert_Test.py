from flask import Flask, request, jsonify
import cv2
import numpy as np
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video file uploaded'}), 400
    
    file = request.files['video']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Process the video to calculate jump height
    jump_height = process_video(filepath)

    return jsonify({'jump_height': jump_height})

def process_video(filepath):
    cap = cv2.VideoCapture(filepath)
    if not cap.isOpened():
        return "Error opening video"

    # Placeholder: Add actual processing logic (e.g., track feet position)
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1  # Just counting frames for now

    cap.release()
    return round(frame_count / 30, 2)  # Fake jump height based on frame count

if __name__ == '__main__':
    app.run(debug=True)