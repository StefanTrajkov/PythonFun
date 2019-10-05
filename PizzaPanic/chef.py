import random
from livewires import games, colour
from pizza import *

screen_width = 710
screen_height = 786


class Chef(games.Sprite):
    image = games.load_image("Images/chef.png")
    y = 55

    def __init__(self, screen, x, speed, odds_change):
        self.init_sprite(screen=screen, x=x, y=Chef.y, dx=speed, dy=0, image=Chef.image)
        self.odds_change = odds_change
        self.time_till_drop = 0

    def moved(self):
        """Check if the direction of movement needs to be reversed."""
        if self.get_left() < 0 or self.get_right() > screen_width:
            self.reverse()
        else:
            same_direction = random.randrange(self.odds_change)
            if not same_direction:
                self.reverse()
        self.drop_pizza

    def reverse(self):
        dx, dy = self.get_velocity()
        self.set_velocity((-dx, dy))

    def drop_pizza(self):
        """Decrease countdown or drop pizza and reset countdown"""

        if self.time_till_drop:
            self.time_till_drop -= 1
        else:
            self.time_till_drop = int(65 / Pizza.speed)
            Pizza(self.screen, self.get_xpos())
