from kivy.app import App
from kivy.uix.button import Label


class TestApp(App):
    def build(self):
        return Label()


TestApp().run()