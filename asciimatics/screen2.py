from asciimatics.screen import ManagedScreen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from time import sleep


@ManagedScreen
def demo(screen=None):
    screen.print_at('Hello world!', 0, 0, 2, 4)
   


    # Draw a diagonal line from the top-left of the screen.
    screen.move(0, 0)
    screen.draw(10, 10)

    # Clear the line
    #screen.move(0, 0)
    #screen.draw(10, 10, char='*')
    screen.refresh()
    sleep(10)
    
demo()
