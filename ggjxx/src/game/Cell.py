from ggjxx.src.game.game import UP,DOWN,RIGHT,LEFT

class Cell:
    def __init__(self):
        self.robots = []
        self._hasFire = False
        self._hasRadiation = False
        self._canGoRight = True
        self._canGoLeft = True
        self._canGoUp = True
        self._canGoDown = True

    def hasFire(self):
        return self._hasFire

    def setOnFire(self):
        self._hasFire = True

    def putOutFire(self):
        self._hasFire = True

    def hasRadiation(self):
        return self._hasRadiation

    def putRadiation(self):
        self._hasRadiation = True

    def putOutRadiation(self):
        self._hasRadiation = False

    def canGo(self, direction):
        if direction == UP:
            return self._canGoUp
        if direction == DOWN:
            return self._canGoDown
        if direction == LEFT:
            return self._canGoLeft
        if direction == RIGHT:
            return self._canGoRight
        return False;

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
            return False;