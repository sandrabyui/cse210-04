import pyray
import game.shared.gamecontants as gameconstants

from game.shared.point import Point


class KeyboardService:
    """Detects player input. 

    The responsibility of a KeyboardService is to detect player key presses and translate them into 
    a point representing a direction.

    Attributes:
        cell_size (int): For scaling directional input to a grid.
    """

    def __init__(self):
        """Constructs a new KeyboardService using the specified cell size.

        Args:
            cell_size (int): The size of a cell in the display grid.
        """
        self._cell_size = gameconstants.CELL_SIZE
        self._dx = 0
        self._dy = 0

    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """
        self._dx = 0
        self._dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            self._dx = -1

        if pyray.is_key_down(pyray.KEY_RIGHT):
            self._dx = 1

        if pyray.is_key_down(pyray.KEY_UP):
            self._dy = -1

        if pyray.is_key_down(pyray.KEY_DOWN):
            self._dy = 1

        direction = Point(self._dx, self._dy)
        direction = direction.scale(self._cell_size)

        return direction
