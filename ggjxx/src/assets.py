import pygame
from .game.constants import *


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
