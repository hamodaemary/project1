from kivy.app import App
from kivy.uix.label import Label
class Kc(App):
    def build(self):
        return Label(text="hi")
Kc().run()