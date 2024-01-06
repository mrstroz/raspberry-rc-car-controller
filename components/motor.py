class Motor:
    """
    The Motor class represents a motor with basic control capabilities.
    It can move forward, backward, set speed, and get the current speed.

    Attributes:
        ena (int): Enable pin for the motor.
        input1 (int): Input pin 1 for motor direction.
        input2 (int): Input pin 2 for motor direction.
        speed (int): Current speed of the motor (default is 0).
    """

    def __init__(self, ena, input1, input2, speed=0):
        """
        Initialize the motor with the given parameters.

        Args:
            ena (int): Enable pin.
            input1 (int): Input pin 1.
            input2 (int): Input pin 2.
            speed (int, optional): Initial speed. Defaults to 0.
        """
        self.ena = ena
        self.input1 = input1
        self.input2 = input2
        self.speed = speed

    def forward(self):
        """Moves the motor forward at the current speed."""
        print('Move Forward: ' + str(self.speed))

    def backward(self):
        """Moves the motor backward at the current speed."""
        print('Move Backward: ' + str(self.speed))

    def get_speed(self):
        """Returns the current speed of the motor."""
        return self.speed

    def set_speed(self, speed):
        """
        Sets the motor's speed.

        Args:
            speed (int): The new speed of the motor.
        """
        self.speed = speed

    def run(self):
        """
        Runs the motor based on the current speed.
        Positive speed moves forward, non-positive moves backward.
        """
        if self.speed > 0:
            self.forward()
        else:
            self.backward()
