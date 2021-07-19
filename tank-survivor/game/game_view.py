import arcade

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        """Sets up the game for the current level"""
        arcade.set_background_color(arcade.color.SKY_BLUE)
        pass

    def on_key_press(self, symbol: int, modifiers: int):
        """Processes key presses

        Arguments:
            key {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were down at the time
        """

        if symbol == arcade.key.A or symbol == arcade.key.LEFT:
            self.player.change_


    def on_key_release(self, key: int, modifiers: int):
        """Processes key releases

        Arguments:
            key {int} -- Which key was released
            modifiers {int} -- Which modifiers were down at the time
        """

    def on_update(self, delta_time: float):
        """Updates the position of all game objects

        Arguments:
            delta_time {float} -- How much time since the last call
        """
        pass

    def on_draw(self):
        pass

if __name__ == "__main__":
    window = Game()
    window.setup()
    arcade.run()