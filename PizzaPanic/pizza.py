import random
from livewires import games

from lives import *

screen_width = 710
screen_height = 786


class Pizza(games.Sprite):
    """A pizza class"""
    image = games.load_image("Images/pizza.png")
    start_y = 90
    speed = 1
    lives = 3
    livesx = 20

    def __init__(self, screen, x, y, image):
        self.init_sprite(screen=screen, x=x, y=Pizza.start_y, dx=0, dy=Pizza.speed, image=Pizza.image)

    def moved(self):
        """Checks if the pizza has reached the bottom"""
        if self.get_bottom > screen_height:
            self.reached_bottom()

    def handle_caught(self):
        self.destroy()

    def reached_bottom(self):
        """Handles the event when pizza reaches the bottom uncaught"""

        self.lives -= 1
        self.destroy()
        for live in self.screen.all_objects():
            if isinstance(live, Lives):
                live.destroy()
                break

        if self.lives == 0:
            self.game_over()

        for live in self.lives:
            Lives(screen=self.screen, x=self.livesx)
            self.livesx += 10

        if Pizza.lives == 0:
            self.game_over()

    def game_over(self):
        """Ends the game, destroy each game element except for the score"""

        for game_object in self.screen.all_objects():
            if not isinstance(game_object, games.Text):
                game_object.destroy()

        games.Message(screen=self.screen, x=screen_width / 2, y=screen_height / 2, size=90, lifetime=500,
                      after_death=self.screen.quit())
