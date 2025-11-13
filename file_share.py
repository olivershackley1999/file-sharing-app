import socket
import os
import time
import sys
import pyqrcode
import png
from pyngrok import ngrok
import subprocess

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return str(ip_address)
    except:
        return "Failed"
    
def get_port():

    while True:
        try:
            port = input("Port Number: ")

            if port == "":
                port = 8010
                return port
            else:
                port = int(port)

        
            if port < 0:
                print("Invalid Port Number. Try again.")
                continue
            elif port >= 0 and port <= 1023:
                print("Port must be above 1,023 and below 65,535")
                continue
            elif port > 65535:
                print("Ports above 65,535 do not exist. Try again.")
                continue
            elif port > 1023 and port <= 65535:
                return port

        except ValueError:
            print("Invalid Port Number. Try again.")
            continue
        except TypeError:
            print("Invalid Port Number. Try again.")
            continue
        except KeyboardInterrupt:
            print('Exiting...')
            sys.exit()

def get_directory():
    try:
        while True:

            path = input("Directory Path: ")

            if os.path.isdir(path):
                print(f"You chose: {path}")
                print("Directory validated.")
                return path
            elif path == "":
                path = os.path.expanduser("~")
                print(f"You chose: {path}")
                print("Path validated.")
                return path
            else:
                print("This path is NOT a directory")
                continue
    except KeyboardInterrupt:
        print()
        print("Exiting...")
        sys.exit()

def generate_qr_code(ip, port):
    home_dir = os.path.expanduser("~")
    desktop = os.path.join(home_dir, "Desktop")
    os.chdir(desktop)
    url = "http://" + str(ip) + ":" + str(port)
    qr = pyqrcode.create(url)
    qr.png("server_qr.png", scale=8)
    print("QR code saved as server_qr.png")

def start_server(path, port, ip):
        os.chdir(path)
        server_process = subprocess.Popen(['python', '-m', 'http.server', str(port)])
        url_computer = ngrok.connect(port)
        
        print(f"COMPUTER: Files now being served from: {url_computer}")
        print("MOBILE: Scan the QR code on your desktop to access via phone.")
        try:
            print("Press Ctrl+C to stop the server...")
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print('Exiting...')
            print(f"Killing process: {server_process.pid}")
            server_process.kill()
            print("Process killed.")
            server_process.wait()
            print("Ngrok tunnel closed.")

def main():
    ip = get_local_ip()
    path = get_directory()
    port = get_port()
    generate_qr_code(ip, port)
    start_server(path, port, ip)

welcome = "FILE SHARING APPLICATION"
length = len(welcome)
print(welcome)
time.sleep(2)
print("-" * length)
time.sleep(1)

if __name__ == "__main__":
    main()
        
    
