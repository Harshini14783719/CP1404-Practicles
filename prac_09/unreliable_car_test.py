from unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar drive method over multiple iterations to confirm reliability behavior."""
    reliable_car = UnreliableCar("Reliable", fuel=1000, reliability=90)
    unreliable_car = UnreliableCar("Unreliable", fuel=1000, reliability=10)

    reliable_successes = 0
    unreliable_successes = 0
    tests = 100

    for i in range(tests):
        if reliable_car.drive(1) > 0:
            reliable_successes += 1
        if unreliable_car.drive(1) > 0:
            unreliable_successes += 1

    if reliable_successes > 70:
        print("reliable car passed test")
    else:
        print("Reliable car failed the test")

    if unreliable_successes < 30:
        print("Unreliable car passed the test.")
    else:
        print("Unreliable car failed the test.")

main()