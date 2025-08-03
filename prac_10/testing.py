"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return ' '.join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # TODO: 2. write assert statements to show if Car sets the fuel correctly
    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    car = Car(fuel=10)
    assert car.fuel == 10, "Car does not set fuel correctly when a value is provided"

    default_car = Car()
    assert default_car.fuel == 0, "Car does not set default fuel correctly"

    def format_phrase(phrase):
        """
        Format a phrase as a sentence, starting with a capital and ending with a single full stop.
        >>> format_phrase("hello")
        'Hello.'
        >>> format_phrase("It is an ex parrot.")
        'It is an ex parrot.'
        >>> format_phrase("good morning")
        'Good morning.'
        """
        pass


run_tests()


doctest.testmod()












