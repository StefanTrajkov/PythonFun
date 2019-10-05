from livewires import games, colour

screen_width = 710
screen_height = 786


class Skillet(games.Sprite):
    image = games.load_image("Images/skillet.png")

    def __init__(self, screen, x, y):
        self.init_sprite(screen, x=x, y=y, image=Skillet.image)
        self.score_value = 0
        self.score_text = games.Text(screen=self.screen, x=650, y=20, text="Score: 0", size=25, colour=colour.black)

    def moved(self):
        """Moves the skillet to mouse position only sideways"""
        x, y = self.screen.mouse_pos()
        self.move_to(x, self.getypos())
        if self.get_left() < 0:
            self.set_left(0)
        if self.get_right() > screen_width:
            self.set_right(screen_width)
        self.check_for_catch()

    def check_for_catch(self):
        for pizza in self.overlapping_objects():
            self.handle_caught()
            pizza.handle_caught()

    def handle_caught(self):
        """Increase and display score."""
        self.score_value += 10
        self.score_text.set_text("Score: " + str(self.score_value))
