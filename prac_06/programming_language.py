class ProgrammingLanguage:

    def __init__(self, name="", typing="", is_reflection=False, year=0):
        """Initialize the attributes"""
        self.name = name
        self.typing = typing
        self.is_reflection = is_reflection
        self.year = year

    def is_dynamic(self):
        """It will return True when typing is dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        """convert object as a string for output"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.is_reflection}, First appeared in {self.year}"
