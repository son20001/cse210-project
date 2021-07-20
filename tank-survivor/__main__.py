import arcade
from game import constants
from game.title_view import TitleView
from game.game_view import GameView
from game.score import Score

class Window(arcade.Window):
    """Open and control main window
    Stereotype:
        Controller
    Attributes: 
        master_volume(file_path): file path for volume
        score (Score): initalize the score class
        background_music (arcade.Sound): initalize background music in arcade.Sound
    Contributors:
            Isabel Aranguren
            Reed Hunsaker
    """
    def __init__(self):
        """Initalize the Window class
        Args:
            self (Window): an instance of Window
        Contributors:
            Reed Hunsaker
            Isabel Aranguren
        """
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.TITLE)

        self.volume = constants.VOLUME

        self.score = Score()
        self.start_view = TitleView()
        self.background_music = arcade.Sound(constants.BGM)
        self.background_music.play(self.volume, loop = True)

    def setup(self):
        gameview = GameView()
        return gameview
    

def main():
    window = Window()
    start_view = TitleView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()