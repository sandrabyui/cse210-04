from game.casting.actor import Actor


class Trail(Actor):
    """
    """
    def __init__(self, pos, color):
        """
        """
        super().__init__()
        self.set_text("#")
        self.set_position(pos)
        self.set_color(color)
