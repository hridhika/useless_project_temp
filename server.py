from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from fer import FER
import base64
import numpy as np
import cv2
import random
import os

app = Flask(__name__)
CORS(app)

# Set the video directory to the current folder
VIDEO_DIR = '.'

# Define a dictionary for local video files based on emotions
videos = {
    "happy": [
        "ishtamalla.mp4",
        "ahankaram.mp4"
    ],
    "sad": [
        "kozhikalmp4.mp4",
        "prajodanammp4.mp4"
    ],
    "angry": [
        "thettukal.mp4",
        "thottu.mp4"
    ],
    "surprise": [
        "thottu.mp4",
        "help.mp4"
    ],
    "neutral": [
        "jeevitham.mp4",
        "prateekshamp4.mp4"
    ],
}

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/analyze-expression', methods=['POST'])
def analyze_expression():
    data = request.json

    if not data or 'image' not in data:
        return jsonify({'error': 'No image data provided.'}), 400

    try:
        # Decode the base64 image
        image_data = data['image'].split(",")[1]
        image = base64.b64decode(image_data)
        np_arr = np.frombuffer(image, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Initialize FER detector
        detector = FER()
        result = detector.detect_emotions(img)

        # Determine the detected emotion
        if result:
            dominant_emotion = result[0]['emotions']
            emotion = max(dominant_emotion, key=dominant_emotion.get)
        else:
            emotion = "unknown"

        # Select a random video based on detected emotion
        video_file = random.choice(videos.get(emotion, []))

        # Generate the video URL or show a default message if no video found
        if video_file:
            video_url = f'{video_file}'
        else:
            video_url = None

        return jsonify({
            'video_url': video_url,
            'description': f'You seem {emotion}!' if video_url else 'No video found for the detected expression.'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/videos/<path:filename>')
def serve_video(filename):
    return send_from_directory(VIDEO_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
