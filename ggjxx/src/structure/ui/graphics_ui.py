import sys, pygame
from ...game.game import *
from ...game.constants import *
from ..action_constants import *
from .base_ui import BaseUI
from ...assets import Assets
from ...robots import *


class GraphicsUI(BaseUI):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.viewport = pygame.Rect(0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1])
        self.assets = Assets()
        self.clock = pygame.time.Clock()
        self.current_frame = 0
        pygame.display.set_caption('Robot Meltdown')

    def getInput(self):
        # if self.game.is_robot_being_controlled():
        return self.get_robot_input()
        # else:
        #     self.draw_selection()

    def render(self, game):
        self.screen.fill((0, 0, 0))

        if game.is_robot_being_controlled():
            self.draw_robot_phase(game)
        else:
            self.draw_selection()
            
        pygame.display.flip()
        self.current_frame += 1
        self.clock.tick(30)

    def get_robot_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("event quit")
                sys.exit()
                return ACTION_QUIT
            elif event.type == pygame.KEYDOWN:
                if event.unicode == UP_KEY_CHAR:
                    return ACTION_GO_UP
                elif event.unicode == DOWN_KEY_CHAR:
                    return ACTION_GO_DOWN
                elif event.unicode == RIGHT_KEY_CHAR:
                    return ACTION_GO_RIGHT
                elif event.unicode == LEFT_KEY_CHAR:
                    return ACTION_GO_LEFT
                elif event.unicode == CHANGE_ROBOT_KEY:
                    return ACTION_ROTATE_ROBOT
                elif event.unicode == QUIT_KEY_CHAR:
                    return ACTION_QUIT
                else:
                    print("unknown key: " + event.unicode)

    def draw_robot_phase(self, game):
        m = game.get_map()
        self.draw_turns_left(game)
        self.draw_map(m)

    def draw_map(self, m):
        for y in range(m.height):
            for x in range(m.width):
                # floor
                self.screen.blit(self.assets.floor, (x * TILE_SIZE, y * TILE_SIZE))

        for y in range(m.height):
            for x in range(m.width):
                c = m.get_cell(x, y)
                self.draw_walls(c, x, y)
                self.draw_hazards(c, x, y)
                self.draw_robot(c, x, y, m.get_robots())

    def draw_turns_left(self, game):

        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)
        black = (0, 0, 0)

        display_surface = self.screen


        font = pygame.font.Font('freesansbold.ttf', 28)

        text = font.render('Turnos: ' + str(game.turns_left), True, white, black)

        textRect = text.get_rect()

        textRect.center = (game.get_map().width * TILE_SIZE + 100, 50)

        display_surface.blit(text, textRect)





    def draw_walls(self, cell, x, y):
        if x == 0:
            self.screen.blit(self.assets.wall_v, (x * TILE_SIZE - WALL_WIDTH/2, y * TILE_SIZE - WALL_VERTICAL_OFFSET))
        if y == 0:
            self.screen.blit(self.assets.wall_h, (x * TILE_SIZE - WALL_WIDTH/2, y * TILE_SIZE - WALL_VERTICAL_OFFSET))
        if not cell.canGo(RIGHT):
            self.screen.blit(self.assets.wall_v, ((x+1) * TILE_SIZE - WALL_WIDTH/2, y * TILE_SIZE - WALL_VERTICAL_OFFSET))
        if not cell.canGo(DOWN):
            self.screen.blit(self.assets.wall_h, (x * TILE_SIZE - WALL_WIDTH/2, (y+1) * TILE_SIZE - WALL_VERTICAL_OFFSET))
        
    def draw_hazards(self, cell, x, y):

        if cell.hasRadiation():
            self.screen.blit(self.assets.pipe, (x * TILE_SIZE, y * TILE_SIZE))
        elif cell.hadRadiation:
            self.screen.blit(self.assets.pipe_fixed, (x * TILE_SIZE, y * TILE_SIZE))
        
        if cell.hasFire():
            self.screen.blit(self.assets.fire, (x * TILE_SIZE, y * TILE_SIZE))
        elif cell.hadFire:
            self.screen.blit(self.assets.fire_fixed, (x * TILE_SIZE, y * TILE_SIZE))

    def draw_robot(self, cell, x, y, robots):
        robots_at_this_position = [r for r in robots if r.x == x and r.y == y]
        if not robots_at_this_position:
            return

        for r in robots_at_this_position:

            if isinstance(r, FireFighterRobot):
                sprites = self.assets.robotr
            elif isinstance(r, RadiationFighterRobot):
                sprites = self.assets.robotg
            else:
                sprites = self.assets.robot

            s = sprites[r.direction]

            self.screen.blit(s, (x * TILE_SIZE, y * TILE_SIZE))

            if r.is_being_controlled:
                self.screen.blit(self.frame(self.assets.light), (x*TILE_SIZE, y*TILE_SIZE))


    def get_selection_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def draw_selection(self):
        self.draw_map()

    def frame(self, sprites):
        return sprites[int((self.current_frame/3)%len(sprites))]

    def teardown(self):
        pass