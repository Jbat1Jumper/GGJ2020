from .action_constants import *

class GameController():
	def __init__(self, game, ui, gameActionInterpreter):
		self.game = game
		self.ui = ui
		self.actionHandlers = [ui, gameActionInterpreter]

	def run(self):
		self.game.restart()
		self.ui.render(self.game)
		while (not self.ui.shouldTerminate(self.game)):
			self.game.update()
			action = self.ui.getInput()
			self.applyAction(action)
			self.ui.render(self.game)

	def applyAction(self, action):
		if not action:
			# Ignore action None
			return

		for handler in self.actionHandlers:
			if handler.applyAction(action):
				return

		print("hay un warning kpo: no sabemos que hacer con la accion '{}'".format(action))