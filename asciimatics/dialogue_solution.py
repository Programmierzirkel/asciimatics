from asciimatics.screen import Screen, ManagedScreen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars, Print
from asciimatics.renderers import FigletText, Rainbow




@ManagedScreen
def demo(screen=None, name ="", fav_colour = 7):

    x=Stars(screen, (screen.width + screen.height) // 2)

    effects = [


        Print(screen,
             FigletText("{}".format(str("Hello"))), screen.height // 2 - 7, colour = fav_colour),

        Print(screen,
                    FigletText("{} !".format(str(name))), screen.height // 2, colour = fav_colour),

        x
        
    ]

    screen.play([Scene(effects, 500)])

#Die Funktion stellt das erste Argument in der Farbe dar, die als zweites Argument angegeben wird.
#BLACK = 0
#RED = 1
#GREEN = 2
#YELLOW = 3
#BLUE = 4
#MAGENTA = 5
#CYAN = 6
#WHITE = 7
def output(output1, output2):

    demo(screen=None, name = output1, fav_colour = output2)







name = input("What is your name?")
colour_name = input("What is your favorite colour?" + 
"""
type: "black", "red", "green", "yellow", "blue", "magenta", "cyan" or "white"!

""")


colour_dict=	{
  "black": 0,
  "red": 1,
  "green": 2,
  "yellow": 3,
  "blue": 4,
  "magenta": 5,
  "cyan": 6,
  "white":7 
}


output(name, colour_dict[colour_name])
