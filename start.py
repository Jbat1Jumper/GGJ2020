#! python
import click
from ggjxx import settings
from ggjxx.tui import Tui
from ggjxx.gui import Gui

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

if __name__ == "__main__":
    cli()
