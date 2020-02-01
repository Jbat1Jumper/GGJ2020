#! python
import click
from ggjxx import settings
from ggjxx.src.TerminalUI.tui import Tui
from ggjxx.src.graphiUI.gui import Gui
from ggjxx.src.game.cell import Cell
from ggjxx.src.game.game import Game

@click.group()
def cli():
    pass

@cli.command(help="Corre el juego por consola")
def tui():
    t = Tui()
    t.init()
    t.run()
    t.teardown()


@cli.command(help="Corre el juego con interfaz grafica")
def gui():
    g = Gui()
    g.init()
    g.run()
    g.teardown()

@cli.command(help="Prueba de Game")
def game():
    g = Game(1,1)


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
