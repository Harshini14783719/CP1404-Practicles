from unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar drive method over multiple iterations to confirm reliability behavior."""
    reliable_car = UnreliableCar("Reliable", fuel=1000, reliability=90)
    unreliable_car = UnreliableCar("Unreliable", fuel=1000, reliability=10)

    reliable_successes = 0
    unreliable_successes = 0
