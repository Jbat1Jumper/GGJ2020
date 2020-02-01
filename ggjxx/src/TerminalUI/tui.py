class Tui:

    def init(self):
        self.gameState = Game()
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
        robot = self.gameState.get_robot()
        for x in xrange(1, map.getHeight()):
            lines = ('', '', '')
            for y in xrange(1, map.getWidth()):
                cell = map.getCell(x, y)
                newLines = self.renderCell(cell, robot.isInCell(x, y))
                lines[0].append(newLines[0])
                lines[1].append(newLines[1])
                lines[2].append(newLines[2])
            print(lines[0])
            print(lines[1])
            print(lines[2])

    def renderCell(self, cell, isRobotInCell):
        line1 = ' --- '
        line2 = '|'
        line3 = ' --- '

        if (isRobotInCell):
            line2.append('R')
        else:
            line2.append('*')

        if (cell.hasFire()):
            line2.append('F')
        else:
            line2.append('*')

        if (cell.hasRadiation()):
            line2.append('R')
        else:
            line2.append('*')

        line2.append('|')

        return (line1, line2, line3)

