# Keylogger and Screenshot Capture Script

## **Description**

This Python script logs keystrokes and captures screenshots at regular intervals, sending the data to a specified remote server. It is intended for use in educational or controlled environments where explicit permission has been granted to monitor and capture user activity. The script demonstrates how sensitive information can be gathered, highlighting the importance of security measures.

## **Features**

- **Keystroke Logging:** Logs all keyboard inputs, including special keys like Enter, Tab, and Space.
- **Screenshot Capture:** Captures the entire screen and encodes the image in base64 format for easy transmission.
- **Data Transmission:** Sends keystrokes and screenshots to a remote server via an HTTP POST request.
- **Configurable Timing:** Allows setting the time interval for how often data is sent to the server.

## **Requirements**

- Python 3.x
- `pynput` library
- `requests` library
- `Pillow` (PIL) library

You can install the required libraries using pip:

```bash
pip install pynput requests pillow
