from .cell import Cell
from .constants import UP,DOWN,RIGHT,LEFT

class Map:
    def __init__(self, w, h, robots):
        self.width = w
        self.height = h
        self.robots = robots
        self.cells = [[Cell() for _ in range(w)] for _ in range(h)]

    def get_robots(self):
        return self.robots

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def getCell(self, x, y):
        return self.cells[y][x]

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

    def has_wall(self, x, y, direction):
        self.validate_coords(x, y)
        q = {
            LEFT: lambda: True if x == 0 else self.v_valls[y][x-1],
            RIGHT: lambda: True if x == self.width-1 else self.v_valls[y][x],
            UP: lambda: True if y == 0 else self.h_valls[y-1][x],
            DOWN: lambda: True if y == self.height-1 else self.v_valls[y][x],
        }
        return q[direction]()

    def set_wall(self, x, y, direction, value):
        self.validate_coords(x, y)
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
    def __init__(self, map_, max_turns):
        self.map = map_
        self.turns_left = max_turns
        self.controlled_robot = None

    # def get_robot():
        # return 

    def get_map(self):
        return self.map

    def get_controlled_robot(self):
        return self.controlled_robot
    
    def won(self):
        # check win condition
        return False

    def lost(self):
        return self.turns_left > 0

    def available_robots(self):
        return filter(lambda r: not r.busy, self.map.get_robots())

    def choose_robot(self, robot):
        self.choose_robot = robot

    def is_robot_being_controlled(self):
        return self.controlled_robot != None

    def go_left(self):
        if not self.is_robot_being_controlled():
            return

        r = self.controlled_robot
        if self.map.getCell(r.x, r.y).canGo(LEFT):
            r.x -= 1

    def go_right(self):
        if not self.is_robot_being_controlled():
            return

        r = self.controlled_robot
        if self.map.getCell(r.x, r.y).canGo(RIGHT):
            r.x += 1

    def go_down(self):
        if not self.is_robot_being_controlled():
            return

        r = self.controlled_robot
        if self.map.getCell(r.x, r.y).canGo(DOWN):
            r.y += 1

    def go_up(self):
        if not self.is_robot_being_controlled():
            return

        r = self.controlled_robot
        if self.map.getCell(r.x, r.y).canGo(UP):
            r.y += 1

    def robot_action(self):
        pass

    def end_turn(self):
        self.turns_left -= 1
        self.controlled_robot = None


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = '_'
        self.busy = False

    def action(self, map):
        pass

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, _x):
        self.x = _x

    def setY(self, _y):
        self.y = _y