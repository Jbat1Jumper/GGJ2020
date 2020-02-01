from ..game.game import Game, Map

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
                newLines = self.renderCell(cell, True)
                lines[0] += newLines[0]
                lines[1] += newLines[1]
                lines[2] += newLines[2]
            print(lines[0])
            print(lines[1])
            print(lines[2])

    def renderCell(self, cell, isRobotInCell):
        line1 = ' --- '
        line2 = '|'
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

        line2 += '|'

        return (line1, line2, line3)

    def initGame(self):
        map = Map(15, 5)
        max_turns = 10
        self.gameState = Game(map, max_turns)
