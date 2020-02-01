from . import cell


UP    = "UP"
DOWN  = "DOWN"
LEFT  = "LEFT"
RIGHT = "RIGHT"


class Map:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.cells = [[cell() for _ in range(w)] for _ in range(h)]

    def validate_coords(self, x, y):
        assert 0 <= x and x < self.width, "coord x ouf of bounds"
        assert 0 <= y and y < self.height, "coord y out of bounds"

    def is_border(self, x, y):
        return x == 0 \
            or x == self.width - 1 \
            or y == 0 \
            or y == self.height - 1

    def get_object(self, x, y):
        validate_coords(x, y)
        return self.cells[y][x]

    def set_object(self, x, y, o):
        validate_coords(x, y)
        self.cells[y][x] = o

    def has_wall(self, x, y, direction):
        validate_coords(x, y)
        q = {
            LEFT: lambda: True if x == 0 else self.v_valls[y][x-1],
            RIGHT: lambda: True if x == self.width-1 else self.v_valls[y][x],
            UP: lambda: True if y == 0 else self.h_valls[y-1][x],
            DOWN: lambda: True if y == self.height-1 else self.v_valls[y][x],
        }
        return q[direction]()

    def set_wall(self, x, y, direction, value):
        validate_coords(x, y)
        q = {
            LEFT:  (self.v_walls, -1,  0),
            RIGHT: (self.v_walls,  0,  0),
            UP:    (self.h_walls,  0, -1),
            DOWN:  (self.h_walls,  0,  0),
        }
        matrix, xoffset, yoffset = q[direction]
        x_ = x + xoffset
        y_ = y + yoffset

        if 0 <= x_ and x_ < self.width-1 \
                and 0 <= y_ and y_ < self.height-1:
            matrix[y_][x_] = value

    def print():
        pass



class Game:
    pass

