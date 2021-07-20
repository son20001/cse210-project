# Imports
import arcade
import random
from game import constants

# Constants
SCALING = 1.0

# Classes
class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        # Setup the empty sprite lists
        self.enemies_list = arcade.SpriteList()
        self.explosion_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

        self.texture = arcade.load_texture(constants.GAME_BACKGROUND)
        self.explosion_sound = arcade.load_sound(constants.EXPLOSION)
        self.drop_sound = arcade.load_sound(constants.DROP)

    def setup(self):
        arcade.set_background_color(arcade.color.YELLOW_GREEN)

        self.player = arcade.Sprite(constants.PLAYER_IMAGE, SCALING)
        self.player.center_y = 0
        self.player.left = 10
        self.all_sprites.append(self.player)

        arcade.schedule(self.add_enemy, 1.0)

        self.paused = False
        self.collided = False
        self.collision_timer = 0.0

    def add_enemy(self, delta_time: float):
        enemy = arcade.Sprite(constants.BOMB_IMAGE, 0.5)

        enemy.left = random.randint(10, constants.SCREEN_WIDTH - 10)
        enemy.top = constants.SCREEN_HEIGHT

        enemy.velocity = (0, random.randint(-200, -50))

        arcade.play_sound(self.drop_sound, 0.4)

        self.enemies_list.append(enemy)
        self.all_sprites.append(enemy)
    
    def explosion(self, center_x):

        # First, create the new enemy sprite
        explosion = arcade.Sprite(constants.EXPLOSION_IMAGE, 0.15)

        # Set its position to a random height and off screen right
        explosion.left = center_x - 50
        explosion.bottom = 0

        arcade.play_sound(self.explosion_sound, 0.8)

        self.explosion_list.append(explosion)
        self.all_sprites.append(explosion)

    def on_key_press(self, symbol: int, modifiers: int):
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
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self.all_sprites.draw()


if __name__ == "game_view":
    # Create a new Space Shooter window
    space_game = GameView(
        int(constants.SCREEN_WIDTH * SCALING), int(constants.SCREEN_HEIGHT * SCALING), constants.SCREEN_TITLE
    )
    # Setup to play
    space_game.setup()
    # Run the game
    arcade.run()



