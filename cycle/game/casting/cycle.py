from game.casting.actor import Actor
import game.shared.gamecontants as gameconstants

from game.services.keyboard_service_flex import KeyboardServiceFlex


class Cycle(Actor):
    """
    Constructs main player unit.

    Responsible for direction, position, death status etc
    """
    def __init__(self, pos, num = 0):
        """
        Constructor 

        Inherits from Actor
        Sets default values
        """
        super().__init__()
        self.set_text("@")
        self.set_position(pos)
        self._keyboard_service_flex = KeyboardServiceFlex(num)
        self._dead = False
        self._previous_position = pos
    
    def get_direction(self):
        """
        Get velocity and directional inputs
        
        Returns velocity

        """
        velocity = self._keyboard_service_flex.get_direction()
        return velocity

    def die(self):
        """
        Sets _dead to True 
        and sets actor color to white

        """
        self._dead = True
        self.set_color(gameconstants.WHITE)

    def move_next(self, max_x, max_y):
        """
        Finds position and from parent moves to next position
        according to velocity
        """
        self._previous_position = self._position
        super().move_next(max_x, max_y)

    def get_previous_position(self):
        """
        Returns previous position
        """

        return self._previous_position

    def isDead (self):
        """
        Returns _dead value
        """
        return self._dead