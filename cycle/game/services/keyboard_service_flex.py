import pyray

from game.services.keyboard_service import KeyboardService
from game.shared.point import Point


class KeyboardServiceFlex(KeyboardService):
    """
    """

    def __init__(self, key_set_num = 0):
        """
        """
        super().__init__()
        self._dx = 0
        self._dy = -1

        self._key_sets = {
            0 : {'l':pyray.KEY_LEFT, 'r':pyray.KEY_RIGHT, 'u':pyray.KEY_UP, 'd':pyray.KEY_DOWN},
            1 : {'l':pyray.KEY_A, 'r':pyray.KEY_D, 'u':pyray.KEY_W, 'd':pyray.KEY_S},
            2 : {'l':pyray.KEY_F, 'r':pyray.KEY_H, 'u':pyray.KEY_T, 'd':pyray.KEY_G},
            3 : {'l':pyray.KEY_J, 'r':pyray.KEY_L, 'u':pyray.KEY_I, 'd':pyray.KEY_K},
            4 : {'l':pyray.KEY_KP_4, 'r':pyray.KEY_KP_6, 'u':pyray.KEY_KP_8, 'd':pyray.KEY_KP_5}
        }

        self.set_keys(key_set_num)


    def set_keys(self, key_set_num):
        """
        """
        self._left  = self._key_sets[key_set_num]['l']
        self._right = self._key_sets[key_set_num]['r']
        self._up    = self._key_sets[key_set_num]['u']
        self._down  = self._key_sets[key_set_num]['d']


    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """

        if pyray.is_key_down(self._left) and self._dx != 1:
            self._dx = -1
            self._dy = 0

        if pyray.is_key_down(self._right) and self._dx != -1:
            self._dx = 1
            self._dy = 0

        if pyray.is_key_down(self._up) and self._dy != 1:
            self._dx = 0
            self._dy = -1

        if pyray.is_key_down(self._down) and self._dy != -1:
            self._dx = 0
            self._dy = 1

        direction = Point(self._dx, self._dy)
        direction = direction.scale(self._cell_size)

        return direction
