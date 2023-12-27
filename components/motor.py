class Motor:
    def __init__(self, ena, input1, input2, speed=0):
        self.ena = ena
        self.input1 = input1
        self.input2 = input2
        self.speed = speed

    def forward(self):
        print('Move Forward: ' + str(self.speed))

    def backward(self):
        print('Move Backward: ' + str(self.speed))

    def set_speed(self, speed):
        self.speed = speed

    def run(self):
        if self.speed > 0:
            self.forward()
        else:
            self.backward()
