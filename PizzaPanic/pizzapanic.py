import random
from livewires import games, colour

from chef import *
from pan import *

screen_width = 710
screen_height = 786
the_screen = games.Screen(screen_width, screen_height)



if __name__ == '__main__':
    my_screen = the_screen
    my_screen.mouse_visible(False)
    wall_image = games.load_image("Images/brickwall.png", transparent=False)
    my_screen.set_background(wall_image)

    Chef(screen=my_screen, x=screen_width/2, speed=1, odds_change=250)
    Skillet(screen=my_screen, x=screen_width/2, y=735)
    my_screen.mainloop()



