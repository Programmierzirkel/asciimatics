from random import choice
from asciimatics.renderers import Plasma, Rainbow, FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.effects import Print
from asciimatics.exceptions import ResizeScreenError
import sys


def demo(screen):
    effects = [
                Print(screen,
                      Plasma(screen.height, screen.width, screen.colours),
                      0,
                      speed=3,
                      transparent=False),
            ]
    screen.play([Scene(effects, 500)])

Screen.wrapper(demo)        