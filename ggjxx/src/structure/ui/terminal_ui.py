import os
from .base_ui import BaseUI
from ...input.getch import _Getch
from ...game.game import Game
from ...game.map import Map
from ...game.constants import *
from ..action_constants import *
from ...robots.base_robot import BaseRobot

class TerminalUI(BaseUI):
    def __init__(self):
        pass

    def getInput(self):
        inkey = _Getch()
        key_pressed = inkey()
        if (key_pressed == UP_KEY_CHAR):
            return ACTION_GO_UP
        if (key_pressed == DOWN_KEY_CHAR):
            return ACTION_GO_DOWN
        if (key_pressed == RIGHT_KEY_CHAR):
            return ACTION_GO_RIGHT
        if (key_pressed == LEFT_KEY_CHAR):
            return ACTION_GO_LEFT
        if (key_pressed == CHANGE_ROBOT_KEY):
            return ACTION_ROTATE_ROBOT
        if (key_pressed == QUIT_KEY_CHAR):
            return ACTION_QUIT

    def clearScreen(self):
        clear = lambda: os.system('clear')
        clear()

    def render(self, game):
        # print()
        self.clearScreen()
        map = game.get_map()
        for y in range(map.getHeight()):
            lines = ['', '', '']
            for x in range(map.getWidth()):
                cell = map.getCell(x, y)
                cr = game.get_controlled_robot()
                robot = cr if cr.x == x and cr.y == y else None
                newLines = self.renderCell(cell, robot)
                lines[0] += newLines[0]
                lines[1] += newLines[1]
                lines[2] += newLines[2]
            lines[0] = lines[0].replace('\\/', '--')
            lines[0] = lines[0].replace('/\\', '--')
            lines[1] = lines[1].replace('\\/', '--')
            lines[1] = lines[1].replace('/\\', '--')
            lines[2] = lines[2].replace('\\/', '--')
            lines[2] = lines[2].replace('/\\', '--')
            print(lines[0])
            print(lines[1])
            print(lines[2])

    def renderCell(self, cell, robot):
        if cell.canGo(LEFT):
            if cell.canGo(UP):
                line1 = ' '
            else:
                line1 = '\\'
            line2 = ' '
            if cell.canGo(DOWN):
                line3 = ' '
            else:
                line3 = '/'
        else:
            if cell.canGo(UP):
                line1 = '|'
            else:
                line1 = '+'
            line2 = '|'
            if cell.canGo(DOWN):
                line3 = '|'
            else:
                line3 = '+'

        if cell.canGo(UP):
            line1 += '   '
        else:
            line1 += '---'

        if cell.canGo(DOWN):
            line3 += '   '
        else:
            line3 += '---'

        if (robot):
            line2 += robot.render()
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
            if cell.canGo(UP):
                line1 += ' '
            else:
                line1 += '/'
            line2 += ' '
            if cell.canGo(DOWN):
                line3 += ' '
            else:
                line3 += '\\'
        else:
            if cell.canGo(UP):
                line1 += '|'
            else:
                line1 += '+'
            line2 += '|'
            if cell.canGo(DOWN):
                line3 += '|'
            else:
                line3 += '+'

        return (line1, line2, line3)