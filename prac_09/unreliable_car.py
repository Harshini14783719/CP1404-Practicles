import random
from car import Car


class UnreliableCar(Car):
    def __init__(self, name="", fuel=0, reliability=0.0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0  # car doesnt move due to unreliability
