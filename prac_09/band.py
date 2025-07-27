class Band:
    def __init__(self, name=""):
        """Initialize a Band with a name and empty list of musicians."""
        self.name = name
        self.members = []

    def add(self, musician):
        """Add a musician to the band."""
        self.members.append(musician)

    def __str__(self):
        """Return a string representation of the Band and its members."""
        return f"{self.name} ({', '.join(str(member) for member in self.members)})"

    def play(self):
        return