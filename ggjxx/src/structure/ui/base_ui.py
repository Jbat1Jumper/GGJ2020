class BaseUI():
	def __init__(self):
		pass

	def getInput(self):
		pass

	def render(self, game):
		pass

	def shouldTerminate(self, game):
		return game.finished()

	def applyAction(self, game):
		return False
