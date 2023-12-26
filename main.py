import os
import RPi.GPIO as GPIO

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_socketio import SocketIO

from components.motor import Motor

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

speed_left = 50
speed_right = 50
motor_left = Motor(2, 3, 4)
motor_right = Motor(14, 15, 18)

while True:
    if speed_left > 0:
        motor_left.forward(abs(speed_left))
    else:
        motor_left.backward(abs(speed_left))

    if speed_right > 0:
        motor_right.forward(abs(speed_right))
    else:
        motor_right.backward(abs(speed_right))

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('send_controller_data')
def handle_stick_data(json):
    global speed_left, speed_right
    
    speed_left = int(json['left'])
    speed_right = int(json['left'])

    

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
