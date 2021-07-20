from game import constants
from arcade.gui import UIImageButton

class Button(UIImageButton):
    def __init__(self, view, game, x = constants.SCREEN_WIDTH / 2, y = constants.SCREEN_HEIGHT / 2,  text = "", normal_texture = None):
        super().__init__(center_x= x, center_y= y,
        text = text, normal_texture = normal_texture)
        self.view = view
        self.center_x = x
        self.center_y = y
        self.window = game

    def on_click(self):
        self.view.setup()
        self.window.show_view(self.view)