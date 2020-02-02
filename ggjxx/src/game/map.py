from .cell import Cell

class Map:
    def __init__(self, w, h, robots, startX, startY):
        self.width = w
        self.height = h
        self.robots = robots
        self.cells = [[Cell() for _ in range(w)] for _ in range(h)]
        self.startX = startX
        self.startY = startY

    def get_robots(self):
        return self.robots

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def getCell(self, x, y):
        return self.cells[y][x]

    def getStartingX(self):
        return self.startX

    def getStartingY(self):
        return self.startY

    def validate_coords(self, x, y):
        assert 0 <= x and x < self.width, "coord x ouf of bounds"
        assert 0 <= y and y < self.height, "coord y out of bounds"

    def is_border(self, x, y):
        return x == 0 \
            or x == self.width - 1 \
            or y == 0 \
            or y == self.height - 1

    def get_cell(self, x, y):
        self.validate_coords(x, y)
        return self.cells[y][x]

    def set_object(self, x, y, o):
        self.validate_coords(x, y)
        self.cells[y][x] = o