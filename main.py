import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = []

circle_x = 20
circle_y = 20

circle_change_x = 7
circle_change_y = 7

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        pass

    def setup(self):

        pass

    def on_update(self, delta_time: float):
        global circle_x
        global circle_y
        global circle_change_x
        global circle_change_y

        if circle_x < 20:
            circle_change_x *= -1
        if circle_x > SCREEN_WIDTH - 20:
            circle_change_x *= -1
        if circle_y < 20:
            circle_change_y *= -1
        if circle_y > SCREEN_HEIGHT - 20:
            circle_change_y *= -1

        circle_x += circle_change_x
        circle_y += circle_change_y

    def on_draw(self):

        arcade.start_render()
        arcade.draw_circle_filled(circle_x, circle_y, 20, (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))




def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()

main()
