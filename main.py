import arcade
import random

WIDTH = 1920
HEIGHT = 1080
SCREEN_TITLE = "Pinball"


class Brick:
    def __init__(self, texture, xPos, yPos, width, height):
        self.texture = texture
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height

    def create_sprite(self):
        self.brick = arcade.Sprite(self.texture)
        self.brick.center_x = self.xPos
        self.brick.center_y = self.yPos
        self.brick.width = self.width
        self.brick.height = self.height


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.brick = arcade.Sprite("brick1.png")
        arcade.set_background_color((51, 51, 51))

        self.brickList = arcade.SpriteList()

    def setup(self):
        self.brick.width = 200
        self.brick.height = 100
        self.brick.center_X = 900
        self.brick.center_y = HEIGHT / 2
        self.brickList.append(self.brick)

    def on_draw(self):
        self.clear()
        self.brickList.draw()

    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass


def main():
    game = MyGame(WIDTH, HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
