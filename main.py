#Troy Tural 404
#Exercice Arcade 1-2

import arcade
import random

#Cette ligne va determoiner la grandeur de l'ecran qui va s'afficher lorsque qu'on va executer le code
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Cette ligne s'agit d'une librairie de couleurs que nos cercles pourront avoir lorsqu'ils seront afficher a l'ecran
COLORS = [arcade.color.AERO_BLUE, arcade.color.ALIZARIN_CRIMSON,
          arcade.color.AQUAMARINE, arcade.color.BAKER_MILLER_PINK]

#En creant la class Cercle, on va pouvoir definir les varibles de nos cercles
class Cercle():
    def __init__(self, rayon, centre_x, centre_y, color):
        self.rayon = rayon
        self.centre_x = centre_x
        self.centre_y = centre_y
        self.color = (color)
#Cette ligne est celui qui permet d'afficher les cercles a l'ecran
    def draw(self):
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)

#En creant la class MyGAme, on va pouvoir donner un nom au fenetre qui va aparaitre lorsqu'on effectura notre code ansi qu'une liste de cercles
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_cercles = []
#Ces lignes de codes va etre celles qui permettent a nos cercles de se placer differament chaque fois que le code est de nouveau effectuer ET elle va peremttre aussi aux cercles d'avoirs des couleurs aleatoies de notre liste de couleurs et qu'ils ne vont pas depasser les bornes de l'ecran
    def setup(self):
        for _ in range(20):
            rayon = random.randint(10, 50)
            center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
            center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
            color = random.choice(COLORS)
            cercle = Cercle(rayon, center_x, center_y, color)
            self.liste_cercles.append(cercle)
#
    def on_draw(self):
        arcade.start_render()

        for cercle in self.liste_cercles:
            cercle.draw()
#Cette ligne de code est celui qui permet a dectecter la sourris sur l'ecran
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.centre_x = x
        self.centre_y = y
#Cette ligne de code va faire en sorte que chaque fois une cerle est cliquer, elle va soit disparaitre ou changer de couleur selon notre liste de couleur tout dependament de queele boutton on clique sur la souris
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):

        for cercle in self.liste_cercles:
            if x > cercle.centre_x - cercle.rayon and x < cercle.centre_x + cercle.rayon and y > cercle.centre_y - cercle.rayon and y < cercle.centre_y +cercle.rayon:
                if button == arcade.MOUSE_BUTTON_LEFT:
                    self.liste_cercles.remove(cercle)
                elif button == arcade.MOUSE_BUTTON_RIGHT:
                    cercle.color = random.choice(COLORS)


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()


