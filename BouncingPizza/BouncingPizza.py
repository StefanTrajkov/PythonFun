from games import *

import random

screen_width = 710
screen_height = 786

class ScreenS(Screen):
    def __init__(self, width, height):
        self.init_screen(width, height)

    def tick(self):
        for object in self.all_objects():
            object.moved()

class Pizza(Sprite):
    def __init__(self, screen, x, y, image, dx, dy):
        self.init_sprite(screen=screen, x=x, y=y, image=image)
        self.dx = dx
        self.dy = dy

    def moved(self):
        x, y = self.pos()
        if x > screen_width-50 or x < 10:
            self.dx = -self.dx
            self.dy = self.dy
        if y > screen_height-50 or y < 10:
            self.dx = self.dx
            self.dy = -self.dy
        self.move_by(self.dx,self.dy)


screen = ScreenS(screen_width, screen_height)
wall_image = load_image("brickwall.png", False)
screen.set_background(wall_image)
pizza_image = load_image("pizza.png")
Pizza(screen, x=screen_width / 2, y=screen_height / 2, image=pizza_image, dx=1, dy=1)
screen.mainloop(120)
