from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def __init__(self):
        super().__init__()
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
