import game.shared.gamecontants as gameconstants

from game.casting.cast import Cast
from game.casting.cycle import Cycle
from game.casting.score import Score
from game.casting.actor import Actor

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.display_service import DisplayService

from game.shared.color import Color
from game.shared.point import Point

def main():

    # create the cast
    cast = Cast()
    

    # Cast Parameters --------------------
    # Actor cycle 1 
    position = Point(int(gameconstants.COLS / 3), int(gameconstants.ROWS / 2)) 
    position = position.scale(gameconstants.CELL_SIZE)
    cycle1 = Cycle(position, 1)
    cycle1.set_velocity(Point(0, 0))
    cycle1.set_color(gameconstants.RED)
    cycle1.set_text("]8[")
    cast.add_actor("cycle1", cycle1)

    # Actor score 1
    position = Point(1, 1) 
    position = position.scale(gameconstants.CELL_SIZE)
    score1 = Score()
    score1.set_position(position)
    score1.set_color(gameconstants.RED)
    score1.set_font_size(gameconstants.FONT_SIZE)
    cast.add_actor("score1", score1)

    # Actor cycle 2
    position = Point(int(gameconstants.COLS / 3 * 2), int(gameconstants.ROWS / 2))
    position = position.scale(gameconstants.CELL_SIZE)
    cycle2 = Cycle(position, 3)
    cycle2.set_velocity(Point(0, 0))
    cycle2.set_color(gameconstants.YELLOW)
    cycle2.set_text("¦Ä¦")
    cast.add_actor("cycle2", cycle2)

    # Actor score 2
    position = Point((gameconstants.COLS - 7), 1) 
    position = position.scale(gameconstants.CELL_SIZE)
    score2 = Score()
    score2.set_position(position)
    score2.set_color(gameconstants.YELLOW)
    score2.set_font_size(gameconstants.FONT_SIZE)
    cast.add_actor("score2", score2)

    # Actor Game Over message
    position = Point(int((gameconstants.COLS / 2) - 6), int((gameconstants.ROWS / 2) - 5))
    position = position.scale(gameconstants.CELL_SIZE)
    message = Actor()
    message.set_text("")
    message.set_position(position)
    message.set_font_size(gameconstants.FONT_SIZE * 2)
    cast.add_actor("messages", message) # Game Over Message

    # start the game
    keyboard_service = KeyboardService()
    display_service = DisplayService(
        gameconstants.CAPTION.format(gameconstants.CENTER),
        gameconstants.MAX_X,
        gameconstants.MAX_Y,
        gameconstants.CELL_SIZE,
        gameconstants.FRAME_RATE
        )

    director = Director(keyboard_service, display_service)
    director.start_game(cast)

if __name__ == "__main__":
    main()
