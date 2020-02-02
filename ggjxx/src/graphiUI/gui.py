import sys, pygame
from ..game.constants import *
from ..TerminalUI.tui import Tui
from ..game.game import *

TILE_SIZE = 48
WALL_WIDTH = 16
WALL_VERTICAL_OFFSET = 8
SCREEN_SIZE = 640, 480


# dirty global
current_frame = 0

def frame(sprites):
    return sprites[int((current_frame/3)%len(sprites))]


class Assets:
    def __init__(self):
        self.floor = pygame.image.load("assets/placeholders/floor.png")
        self.floor = pygame.transform.scale(self.floor, (TILE_SIZE, TILE_SIZE))

        self.wall_h = pygame.image.load("assets/placeholders/wall_h.png")
        sz = self.wall_h.get_size()
        self.wall_h = pygame.transform.scale(self.wall_h, (TILE_SIZE, int(sz[1] * (TILE_SIZE/sz[0]))))

        self.wall_v = pygame.image.load("assets/placeholders/wall_v.png")
        sz = self.wall_v.get_size()
        self.wall_v = pygame.transform.scale(self.wall_v, (WALL_WIDTH, int(sz[1] * (WALL_WIDTH/sz[0]))))

        def load_robot_image(suffix, num):
            s = pygame.image.load("assets/placeholders/robot" + suffix + str(num) + ".png")
            s = pygame.transform.scale(s, (TILE_SIZE, TILE_SIZE))
            return s

        self.robot = {key: load_robot_image("", num) for (key, num) in [(UP, 1), (LEFT, 2), (DOWN, 3), (RIGHT, 4)]}
        self.robotg = {key: load_robot_image("g", num) for (key, num) in [(UP, 1), (LEFT, 2), (DOWN, 3), (RIGHT, 4)]}
        self.robotr = {key: load_robot_image("r", num) for (key, num) in [(UP, 1), (LEFT, 2), (DOWN, 3), (RIGHT, 4)]}

        self.fire = pygame.image.load("assets/placeholders/fire1.png")
        self.fire = pygame.transform.scale(self.fire, (TILE_SIZE, TILE_SIZE))

        self.fire_fixed = pygame.image.load("assets/placeholders/fire2.png")
        self.fire_fixed = pygame.transform.scale(self.fire_fixed, (TILE_SIZE, TILE_SIZE))

        self.pipe = pygame.image.load("assets/pipe_broken.png")
        self.pipe = pygame.transform.scale(self.pipe, (TILE_SIZE, TILE_SIZE))

        self.pipe_fixed = pygame.image.load("assets/pipe_fixed.png")
        self.pipe_fixed = pygame.transform.scale(self.pipe_fixed, (TILE_SIZE, TILE_SIZE))



        self.light = self.load_animation("assets/placeholders/light#.png", 5)

    def load_animation(self, filename, frames):
        sprites = []
        for i in range(frames):
            s = pygame.image.load(filename.replace("#", str(i+1)))
            s = pygame.transform.scale(s, (TILE_SIZE, TILE_SIZE))
            sprites.append(s)
        return sprites


class Gui:
    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.viewport = pygame.Rect(0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1])
        self.game = self.create_game()
        self.assets = Assets()
        self.clock = pygame.time.Clock()

    def create_game(self):
        tui = Tui()
        tui.initGame()
        return tui.gameState

    def run(self):
        while not self.game.won() or not self.game.lost():

            self.screen.fill((0, 0, 0))
            
            if self.game.is_robot_being_controlled():
                self.get_robot_input()
                self.draw_robot_phase()
            else:
                self.get_selection_input()
                self.draw_selection()
                
            pygame.display.flip()
            global current_frame
            current_frame += 1
            self.clock.tick(30)

    def get_robot_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("event quit")
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.unicode == UP_KEY_CHAR:
                    self.game.go_up()
                elif event.unicode == DOWN_KEY_CHAR:
                    self.game.go_down()
                elif event.unicode == RIGHT_KEY_CHAR:
                    self.game.go_right()
                elif event.unicode == LEFT_KEY_CHAR:
                    self.game.go_left()
                elif event.unicode == CHANGE_ROBOT_KEY:
                    self.game.switchControlledRobot()
                elif event.unicode == QUIT_KEY_CHAR:
                    print("key event quit")
                    sys.exit()
                else:
                    print("unknown key: " + event.unicode)

    def draw_robot_phase(self):
        self.draw_map()

    
    def draw_map(self):
        m = self.game.get_map()
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

            if isinstance(r, FireFighter):
                sprites = self.assets.robotr
            elif isinstance(r, RadiationFighter):
                sprites = self.assets.robotg
            else:
                sprites = self.assets.robot

            s = sprites[r.direction]

            self.screen.blit(s, (x * TILE_SIZE, y * TILE_SIZE))

            if r.is_being_controlled:
                self.screen.blit(frame(self.assets.light), (x*TILE_SIZE, y*TILE_SIZE))


    def get_selection_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def draw_selection(self):
        self.draw_robot()

    def teardown(self):
        pass
