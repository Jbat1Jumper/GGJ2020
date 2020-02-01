<<<<<<< HEAD
from ..game.game import Game, Map, Robot
from ..game.constants import UP_KEY_CHAR, DOWN_KEY_CHAR, RIGHT_KEY_CHAR, LEFT_KEY_CHAR
from ..input.getch import _Getch
=======
from ..game.game import Game, Map
from ..game.constants import UP,DOWN,LEFT,RIGHT
>>>>>>> 63d03c490bd15c222877e2ba22f4e8f86f0d7f5b

class Tui:

    def init(self):
        self.initGame()
        self.render()
        pass

    def run(self):
        while (not self.gameState.willShutdown()):
            self.updateGame()
        pass

    def teardown(self):
        pass

    def render(self):
        map = self.gameState.get_map()
        # robot = self.gameState.get_robot()
        for y in range(map.getHeight()):
            lines = ['', '', '']
            for x in range(map.getWidth()):
                cell = map.getCell(x, y)
                # newLines = self.renderCell(cell, robot.isInCell(x, y))
                cr = self.gameState.get_controlled_robot()
                robot = cr if cr.x == x and cr.y == y else None
                newLines = self.renderCell(cell, robot)
                lines[0] += newLines[0]
                lines[1] += newLines[1]
                lines[2] += newLines[2]
            print(lines[0])
            print(lines[1])
            print(lines[2])


    def renderCell(self, cell, isRobotInCell):
        if cell.canGo(UP):
            line1 = '     '
        else:
            line1 = ' --- '
        if cell.canGo(LEFT):
            line2 = ' '
        else:
            line2 = '|'
        if cell.canGo(DOWN):
            line3 = '     '
        else:
            line3 = ' --- '

        if (robot):
            line2 += 'X'
        else:
            line2 += ' '

        if (cell.hasFire()):
            line2 += 'F'
        else:
            line2 += ' '

        if (cell.hasRadiation()):
            line2 += 'R'
        else:
            line2 += ' '

        if cell.canGo(RIGHT):
            line2 += ' '
        else:
            line2 += '|'

        return (line1, line2, line3)

    def initGame(self):
        robots = [Robot(1, 2)]
        map = Map(4, 3, None, robots)
        map.get_cell(0,0).setAvailableDirections([DOWN])
        map.get_cell(0,1).setAvailableDirections([DOWN,UP])
        map.get_cell(0,2).setAvailableDirections([RIGHT,UP])
        map.get_cell(1,2).setAvailableDirections([RIGHT,LEFT])
        map.get_cell(2,2).setAvailableDirections([UP,LEFT])
        map.get_cell(2,1).setAvailableDirections([DOWN,LEFT,UP])
        map.get_cell(1,1).setAvailableDirections([RIGHT,UP])
        map.get_cell(1,0).setAvailableDirections([RIGHT,DOWN])
        map.get_cell(2,0).setAvailableDirections([LEFT,RIGHT,DOWN])
        map.get_cell(3,0).setAvailableDirections([LEFT])
        map.get_cell(3,1).setAvailableDirections([])
        map.get_cell(3,2).setAvailableDirections([])

        max_turns = 10
        self.gameState = Game(map, max_turns)
        self.gameState.choose_robot(robots[0])

    def updateGame(self):
        self.applyActionByInput()
        self.render()

    def applyActionByInput(self):
        inkey = _Getch()
        key_pressed = inkey()
        if (key_pressed == UP_KEY_CHAR):
            self.gameState.go_up()
        if (key_pressed == DOWN_KEY_CHAR):
            self.gameState.go_down()
        if (key_pressed == RIGHT_KEY_CHAR):
            self.gameState.go_right()
        if (key_pressed == LEFT_KEY_CHAR):
            self.gameState.go_left()

