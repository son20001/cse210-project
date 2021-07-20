import arcade
from game import constants

class ResultView(arcade.View):
    def __init__(self, score):
        super().__init__()
        self.texture = arcade.load_texture(constants.RESULT_BACKGROUND)
        arcade.set_background_color(arcade.color.BUD_GREEN)

        self.pen_sound = arcade.Sound(constants.PEN)
        self.text_angle = 0
        self.score = round(score.get_score(),1)
        
    def on_show(self):
        self.setup()
    
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()
        else:
            game_view = self.window.restart()
            game_view.setup()
            self.window.show_view(game_view)

    def setup(self):
        self.pen_sound.play(constants.VOLUME * 4, loop= False)

    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH + 200, constants.SCREEN_HEIGHT + 200)

        text_x = (constants.SCREEN_WIDTH / 2) - 140
        text_y = constants.SCREEN_HEIGHT / 2
        text = "your score is " + str(self.score)
        arcade.draw_text(text, text_x, text_y + 200, arcade.color.BLACK_OLIVE, 30)
        
        if self.score > 60:
            text = "Captain Sherman call a bombing mission directly on his \n\nposition to avoid capture and to defense the fort.\n\n After the bombing, He was rescued safely \n\nand awarded the Distinguished Service Cross."
            arcade.draw_text(text, text_x - 275, text_y -100, arcade.color.BLACK_OLIVE, 30, width=constants.SCREEN_WIDTH - 100, align= "center")
        else:
            text = "Captain Sherman call a bombing mission directly on his \n\nposition to avoid capture and to defense the fort.\n\n After the bombing, He died in battle, but protected \n\nthe fortress and awarded the Medal of Honor."
            arcade.draw_text(text, text_x - 275, text_y -100, arcade.color.BLACK_OLIVE, 30, width=constants.SCREEN_WIDTH - 100, align= "center")

        text = "Press any key to restart"
        arcade.draw_text(text,text_x - 280,text_y-250, arcade.color.BLACK_OLIVE, 30, width=constants.SCREEN_WIDTH - 100, align= "center")