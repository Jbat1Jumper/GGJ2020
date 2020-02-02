#! python
import click
from ggjxx import settings
# from ggjxx.src.TerminalUI.tui import Tui
from ggjxx.src.graphiUI.gui import Gui
from ggjxx.src.game.cell import Cell
from ggjxx.src.game.game import Game, Map
from ggjxx.src.structure.game_controller import GameController
from ggjxx.src.structure.game_action_interpreter import GameActionInterpreter
from ggjxx.src.structure.ui.terminal_ui import TerminalUI
from ggjxx.src.structure.ui.graphics_ui import GraphicsUI
from ggjxx.src.structure.levels.level1 import Level1

@click.group()
def cli():
    pass

@cli.command(help="Corre el juego por consola")
def tui():
    gameLevel = Level1()
    game = Game(gameLevel)

    ui = TerminalUI()

    gameActionInterpreter = GameActionInterpreter()

    gameController = GameController(game, ui, gameActionInterpreter)
    gameController.run()


@cli.command(help="Corre el juego con interfaz grafica")
def gui():
    gameLevel = Level1()
    game = Game(gameLevel)

    ui = GraphicsUI()

    gameActionInterpreter = GameActionInterpreter()

    gameController = GameController(game, ui, gameActionInterpreter)
    gameController.run()

@cli.command(help="Prueba de Game")
def game():
    g = Game(1,1)


@cli.command(help="Prueba de Map")
def game():
    m = Map(1,1)
    m.get_cell(0, 0)


@cli.command(help="Prueba de Cell")
def cell():
    c = Cell()

    print('--------------------')
    print('Testing fire')

    print(c.hasFire())
    c.setOnFire()
    print(c.hasFire())
    c.putOutFire()
    print(c.hasFire())

    print('--------------------')
    print('Testing radiation')

    print(c.hasRadiation())
    c.putRadiation()
    print(c.hasRadiation())
    c.putOutRadiation()
    print(c.hasRadiation())


    print('--------------------')
    print('Testing directions')

    print(c.canGo("RIGHT"))
    print(c.canGo("LEFT"))
    print(c.canGo("UP"))
    print(c.canGo("DOWN"))

    c.setAvailableDirections([])

    print(c.canGo("RIGHT"))
    print(c.canGo("LEFT"))
    print(c.canGo("UP"))
    print(c.canGo("DOWN"))

    c.setAvailableDirections(["UP","RIGHT","LEFT","DOWN"])

    print(c.canGo("RIGHT"))
    print(c.canGo("LEFT"))
    print(c.canGo("UP"))
    print(c.canGo("DOWN"))

    c.setAvailableDirections(["UP","RIGHT"])

    print("up-right")
    print(c.canGo("RIGHT"))
    print(c.canGo("LEFT"))
    print(c.canGo("UP"))
    print(c.canGo("DOWN"))

    c.setAvailableDirections(["LEFT","DOWN"])

    print("left-down")
    print(c.canGo("RIGHT"))
    print(c.canGo("LEFT"))
    print(c.canGo("UP"))
    print(c.canGo("DOWN"))



if __name__ == "__main__":
    cli()
