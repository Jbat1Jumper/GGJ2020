from .action_constants import *
from ..game.game import Game

class GameActionInterpreter():
	def __init__(self, game):
		self.game = game

	def applyAction(self, action):
		if (action == ACTION_GO_UP):
			self.game.go_up()
			return True
		elif (action == ACTION_GO_DOWN):
			self.game.go_down()
			return True
		elif (action == ACTION_GO_LEFT):
			self.game.go_left()
			return True
		elif (action == ACTION_GO_RIGHT):
			self.game.go_right()
			return True
		elif (action == ACTION_ROTATE_ROBOT):
			self.game.switchControlledRobot()
			return True
		elif (action == ACTION_QUIT):
			self.game.terminate()
			return True
		elif (action == ACTION_RESTART):
			self.game.restart()
			return True
		elif action:
			print("Unknown aktion: {}".format(action))

		return False