import arcade
from game import constants
from game.game_view import GameView
from arcade.gui import UIManager
from game.button import Button

class TitleView(arcade.View):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(constants.TITLE_BACKGROUND)
        self.ui_manager = UIManager()
        
    def on_show(self):
        self.setup()
    
    def setup(self):
        self.ui_manager.purge_ui_elements()

        start_texture = arcade.load_texture(constants.START_BUTTON)
        play_button = Button(GameView(), self.window, y = (constants.SCREEN_HEIGHT / 2) - 20, normal_texture= start_texture)

        instruct_texture = arcade.load_texture(constants.INSTRUCTION_BUTTON)
        instruct_button = Button(HowToPlayView(), self.window, y = (constants.SCREEN_HEIGHT / 2) - 150, normal_texture = instruct_texture)

        self.ui_manager.add_ui_element(play_button)
        self.ui_manager.add_ui_element(instruct_button)
        
    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
            


class HowToPlayView(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()
        self.texture = arcade.load_texture(constants.INSTRUCTION_BACKGROUND)

    def on_show(self):
        self.setup()
    
    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

    def setup(self):
        self.ui_manager.purge_ui_elements()

        back_texture = arcade.load_texture(constants.BACK_BUTTON)
        self.back_button = Button(TitleView(), self.window, x = constants.SCREEN_WIDTH / 2, y = 100, normal_texture= back_texture)

        self.ui_manager.add_ui_element(self.back_button)
    
    def on_show_view(self):
        arcade.load_texture(constants.TITLE_BACKGROUND)
