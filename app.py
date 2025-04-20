from flask import Flask, render_template, Response, jsonify, request
import cv2
import numpy as np
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__)

# Configuration de la caméra depuis les variables d'environnement
CAMERA_IP = os.getenv('CAMERA_IP')
CAMERA_USERNAME = os.getenv('CAMERA_USERNAME')
CAMERA_PASSWORD = os.getenv('CAMERA_PASSWORD')
CAMERA_PORT = os.getenv('CAMERA_PORT')

RTSP_URL = f"rtsp://{CAMERA_USERNAME}:{CAMERA_PASSWORD}@{CAMERA_IP}:{CAMERA_PORT}/stream1"
rotation_angle = 90

def get_frame():
    cap = cv2.VideoCapture(RTSP_URL)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Appliquer la rotation
        if rotation_angle != 0:
            (h, w) = frame.shape[:2]
            center = (w // 2, h // 2)
            M = cv2.getRotationMatrix2D(center, rotation_angle, 1.0)
            frame = cv2.warpAffine(frame, M, (w, h))
        
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(get_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/rotate', methods=['POST'])
def rotate():
    global rotation_angle
    data = request.get_json()
    angle = int(data.get('angle', 0))
    rotation_angle = angle
    return jsonify({'status': 'success', 'angle': angle})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8765, debug=True) 
