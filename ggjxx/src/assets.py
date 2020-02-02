import pygame
from .game.constants import *


class Assets:
    def __init__(self):
        def load_tile(filename):
            s = pygame.image.load(filename).convert_alpha()
            s = pygame.transform.scale(s, (TILE_SIZE, TILE_SIZE))
            return s

        self.floor  = load_tile("assets/floor_2.png")
        self.wall_h = load_tile("assets/wall_horizontal.png")
        self.wall_v = load_tile("assets/wall_vertical.png")

        self.robot = {
            UP:    load_tile("assets/robot_radar_up.png"),
            DOWN:  load_tile("assets/robot_radar_down.png"),
            LEFT:  load_tile("assets/robot_radar_left.png"),
            RIGHT: load_tile("assets/robot_radar_right.png"),
        }

        self.robotg = {
            UP:    load_tile("assets/robot_reparador_up.png"),
            DOWN:  load_tile("assets/robot_reparador_down.png"),
            LEFT:  load_tile("assets/robot_reparador_left.png"),
            RIGHT: load_tile("assets/robot_reparador_right.png"),
        }

        self.robotr = {
            UP:    load_tile("assets/robot_cable_up.png"),
            DOWN:  load_tile("assets/robot_cable_down.png"),
            LEFT:  load_tile("assets/robot_tape_left.png"),
            RIGHT: load_tile("assets/robot_tape_right.png"),
        }

        self.fire       = load_tile("assets/cable_broken.png")
        self.fire_fixed = load_tile("assets/cable_fixed.png")
        self.pipe       = load_tile("assets/pipe_broken.png")
        self.pipe_fixed = load_tile("assets/pipe_fixed.png")

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
