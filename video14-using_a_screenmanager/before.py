
from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout

class FirstScreen(BoxLayout):
    pass

class SecondScreen(BoxLayout):
    pass

class ColourScreen(BoxLayout):
    colour = ListProperty([1, 0, 0, 1])

root_widget = Builder.load_string('''
#:import random random.random

BoxLayout:
    orientation: 'vertical'
    FirstScreen:
    SecondScreen:
    ColourScreen:

<FirstScreen>:
    orientation: 'vertical'
    Label:
        text: 'first screen!'
        font_size: 30
    Image:
        source: 'colours.png'
        allow_stretch: True
        keep_ratio: False
    BoxLayout:
        Button:
            text: 'goto second screen'
            font_size: 30
        Button:
            text: 'get random colour screen'
            font_size: 30

<SecondScreen>:
    orientation: 'vertical'
    Label:
        text: 'second screen!'
        font_size: 30
    Image:
        source: 'colours2.png'
        allow_stretch: True
        keep_ratio: False
    BoxLayout:
        Button:
            text: 'goto first screen'
            font_size: 30
        Button:
            text: 'get random colour screen'
            font_size: 30

<ColourScreen>:
    orientation: 'vertical'
    colour: random(), random(), random(), 1
    Label:
        text: 'colour {:.2},{:.2},{:.2} screen'.format(*root.colour[:3])
        font_size: 30
    Widget:
        canvas:
            Color:
                rgba: root.colour
            Ellipse:
                pos: self.pos
                size: self.size
    BoxLayout:
        Button:
            text: 'goto first screen'
            font_size: 30
        Button:
            text: 'get random colour screen'
            font_size: 30
''')

runTouchApp(root_widget)
