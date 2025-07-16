CURRENT_YEAR = 2025
VINTAGE_YEAR = 50


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """converts object to string for output"""
        return f"{self.name} ({self.year}): ${self.cost}"

    def __lt__(self, other):
        """Allow sorting guitars by year (older = less)."""
        return self.year < other.year

    def get_age(self):
        """find age of guitar by deducting self.year from current year"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """find if guitar is vintage if it is more than 50 years"""
        return self.get_age() >= VINTAGE_YEAR
