from asciimatics.screen import Screen, ManagedScreen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars, Print
from asciimatics.renderers import FigletText, Rainbow

import time 




@ManagedScreen
def demo(screen=None, output1="", output2="", duration=50):



    effects = [


        Print(screen,
             Rainbow(screen, FigletText("{}".format(str(output1)))), screen.height // 2 - 7),

        Print(screen,
             Rainbow(screen, FigletText("{}".format(str(output2)))), screen.height // 2),

        Stars(screen, (screen.width + screen.height) // 2)
        
    ]

    screen.play([Scene(effects, duration)], repeat=False)
 

def output(output1, output2):

    demo(screen=None, output1 = output1, output2 = output2)




x = "Hello" 
y = "W o r l d !"


for i in range(0,9):

    if i % 2 == 0:

        output(x, y)
    else:

        output("Goodbye", "World!")