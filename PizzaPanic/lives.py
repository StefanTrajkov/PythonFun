import random
from livewires import games, colour
from livewires.games import Sprite

screen_width = 710
screen_height = 786


class Lives(Sprite):
    image = games.load_image("images/live.bmp")
    start_y = 20

    def __init__(self, screen, x):
        self.init_sprite(screen=screen, x=x, y=Lives.start_y, image=self.image)

    def destroy(self):
        self.destroy()


screen = games.Screen(screen_width, screen_height)
wallimg = games.load_image("images/brickwall.png", False)
screen.set_background(wallimg)

Lives(screen, 20)

screen.mainloop()

