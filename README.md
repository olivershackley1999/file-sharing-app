# File Sharing App

Lightweight tool to access computer files from a phone without cloud services or account signup.

## What it does

- Serves files from any directory via HTTP server on a user-defined port
- Supports local network access (fast, private) or remote access via Ngrok tunnel (anywhere)
- Generates QR code for instant mobile device access
- No account creation or cloud storage required

## How it works

**Four-step flow:**

1. **Configure**: Specify the directory path and port number
2. **Choose Access Mode**: Local network (faster) or Ngrok tunnel (remote access from anywhere)
3. **Server Starts**: HTTP server begins serving files from the specified directory
4. **Connect**: Scan the QR code saved to your desktop or paste the URL into any browser

## Tech Stack

- Python 3.13
- http.server (built-in Python HTTP server)
- pyngrok (Ngrok tunnel for remote access)
- pyqrcode (QR code generation)

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/olivershackley1999/file-sharing-app.git
   cd file-sharing-app
   ```

2. Install dependencies
   ```bash
   pip install pyqrcode pypng pyngrok
   ```

3. Run the script
   ```bash
   python file_share.py
   ```

4. Follow the prompts to configure directory, port, and access mode

## Usage

```
FILE SHARING APPLICATION
------------------------
Directory Path: /Users/me/Documents
Port Number: 8080

COMPUTER: Files now being served from: https://abc123.ngrok.io
MOBILE: Scan the QR code on your desktop to access via phone.
Press Ctrl+C to stop the server...
```

## Project Motivation

Built as a quick way to transfer files between devices without relying on cloud services, email attachments, or third-party apps.
