from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """Kivy app for converting miles to kilometers."""
    output_km = StringProperty()

    def build(self):
        """Build the kivy app from the kv file."""
        self.title = 'Convert Miles to Kilometers'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle calculation (could be button press or other call)."""
        miles = self.convert_to_number(text)
        self.output_km = str(miles * MILES_TO_KM)

    def handle_increment(self, text, change):
        """Handle up/down button press."""
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    def convert_to_number(self, text):
        """Convert text to float."""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConverterApp().run()