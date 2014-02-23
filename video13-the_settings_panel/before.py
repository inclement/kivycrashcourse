
from kivy.app import App
from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout


Builder.load_string('''
<Interface>:
    orientation: 'vertical'
    Button:
        text: 'open the settings!'
        font_size: 150
''')

class Interface(BoxLayout):
    pass

class SettingsApp(App):
    def build(self):
        return Interface()

SettingsApp().run()
