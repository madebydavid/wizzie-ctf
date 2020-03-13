#!/usr/bin/env ./../bin/python3
import socketserver
import webbrowser
import threading
import time
import csv

from http.server import SimpleHTTPRequestHandler

class BankHTTP(SimpleHTTPRequestHandler):
    def do_POST(self):
        login_info = self.rfile.read(int(self.headers['Content-Length']))
        print(login_info)

print("Starting bank_server")
bank_server = socketserver.TCPServer(('', 8000), BankHTTP)
threading.Thread(target=bank_server.serve_forever).start()

def open_browser():
    time.sleep(3)
    webbrowser.open_new('http://localhost:8000/index.html')

threading.Thread(target=open_browser).start()
