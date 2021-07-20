import arcade
from game import constants

class ResultView(arcade.View):
    def __init__(self, score):
        super().__init__()
        self.texture = arcade.load_texture(constants.RESULT_BACKGROUND)
        arcade.set_background_color(arcade.color.BUD_GREEN)

        self.pen_sound = arcade.Sound(constants.PEN)
        self.text_angle = 0
        self.score = score

        
    def on_show(self):
        self.setup()
    
    def on_key_press(self, symbol: int, modifiers: int):
        game_view = self.window.restart()
        game_view.setup()

    def setup(self):
        self.pen_sound.play(constants.VOLUME * 3, loop= False)

    def on_draw(self):
        arcade.start_render()
        

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
    
    def on_draw(self):
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)