#Importation des modules "Arcade" et "Random" pour pouvoir les utiliser
import arcade
import random

#Création de la banque de couleurs
colors = [arcade.csscolor.GOLD, arcade.csscolor.AQUAMARINE, arcade.csscolor.BLANCHED_ALMOND, arcade.csscolor.SLATE_GRAY, arcade.csscolor.DARK_GOLDENROD, arcade.csscolor.FOREST_GREEN, arcade.csscolor.DARK_SEA_GREEN,
          arcade.csscolor.ROYAL_BLUE, arcade.csscolor.LIGHT_SLATE_GRAY, arcade.csscolor.PAPAYA_WHIP, arcade.csscolor.MEDIUM_PURPLE, arcade.csscolor.DARK_TURQUOISE, arcade.csscolor.LIGHT_CORAL, arcade.csscolor.FLORAL_WHITE]

#Définition des variables pour la taille de la fenêtre
screen_width = 1200
screen_height = 900

#Création de la classe de l'objet balle (dimensions, couleur aléatoire et déplacement dans la fenêtre)
#L'input est la position reçue du click de la souris ("x" et "y") qui sera la position où la balle apparaîtra
class Ball:
    def __init__(self, x, y):
        self.rayon = 25
        self.center_x = x
        self.center_y = y
        self.color = random.choice(colors)
        self.change_x = 7
        self.change_y = 7

    def on_update(self):
        if self.center_x < 25:
            self.change_x *= -1
        if self.center_x > 1175:
            self.change_x *= -1
        if self.center_y < 25:
            self.change_y *= -1
        if self.center_y > 875:
            self.change_y *= -1

        self.center_x += self.change_x
        self.center_y += self.change_y

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.rayon, self.color)


#Création de la classe de l'objet rectangle (dimensions, couleur aléatoire et déplacement vertical)
#L'input est la position reçue du click de la souris ("x" et "y") qui sera la position où le rectangle apparaîtra
class Rectangle:
    def __init__(self, x, y):
        self.height = 72
        self.width = 24
        self.center_x = x
        self.center_y = y
        self.color = random.choice(colors)
        self.change_y = 7

    def on_update(self):
        if self.center_y < 24:
            self.change_y *= -1
        if self.center_y > 876:
            self.change_y *= -1

        self.center_y += self.change_y

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.height, self.width, self.color, 90)

#Création de la classe MyGame (création de la fenêtre et dessine une balle pour un click gauche ou un rectangle pour un click droit)
#Les inputs sont la position de la souris ("x" et "y") où l'objet (balle ou rectangle) apparaîtra et le click (droit, représenté par "arcade.MOUSE_BUTTON_RIGHT" ou gauche, représenté par "arcade.MOUSE_BUTTON_LEFT") qui décidera de l'objet dessiné.
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(screen_width, screen_height, "Clicks")
        self.list_balls = []
        self.list_rectangles = []

    def setup(self):
        pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.list_balls.append(Ball(x, y))
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.list_rectangles.append(Rectangle(x, y))

    def on_update(self, delta_time: float):
        for Ball in self.list_balls:
            Ball.on_update()
        for Rectangle in self.list_rectangles:
            Rectangle.on_update()

    def on_draw(self):
        arcade.start_render()
        for Ball in self.list_balls:
            Ball.draw()
        for Rectangle in self.list_rectangles:
            Rectangle.draw()

#Fonction qui fera démarrer le programme
def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()

#Lancement du programme
main()
