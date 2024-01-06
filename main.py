import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_socketio import SocketIO
# from components.motor import Motor
from components.gpioMotor import GpioMotor

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app)

# motor_left = Motor(2, 3, 4)
# motor_right = Motor(14, 15, 18)

motor_left = GpioMotor(2, 3, 4)
motor_right = GpioMotor(14, 15, 18)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('send_start')
def handle_reset():
    global motor_left, motor_right

    while True:
        motor_left.run()
        motor_right.run()


@socketio.on('send_controller_data')
def handle_stick_data(json):
    global motor_left, motor_right

    speed_left = int(json['left'])
    speed_right = int(json['right'])

    motor_left.set_speed(speed_left)
    motor_right.set_speed(speed_right)


@socketio.on('send_reset')
def handle_reset():
    global motor_left, motor_right

    motor_left.set_speed(0)
    motor_right.set_speed(0)


if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
