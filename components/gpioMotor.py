import RPi.GPIO as GPIO

from components.motor import Motor


class GpioMotor(Motor):
    """
    GpioMotor class, inheriting from Motor, is designed to interface with a motor
    using Raspberry Pi's GPIO pins. This class initializes the motor, sets up the GPIO pins,
    and controls the motor's forward and backward movement.

    Attributes are inherited from the Motor class.
    """

    def __init__(self, ena, input1, input2, speed=0):
        """
        Initialize the GpioMotor instance.

        Args:
            ena (int): PWM control pin for the motor.
            input1 (int): Input pin 1 for controlling motor direction.
            input2 (int): Input pin 2 for controlling motor direction.
            speed (int, optional): Initial speed of the motor. Defaults to 0.
        """
        super().__init__(ena, input1, input2, speed)  # Call the constructor of the parent Motor class

        # Set up the GPIO mode and warnings
        GPIO.setmode(GPIO.BCM)  # Use Broadcom SOC channel numbers
        GPIO.setwarnings(False)  # Disable GPIO warnings

        # Set up the GPIO pins for output
        GPIO.setup(self.ena, GPIO.OUT)
        GPIO.setup(self.input1, GPIO.OUT)
        GPIO.setup(self.input2, GPIO.OUT)

        # Initialize PWM on the enable pin and start it at the set speed
        self.pwm = GPIO.PWM(self.ena, 100)  # PWM frequency set to 100 Hz
        self.pwm.start(self.speed)

    def forward(self):
        """
        Controls the motor to move forward. Overrides the forward method
        from the parent Motor class.
        """
        super().forward()  # Call the forward method from the parent class
        # Set the GPIO pins to move the motor forward
        GPIO.output(self.input1, GPIO.LOW)
        GPIO.output(self.input2, GPIO.HIGH)
        # Change the duty cycle of the PWM to the absolute value of speed
        self.pwm.ChangeDutyCycle(abs(self.speed))

    def backward(self):
        """
        Controls the motor to move backward. Overrides the backward method
        from the parent Motor class.
        """
        super().backward()  # Call the backward method from the parent class
        # Set the GPIO pins to move the motor backward
        GPIO.output(self.input1, GPIO.HIGH)
        GPIO.output(self.input2, GPIO.LOW)
        # Change the duty cycle of the PWM to the absolute value of speed
        self.pwm.ChangeDutyCycle(abs(self.speed))
