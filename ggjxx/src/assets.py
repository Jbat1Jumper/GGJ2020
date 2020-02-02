import pygame
from .game.constants import *


class Assets:
    def __init__(self):
        self.floor = pygame.image.load("assets/floor_2.png")
        self.floor = pygame.transform.scale(self.floor, (TILE_SIZE, TILE_SIZE))

        self.wall_h = pygame.image.load("assets/wall_horizontal.png")
        sz = self.wall_h.get_size()
        self.wall_h = pygame.transform.scale(self.wall_h, (TILE_SIZE, TILE_SIZE))

        self.wall_v = pygame.image.load("assets/wall_vertical.png")
        sz = self.wall_v.get_size()
        self.wall_v = pygame.transform.scale(self.wall_v, (TILE_SIZE, TILE_SIZE))

        def load_robot_image(suffix, num):
            s = pygame.image.load("assets/placeholders/robot" + suffix + str(num) + ".png")
            s = pygame.transform.scale(s, (TILE_SIZE, TILE_SIZE))
            return s

        self.robot = {key: load_robot_image("", num) for (key, num) in [(UP, 1), (LEFT, 2), (DOWN, 3), (RIGHT, 4)]}
        self.robotg = {key: load_robot_image("g", num) for (key, num) in [(UP, 1), (LEFT, 2), (DOWN, 3), (RIGHT, 4)]}
        self.robotr = {key: load_robot_image("r", num) for (key, num) in [(UP, 1), (LEFT, 2), (DOWN, 3), (RIGHT, 4)]}

        self.fire = pygame.image.load("assets/cable_broken.png")
        self.fire = pygame.transform.scale(self.fire, (TILE_SIZE, TILE_SIZE))

        self.fire_fixed = pygame.image.load("assets/cable_fixed.png")
        self.fire_fixed = pygame.transform.scale(self.fire_fixed, (TILE_SIZE, TILE_SIZE))

        self.pipe = pygame.image.load("assets/pipe_broken.png")
        self.pipe = pygame.transform.scale(self.pipe, (TILE_SIZE, TILE_SIZE))

        self.pipe_fixed = pygame.image.load("assets/pipe_fixed.png")
        self.pipe_fixed = pygame.transform.scale(self.pipe_fixed, (TILE_SIZE, TILE_SIZE))

        self.light = self.load_animation("assets/placeholders/light#.png", 1, 5)

        self.puddle = self.load_animation("assets/floor_radioactive_goop.png", 1, 1)
        self.electricity = self.load_animation("assets/floor_electric_f#.png", 1, 2)

    def load_animation(self, filename, start, frames):
        sprites = []
        for i in range(start, start + frames):
            s = pygame.image.load(filename.replace("#", str(i))).convert_alpha()
            s = pygame.transform.scale(s, (TILE_SIZE, TILE_SIZE))
            sprites.append(s)
        return sprites
