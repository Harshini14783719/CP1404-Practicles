class ProgramingLanguage:

    def __init__(self, name="", typing="", is_reflection=False, year=0):
        """Initialize the attributes"""
        self.name = name
        self.typing = typing
        self.is_reflection = is_reflection
        self.year = year

    def is_dynamic(self):
        """It will return True when typing is dynamic"""
        return self.typing == "Dynamic"