import cv2
import requests
import numpy as np
from io import BytesIO
import threading
import time

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN'
# Replace 'YOUR_CHAT_ID' with your actual chat ID
CHAT_ID = 'YOUR_CHAT_ID'

# Function to get updates from Telegram
def get_updates(offset):
    response = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset={offset}").json()
    return response['result']

# Function to send a message to Telegram
def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    requests.post(url, json=params)

# Function to send a message and image on Telegram
def send_msg_with_image(text, image):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    _, img_encoded = cv2.imencode('.jpg', image)
    files = {'photo': ('image.jpg', img_encoded.tostring())}
    data = {'chat_id': CHAT_ID, 'caption': text}
    response = requests.post(url, files=files, data=data)
    print(response.json())

# Load the face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect faces in an image and send a message with the detected face image
def detect_faces_and_send_message(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    if len(faces) > 0:
        send_msg_with_image("Face detected!", frame)

# Function to handle incoming messages
def handle_messages():
    last_update_id = 0
    while True:
        updates = get_updates(last_update_id + 1)
        for update in updates:
            last_update_id = update['update_id']
            if 'message' in update and 'text' in update['message']:
                chat_id = update['message']['chat']['id']
                message_text = update['message']['text']
                print(f"Received message from {chat_id}: {message_text}")
                if message_text == 'img':
                    # Capture current frame
                    ret, frame = cap.read()
                    if ret:
                        send_msg_with_image("Current frame", frame)
                    else:
                        send_message(chat_id, "Failed to capture frame")
        time.sleep(1)

# Start a separate thread to handle incoming messages
message_thread = threading.Thread(target=handle_messages)
message_thread.start()

# Function to continuously capture frames and perform face detection
def capture_and_detect():
    while True:
        ret, frame = cap.read()
        if ret:
            detect_faces_and_send_message(frame)
            cv2.imshow('Face Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

# Start the video capture
cap = cv2.VideoCapture(0) 

# Start a separate thread for frame capture and face detection
capture_thread = threading.Thread(target=capture_and_detect)
capture_thread.start()

# Wait for the threads to finish
capture_thread.join()

cap.release()
cv2.destroyAllWindows()
