from .action_constants import *
from ..game.game import Game

class GameActionInterpreter():
	def __init__(self):
		pass

	def applyAction(self, game, action):
		if (action == ACTION_GO_UP):
			game.go_up()
		elif (action == ACTION_GO_DOWN):
			game.go_down()
		elif (action == ACTION_GO_LEFT):
			game.go_left()
		elif (action == ACTION_GO_RIGHT):
			game.go_right()
		elif (action == ACTION_ROTATE_ROBOT):
			game.switchControlledRobot()
		elif (action == ACTION_QUIT):
			game.terminate()
		elif (action == ACTION_RESTART):
			game.restart()
		elif action:
			print("Unknown aktion: {}".format(action))