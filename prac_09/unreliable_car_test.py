from car import Car


class UnreliableCar:
    def __init__(self, name="", fuel=0, reliability=0.0):
        super().__init__(name, fuel)
        self.reliability = reliability
