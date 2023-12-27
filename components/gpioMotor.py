import RPi.GPIO as GPIO

from components.motor import Motor


class GpioMotor(Motor):
    def __init__(self, ena, input1, input2, speed=0):
        super().__init__(ena, input1, input2, speed)
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.ena, GPIO.OUT)
        GPIO.setup(self.input1, GPIO.OUT)
        GPIO.setup(self.input2, GPIO.OUT)
        self.pwm = GPIO.PWM(self.ena, 100)
        self.pwm.start(self.speed)

    def forward(self):
        super().forward()
        GPIO.output(self.input1, GPIO.LOW)
        GPIO.output(self.input2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(abs(self.speed))

    def backward(self):
        super().backward()
        GPIO.output(self.input1, GPIO.HIGH)
        GPIO.output(self.input2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(abs(self.speed))
