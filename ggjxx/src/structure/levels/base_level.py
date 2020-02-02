class BaseLevel():
	def __init__(self):
		self.robots = None
		self.map = None
		self.max_turns = None

	def getRobots(self):
		return self.robots

	def getMap(self):
		return self.map

	def getMaxTurns(self):
		return self.max_turns