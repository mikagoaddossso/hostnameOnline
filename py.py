from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/')
def get_hostname():
    hostname = socket.gethostname()
    return f"<h1>Hostname : {hostname}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)