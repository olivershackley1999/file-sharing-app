# File Sharing Application

A fast, lightweight tool for anyone to access their computer files from a phone (no account signup or cloud needed!)

# Features

* Choose between local network access (speed/privacy) or remote access (anywhere)
* Serves files from HTTP Server on a user-defined port
* Uses an Ngrok forwarding URL for remote access
* Generates QR Code for mobile device access 

# Requirements

- Python 3.13.7

# Installation

1. Clone the repository
2. Install dependencies: "python3 -m pip install pyqrcode pypng pyngrok"

# Usage

1. Run the script: python3 file_share.py
2. Follow the prompts:
   - Enter the path you want to access files from.
   - Enter a port number (between 1023 and 65535).
   - Copy/paste the ngrok URL into your browser (immediately after "Ngrok Tunnel:") OR
   - Scan the QR Code saved to your desktop from your phone.
3. Access files from anywhere!

# How It Works

When you run the script, it gives you the option of accessing your files locally or remotely.

If localhost, it grabs the user's local IP Address, asks for the path, port number, and starts the HTTP Server on the selected port. 

If Ngrok, Ngrok creates a tunnel from the user's port to a forwarding URL served from Ngrok's cloud, enabling remote access from anywhere (albeit with a speed and security tradeoff).

In either case, a QR Code is generated containing either the local network URL or the ngrok URL and is saved to the user's desktop for quick access.

The full flow:

Specify path --> enter port --> choose Ngrok URL or localhost access --> HTTP Server starts --> QR Code saved to desktop --> paste URL into browser / scan QR Code on mobile --> files served! 


