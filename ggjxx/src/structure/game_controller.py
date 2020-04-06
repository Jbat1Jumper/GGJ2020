from .action_constants import *

class GameController():
	def __init__(self, game, ui, gameActionInterpreter):
		self.game = game
		self.ui = ui
		self.gameActionInterpreter = gameActionInterpreter

	def run(self):
		self.game.restart()
		self.ui.render(self.game)
		while (not self.game.finished()):
			self.game.update()
			action = self.ui.getInput()
			self.gameActionInterpreter.applyAction(self.game, action)
			self.ui.render(self.game)