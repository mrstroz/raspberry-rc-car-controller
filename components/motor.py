class Motor:
    def __init__(self, ena, input1, input2):
        self.ena = ena
        self.input1 = input1
        self.input2 = input2
        # GPIO.setup(self.pwm,GPIO.OUT)
        # GPIO.setup(self.input1,GPIO.OUT)
        # GPIO.setup(self.input2,GPIO.OUT)
        # self.pwm = GPIO.PWM(self.ena,100)
        # self.pwm.start(0)

    def forward(self, x):
        print('Move Forward: ' + x)
        # GPIO.output(self.input1, GPIO.LOW)
        # GPIO.output(self.input2, GPIO.HIGH)
        # self.pwm.ChangeDutyCycle(x)

    def backward(self, x):
        print('Move Backward: ' + x)
        # GPIO.output(self.input1, GPIO.HIGH)
        # GPIO.output(self.input2, GPIO.LOW)
        # self.pwm.ChangeDutyCycle(x)
