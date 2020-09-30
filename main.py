import time
import json
import socket
from flask import Flask, request

app = Flask(__name__)

def get_host_ip(): 
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

@app.route('/')
def index():
    hostname = socket.gethostname()
    if request.environ.get('HTTP_X_FORWARDED_FOR') is not None:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.environ['REMOTE_ADDR']
    return json.dumps({
        "ClientIP": ip,
        "Host": hostname,
        "ServerIP": get_host_ip(),
        "Time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "Version": "latest"
    })


if __name__ == '__main__':
    app.run(
        host = app.config.get("HOST", "127.0.0.1"),
        port = app.config.get("PORT", 5000),
        debug = True
    )
