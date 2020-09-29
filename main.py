import time
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/sleep')
def sleep():
    time.sleep(3)
    return "Sleep 3 sec.."

if __name__ == '__main__':
    app.run(
        host = app.config.get("HOST", "127.0.0.1"),
        port = app.config.get("PORT", 5000)
    )