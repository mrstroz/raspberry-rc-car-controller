import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_socketio import SocketIO

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('send_controller_data')
def handle_stick_data(json):
    print(json['x'] + json['y'])


if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
