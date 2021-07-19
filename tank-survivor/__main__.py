# Imports
import arcade
import random
from game import constants

# Constants
SCALING = 1.0

# Classes

class TankSurvivor(arcade.Window):
    """Space Shooter side scroller game
    Player starts on the left, enemies appear on the right
    Player can move anywhere, but not off screen
    Enemies fly to the left at variable speed
    Collisions end the game
    """

    def __init__(self, width: int, height: int, title: str):
        """Initialize the game"""
        super().__init__(width, height, title)

        # Setup the empty sprite lists
        self.enemies_list = arcade.SpriteList()
        self.explosion_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

    def setup(self):
        """Get the game ready to play"""

        # Set the background color
        arcade.set_background_color(arcade.color.YELLOW_GREEN)

        # Setup the player
        self.player = arcade.Sprite(constants.PLAYER_IMAGE, SCALING)
        self.player.center_y = 0
        self.player.left = 10
        self.all_sprites.append(self.player)

        # Spawn a new enemy every second
        arcade.schedule(self.add_enemy, 1.0)


        # Unpause everything and reset the collision timer
        self.paused = False
        self.collided = False
        self.collision_timer = 0.0

    def add_enemy(self, delta_time: float):
        """Adds a new enemy to the screen

        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """

        # First, create the new enemy sprite
        enemy = arcade.Sprite(constants.BOMB_IMAGE, 0.5)

        # Set its position to a random height and off screen right
        enemy.left = random.randint(10, self.width - 10)
        enemy.top = random.randint(self.height - 10, self.height)

        # Set its speed to a random speed heading left
        enemy.velocity = (0, random.randint(-200, -50))

        # Add it to the enemies list
        self.enemies_list.append(enemy)
        self.all_sprites.append(enemy)
    
    def explosion(self, center_x):

        # First, create the new enemy sprite
        explosion = arcade.Sprite(constants.EXPLOSION_IMAGE, 0.1)

        # Set its position to a random height and off screen right
        explosion.left = center_x
        explosion.bottom = 0

        # Set its speed to a random speed heading left
        # explosion.velocity = (0, 0)

        # Add it to the enemies list
        self.explosion_list.append(explosion)
        self.all_sprites.append(explosion)

    def on_key_press(self, symbol: int, modifiers: int):
        """Handle user keyboard input
        Q: Quit the game
        P: Pause the game
        I/J/K/L: Move Up, Left, Down, Right
        Arrows: Move Up, Left, Down, Right

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if symbol == arcade.key.ESCAPE:
            # Quit immediately
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused

        if symbol == arcade.key.J or symbol == arcade.key.LEFT:
            self.player.change_x = -250

        if symbol == arcade.key.L or symbol == arcade.key.RIGHT:
            self.player.change_x = 250

    def on_key_release(self, symbol: int, modifiers: int):
        """Undo movement vectors when movement keys are released

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """

        if (
            symbol == arcade.key.J
            or symbol == arcade.key.L
            or symbol == arcade.key.LEFT
            or symbol == arcade.key.RIGHT
        ):
            self.player.change_x = 0

    def on_update(self, delta_time: float):
        # Did we collide with something earlier? If so, update our timer
        if self.collided:
            self.collision_timer += delta_time
            # If we've paused for two seconds, we can quit
            if self.collision_timer > 2.0:
                arcade.close_window()
            # Stop updating things as well
            return

        # If we're paused, don't update anything
        if self.paused:
            return

        # Did we hit anything? If so, end the game
        if self.player.collides_with_list(self.enemies_list) or self.player.collides_with_list(self.explosion_list):
            self.collided = True
            self.collision_timer = 0.0
            arcade.play_sound(self.collision_sound)

        # Update everything
        for sprite in self.all_sprites:
            sprite.center_x = int(
                sprite.center_x + sprite.change_x * delta_time
            )
            sprite.center_y = int(
                sprite.center_y + sprite.change_y * delta_time
            )
        # self.all_sprites.update()

        for sprite in self.enemies_list:
            if sprite.bottom < 0:
                sprite.remove_from_sprite_lists()
                self.explosion(sprite.center_x)

        # Keep the player on screen
        if self.player.bottom < 0:
            self.player.bottom = 0
        if self.player.left < 0:
            self.player.left = 0

    def on_draw(self):
        """Draw all game objects"""

        arcade.start_render()
        self.all_sprites.draw()


if __name__ == "__main__":
    # Create a new Space Shooter window
    space_game = TankSurvivor(
        int(constants.SCREEN_WIDTH * SCALING), int(constants.SCREEN_HEIGHT * SCALING), constants.SCREEN_TITLE
    )
    # Setup to play
    space_game.setup()
    # Run the game
    arcade.run()



