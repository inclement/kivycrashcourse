
from kivy.base import runTouchApp
from kivy.lang import Builder

from kivy.uix.widget import Widget

from kivy.clock import Clock
from kivy.animation import Animation

from kivy.properties import ListProperty

from kivy.core.window import Window

from random import random

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
    velocity = ListProperty([10, 15])

    def __init__(self, **kwargs):
        super(ClockRect, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1/60.)

    def update(self, *args):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        if self.x < 0 or (self.x + self.width) > Window.width:
            self.velocity[0] *= -1
        if self.y < 0 or (self.y + self.height) > Window.height:
            self.velocity[1] *= -1


class AnimRect(Widget):
    def anim_to_random_pos(self):
        Animation.cancel_all(self)
        random_x = random() * (Window.width - self.width)
        random_y = random() * (Window.height - self.height)

        anim = Animation(x=random_x, y=random_y,
                         duration=4,
                         t='out_elastic')
        anim.start(self)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.anim_to_random_pos()

runTouchApp(Root())
