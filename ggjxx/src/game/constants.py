
UP    = "UP"
DOWN  = "DOWN"
LEFT  = "LEFT"
RIGHT = "RIGHT"

# UP_KEY_CHAR = '\x1b[A'
# DOWN_KEY_CHAR = '\x1b[B'
# RIGHT_KEY_CHAR = '\x1b[C'
# LEFT_KEY_CHAR = '\x1b[D'

UP_KEY_CHAR = 'w'
DOWN_KEY_CHAR = 's'
RIGHT_KEY_CHAR = 'd'
LEFT_KEY_CHAR = 'a'
CHANGE_ROBOT_KEY = ' '
RESTART_KEY_CHAR = 'r'

# QUIT_KEY_CHAR = ord('q')
QUIT_KEY_CHAR = 'q'


# Tamaños de assets
TILE_SIZE = 48
WALL_WIDTH = 16
SCREEN_SIZE = 640, 480

class WallOffsets:
    WALL_V_Y_OFFSET = -3
    WALL_V_X_OFFSET = 23
    WALL_H_Y_OFFSET = 28
    WALL_H_X_OFFSET = 0


# Eventos
MOVEMENT_NOT_ALLOWED = "MOVEMENT_NOT_ALLOWED"
MOVEMENT_DONE = "MOVEMENT_DONE"
KILL_ROBOT = "KILL_ROBOT"
