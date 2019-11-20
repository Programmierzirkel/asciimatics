from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars, Mirage, Snow
from asciimatics.renderers import FigletText, Fire, SpeechBubble
from time import sleep

def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("P Y T H O N", font='big'),
            screen.height // 2 - 8),
        Cycle(
            screen,
            Fire(screen.height, screen.width,'O', 0.5, 50, 5),
            screen.height // 2 + 3),
            Snow(screen),

        Mirage(screen, FigletText("R O C K S ! ! !"), screen.height // 2 + 3, 2)

       
            
          
        
    ]
    screen.play([Scene(effects, 500)])
    
Screen.wrapper(demo)