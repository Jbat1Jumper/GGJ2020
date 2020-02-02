from .action_constants import *
from ..game.game import Game

class GameActionInterpreter():
	def __init__(self):
		pass

	def applyAction(self, game, action):
		if (action == ACTION_GO_UP):
			game.go_up()
		if (action == ACTION_GO_DOWN):
			game.go_down()
		if (action == ACTION_GO_LEFT):
			game.go_left()
		if (action == ACTION_GO_RIGHT):
			game.go_right()
		if (action == ACTION_ROTATE_ROBOT):
			game.switchControlledRobot()
		if (action == ACTION_QUIT):
			game.terminate()