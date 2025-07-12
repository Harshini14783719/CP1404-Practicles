CURRENT_YEAR = 2025

class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """converts object to string for oitput"""
        return f"{self.name} ({self.year}): ${self.cost}"

    def get_age(self):
        """find age of guitar by deducting self.year from current year"""
        return CURRENT_YEAR - self.year
