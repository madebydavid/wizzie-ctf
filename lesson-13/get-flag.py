#!/usr/bin/env ./../bin/python3
import socketserver
import webbrowser
import threading
import time
import csv

from http.server import SimpleHTTPRequestHandler
from urllib.parse import parse_qs
from random import randint

class BankHTTP(SimpleHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            login_info = parse_qs(post_data.decode())
            print(login_info_raw.decode())
            print(login_info)
            print(login_info['username'])
        except:
            pass

# Pick a random port number
port = randint(8000, 9000)

# Start the bank HTTP server
print('Starting bank_server on port %d' % port)
bank_server = socketserver.TCPServer(('', port), BankHTTP)
threading.Thread(target=bank_server.serve_forever).start()

# Open the web browser
def open_browser():
    time.sleep(3)
    webbrowser.open_new('http://localhost:%d/index.html' % port)

threading.Thread(target=open_browser).start()
