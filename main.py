import arcade
import random

WIDTH = 1600
HEIGHT = 900
SCREEN_TITLE = "Pinball"

BRICK_HEIGHT = 100
BRICK_WIDTH = 100
BRICK_LAYERS = 3


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color((51, 51, 51))

        self.brickList = arcade.SpriteList()
        self.click = False

    def setup(self):
        self.create_brick_list()
        self.create_palet()

    def create_brick_list(self):
        for x in range(round(WIDTH / BRICK_WIDTH)):
            for y in range(3):
                self.brick = arcade.Sprite("images/brick2.png")
                self.brick.width = BRICK_WIDTH
                self.brick.height = BRICK_HEIGHT
                self.brick.set_position((0 + self.brick.width / 2) + x * BRICK_WIDTH, (HEIGHT - self.brick.height / 2) - y * BRICK_HEIGHT)
                self.brickList.append(self.brick)

    def create_palet(self):
        self.palet = arcade.Sprite("images/palet.png")
        self.palet.set_position(WIDTH / 2, 50)
        self.palet.height = 100
        self.palet.width = 200

    def on_draw(self):
        self.clear()
        self.brickList.draw()
        self.palet.draw()

    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        if self.click:
            self.palet.set_position(x, 50)
            if self.palet.center_x <= self.palet.width / 2 :
                self.palet.set_position(self.palet.width / 2, 50)
            elif self.palet.center_x  >= WIDTH - self.palet.width / 2 :
                self.palet.set_position(WIDTH - self.palet.width / 2, 50)


    def on_mouse_press(self, x, y, button, key_modifiers):
        self.click = True

    def on_mouse_release(self, x, y, button, key_modifiers):
        self.click = False

def main():
    game = MyGame(WIDTH, HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
