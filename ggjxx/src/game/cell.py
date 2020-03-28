from .constants import UP,DOWN,RIGHT,LEFT

class Cell:
    def __init__(self):
        self.robots = []
        self._hasFire = False
        self.hadFire = False
        self._hasRadiation = False
        self.hadRadiation = False
        self._canGoRight = True
        self._canGoLeft = True
        self._canGoUp = True
        self._canGoDown = True
        self._hasReactor = False
        self._hadReactor = False
        self._reactorIsFaulty = False
        self._hasFow = True

    def hasFow(self):
        return self._hasFow

    def hasFire(self):
        return self._hasFire

    def setOnFire(self):
        self._hasFire = True

    def putOutFire(self):
        self.hadFire = self.hadFire or self._hasFire
        self._hasFire = False

    def hasRadiation(self):
        return self._hasRadiation

    def putRadiation(self):
        self._hasRadiation = True

    def putOutRadiation(self):
        self.hadRadiation = self.hadRadiation or self._hasRadiation 
        self._hasRadiation = False

    def setWorkingReactor(self):
        self._hasReactor = True
        self._reactorIsFaulty = False

    def setFaultyReactor(self):
        self._hasReactor = True
        self._reactorIsFaulty = True

    def hasReactor(self):
        return self._hasReactor

    def fixReactor(self):
        if (self.hasReactor() and self.reactorIsFaulty()):
            self._hasReactor = True
            self._reactorIsFaulty = False
            # print('reactor fixed')

    def reactorIsFaulty(self):
        return self._reactorIsFaulty

    def canGo(self, direction):
        if direction == UP:
            return self._canGoUp
        if direction == DOWN:
            return self._canGoDown
        if direction == LEFT:
            return self._canGoLeft
        if direction == RIGHT:
            return self._canGoRight
        return False

    def setAvailableDirections(self, directions):
        self._canGoUp = False
        self._canGoDown = False
        self._canGoLeft = False
        self._canGoRight = False

        for direction in directions:
            if direction == UP:
                self._canGoUp = True
            if direction == DOWN:
                self._canGoDown = True
            if direction == LEFT:
                self._canGoLeft = True
            if direction == RIGHT:
                self._canGoRight = True