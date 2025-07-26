from silver_service_taxi import SilverServiceTaxi


def main():
    """Test fare calculation for SilverServiceTaxi with fanciness factor."""
    taxi = SilverServiceTaxi("Hummer", 200, 2)
    taxi.start_fare()
    taxi.drive(18)
    fare = taxi.get_fare()
    print(f"fare calculated = {fare:.2f}")
    assert abs(fare - 48.78) < 0.01, f"Expected fare to be $48.78, but got ${fare:.2f}"
    print(taxi)


main()
