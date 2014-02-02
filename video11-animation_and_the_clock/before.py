
from kivy.base import runTouchApp
from kivy.lang import Builder

from kivy.uix.widget import Widget

from kivy.clock import Clock
from kivy.animation import Animation

Builder.load_string('''
<Root>:
    ClockRect:
        pos: 300, 300
    AnimRect:
        pos: 500, 300

<ClockRect>:
    canvas:
        Color:
            rgba: 1, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size

<AnimRect>:
    canvas:
        Color:
            rgba: 0, 1, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
''')

class Root(Widget):
    pass

class ClockRect(Widget):
    pass


class AnimRect(Widget):
    pass

runTouchApp(Root())
