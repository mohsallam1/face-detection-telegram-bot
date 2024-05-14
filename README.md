# Face Detection Telegram Bot

This Python script implements a Telegram bot that captures video frames from a webcam, detects faces using OpenCV, and sends images with detected faces to a specified Telegram chat. The bot provides real-time face detection functionality and allows users to interact with it through Telegram messages.

## Functionality

### 1. `get_updates(offset)`

This function sends a request to the Telegram Bot API to retrieve updates from the chat. It takes an offset parameter to fetch only new updates. The function returns a list of updates, which include incoming messages, chat actions, and other events.

### 2. `send_message(chat_id, text)`

The `send_message` function sends a text message to a specified chat or user using the Telegram Bot API. It requires the chat_id of the recipient and the text message to be sent.

### 3. `send_msg_with_image(text, image)`

This function sends a message along with an image to a specified chat or user using the Telegram Bot API. It encodes the image in JPEG format and sends it as a file attachment along with the provided text message.

### 4. `detect_faces_and_send_message(frame)`

The `detect_faces_and_send_message` function takes a video frame captured from the webcam as input. It uses OpenCV's face detection functionality to detect faces in the frame. If one or more faces are detected, it calls the `send_msg_with_image` function to send the frame with the detected faces to the Telegram chat.

### 5. `handle_messages()`

This function continuously checks for incoming messages from the Telegram chat. It retrieves updates using the `get_updates` function and processes each message accordingly. If a message with the text "img" is received, it captures a video frame from the webcam and sends it to the chat using the `send_msg_with_image` function.

### 6. `capture_and_detect()`

The `capture_and_detect` function continuously captures video frames from the webcam using OpenCV. For each frame, it calls the `detect_faces_and_send_message` function to perform face detection and send the frame with detected faces to the Telegram chat. It also displays the video feed with face detection visualization in a window using OpenCV's `imshow` function.

## Usage

1. Replace the placeholder values for `BOT_TOKEN` and `CHAT_ID` with your actual bot token and chat ID.
2. Run the `script.py` script to start the Telegram bot.
3. Interact with the bot by sending messages to the specified chat. Use the "img" command to capture and send the current frame with.

## Dependencies

- Python 3.x
- OpenCV (cv2)
- requests


