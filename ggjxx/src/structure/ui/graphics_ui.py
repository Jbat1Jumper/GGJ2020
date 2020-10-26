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

        self.wait_for_exit = False
        self.should_terminate = False

    def getInput(self):
        if self.wait_for_exit:
            return self.get_dialog_input()
        return self.get_robot_input()

    def render(self, game):
        self.screen.fill((0, 0, 0))

        if game.is_robot_being_controlled():
            self.draw_robot_phase(game)
        else:
            self.draw_selection()

        if self.wait_for_exit:
            self.draw_confirmation_dialog(game)
            
        pygame.display.flip()
        self.current_frame += 1
        self.clock.tick(30)

    def applyAction(self, action):
        if action == ACTION_QUIT:
            self.wait_for_exit = True
            return True

        if action == ACTION_DIALOG_CONFIRM:
            self.should_terminate = True
            return True

        if action == ACTION_DIALOG_CANCEL:
            self.wait_for_exit = False
            return True

    def get_dialog_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.unicode == CHANGE_ROBOT_KEY:
                    return ACTION_DIALOG_CONFIRM
                if event.unicode == QUIT_KEY_CHAR:
                    return ACTION_DIALOG_CANCEL

    def get_robot_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
                elif event.unicode == RESTART_KEY_CHAR:
                    return ACTION_RESTART

                elif event.unicode == 'u':
                    print (WallOffsets.WALL_V_X_OFFSET)
                    WallOffsets.WALL_V_X_OFFSET += 1
                elif event.unicode == 'j':
                    print (WallOffsets.WALL_V_X_OFFSET)
                    WallOffsets.WALL_V_X_OFFSET -= 1
                elif event.unicode == 'i':
                    print (WallOffsets.WALL_V_Y_OFFSET)
                    WallOffsets.WALL_V_Y_OFFSET += 1
                elif event.unicode == 'k':
                    print (WallOffsets.WALL_V_Y_OFFSET)
                    WallOffsets.WALL_V_Y_OFFSET -= 1

                elif event.unicode == 'o':
                    print (WallOffsets.WALL_H_X_OFFSET)
                    WallOffsets.WALL_H_X_OFFSET += 1
                elif event.unicode == 'l':
                    print (WallOffsets.WALL_H_X_OFFSET)
                    WallOffsets.WALL_H_X_OFFSET -= 1
                elif event.unicode == 'p':
                    print (WallOffsets.WALL_H_Y_OFFSET)
                    WallOffsets.WALL_H_Y_OFFSET += 1
                elif event.unicode == ';':
                    print (WallOffsets.WALL_H_Y_OFFSET)
                    WallOffsets.WALL_H_Y_OFFSET -= 1
                else:
                    print("unknown key: " + event.unicode)
                sys.stdout.flush()

    def draw_robot_phase(self, game):
        self.draw_turns_left(game)
        if game.finished():
            self.draw_game_finished(game)
        self.draw_map(game)
    
    def draw_map(self, game):
        m = game.get_map()
        for y in range(m.height):
            for x in range(m.width):
                # floor
                self.screen.blit(self.assets.floor, (x * TILE_SIZE, y * TILE_SIZE))

        for y in range(m.height):
            for x in range(m.width):
                c = m.get_cell(x, y)
                if c.hasFog():
                    self.draw_fog(c, x, y)
                else:
                    self.draw_hazards(c, x, y, game)
                    self.draw_robot(c, x, y, m.get_robots())
                    self.draw_walls(c, x, y)

    def draw_turns_left(self, game):
        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)
        black = (0, 0, 0)

        display_surface = self.screen
        font = self.assets.font
        text = font.render('Turnos: ' + str(game.turns_left), True, white, black)
        textRect = text.get_rect()
        textRect.center = (game.get_map().width * TILE_SIZE + 100, 50)
        display_surface.blit(text, textRect)

    def draw_game_finished(self,game):
        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)
        black = (0, 0, 0)

        display_surface = self.screen
        font = self.assets.font
        text = "Has ganado" if game.won() else "LoSeR"
        text = font.render(text, True, white, black)
        textRect = text.get_rect()
        textRect.center = (game.get_map().width * TILE_SIZE + 100, 100)
        display_surface.blit(text, textRect)



    def draw_walls(self, cell, x, y):
        if x == 0:
            self.screen.blit(self.assets.wall_v, (x * TILE_SIZE - WallOffsets.WALL_V_X_OFFSET, y * TILE_SIZE - WallOffsets.WALL_V_Y_OFFSET))
        if y == 0:
            self.screen.blit(self.assets.wall_h, (x * TILE_SIZE - WallOffsets.WALL_H_X_OFFSET, y * TILE_SIZE - WallOffsets.WALL_H_Y_OFFSET))
        if not cell.canGo(RIGHT):
            self.screen.blit(self.assets.wall_v, ((x+1) * TILE_SIZE - WallOffsets.WALL_V_X_OFFSET, y * TILE_SIZE - WallOffsets.WALL_V_Y_OFFSET))
        if not cell.canGo(DOWN):
            self.screen.blit(self.assets.wall_h, (x * TILE_SIZE - WallOffsets.WALL_H_X_OFFSET, (y+1) * TILE_SIZE - WallOffsets.WALL_H_Y_OFFSET))
        
    def draw_hazards(self, cell, x, y, game):

        adjacent_cells = game.getAdjacentCells(x, y)

        if [c for c in adjacent_cells if c.hasRadiation()]:
            self.screen.blit(self.frame(self.assets.puddle), (x * TILE_SIZE, y * TILE_SIZE))

        if [c for c in adjacent_cells if c.hasFire()]:
            self.screen.blit(self.frame(self.assets.electricity), (x * TILE_SIZE, y * TILE_SIZE))

        if cell.hasReactor() and cell.reactorIsFaulty():
            self.screen.blit(self.assets.reactor, (x * TILE_SIZE, y * TILE_SIZE))
        elif cell.hasReactor() and not cell.reactorIsFaulty():
            self.screen.blit(self.assets.reactor_fixed, (x * TILE_SIZE, y * TILE_SIZE))
        else:
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

    def draw_fog(self, cell, x, y):
        rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(self.screen, [0, 0, 0], rect)

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

    def draw_confirmation_dialog(self, game):
        white = (255, 255, 255)
        gray = (90, 90, 90)
        black = (0, 0, 0)

        display_surface = self.screen
        font = self.assets.font
        text = font.render('Presione espacio para salir', True, white, black)
        textRect = text.get_rect()
        textRect.center = (self.viewport.width / 2, self.viewport.height / 2)
        backgroundRect = textRect.inflate(1, 3)
        display_surface.fill(gray, backgroundRect)
        display_surface.blit(text, textRect)

    def shouldTerminate(self, game):
        return self.wait_for_exit and self.should_terminate