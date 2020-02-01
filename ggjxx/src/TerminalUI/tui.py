from ..game.game import Game, Map
from ..game.constants import UP,DOWN,LEFT,RIGHT

class Tui:

    def init(self):
        self.initGame()
        self.render()
        pass

    def run(self):
        # while (!self.gameState.willShutdown()):
            # self.
        pass

    def teardown(self):
        pass

    def render(self):
        map = self.gameState.get_map()
        # robot = self.gameState.get_robot()
        for x in range(map.getHeight()):
            lines = ['', '', '']
            for y in range(map.getWidth()):
                cell = map.getCell(x, y)
                # newLines = self.renderCell(cell, robot.isInCell(x, y))
                newLines = self.renderCell(cell, False)
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

        if (isRobotInCell):
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
        map = Map(4, 3, None)
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
