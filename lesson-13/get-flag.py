#!/usr/bin/env ./../bin/python3
import csv
import hashlib
import http.server
import os
import random
import socketserver
import threading
import time
import urllib.parse
import webbrowser

web_dir = os.path.join(os.path.dirname(__file__), 'web')
os.chdir(web_dir)

# Load the users and MD5 passwords from the CSV file
user_passwords = {}
user_file = open('./users.csv')
csv_data = csv.reader(user_file)
next(csv_data) # skip the first row
for row in csv_data:
    user_passwords[row[0]] = row[1]


class BankHTTP(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        try:
            # Get the username and password values given to us
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            login_info = urllib.parse.parse_qs(post_data.decode())

            username = login_info['username'][0]
            password = login_info['password'][0]

            # Check the user exists
            if username not in user_passwords:
                raise Exception('Invalid username')

            # Check the password is correct
            md5_password = hashlib.md5(password.encode()).hexdigest()
            if user_passwords[username] != md5_password:
                raise Exception('Invalid password')

            # Return the flag
            flag_file = open('../flag.txt')
            flag = flag_file.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes(flag, 'utf8'))

        except Exception as e:
            # Show the error
            self.send_response(301)
            error = urllib.parse.quote(str(e))
            self.send_header('Location','/index.html?error=%s' % error)
            self.end_headers()


# Start the bank web server
port = random.randint(8000, 9000)
print('Starting bank server on port %d' % port)
bank_server = socketserver.TCPServer(('', port), BankHTTP)
threading.Thread(target=bank_server.serve_forever).start()


# Open the web browser
def open_browser():
    time.sleep(3)
    webbrowser.open_new('http://localhost:%d/index.html' % port)
threading.Thread(target=open_browser).start()
