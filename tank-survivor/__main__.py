import arcade
from game import constants
from game.title_view import TitleView
from game.game_view import GameView
from game.score import Score

class Window(arcade.Window):

    def __init__(self):

        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        self.volume = constants.VOLUME

        self.score = Score()
        self.start_view = TitleView()
        self.background_music = arcade.Sound(constants.BGM)
        self.background_music.play(self.volume, loop = True)

    def setup(self):
        gameview = GameView()
        return gameview
    
    def restart(self):
        titleView = TitleView()
        return titleView

def main():
    window = Window()
    start_view = TitleView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()