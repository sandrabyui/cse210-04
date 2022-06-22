from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.

    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.

        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score1 = cast.get_first_actor("score1")  # P1
        score2 = cast.get_first_actor("score2")  # P2
        cycle_one = cast.get_first_actor("cycle_one")  # P1
        cycle_two = cast.get_first_actor("cycle_two")  # P2
        segments_one = cycle_one.get_segments()  # P1
        segments_two = cycle_two.get_segments()  # P2
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actors(segments_one)  # P1
        self._video_service.draw_actors(segments_two)  # P2
        self._video_service.draw_actor(score1)  # P1
        self._video_service.draw_actor(score2)  # P2
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()
