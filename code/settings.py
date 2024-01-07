# Screen settings
SCREEN_W = 1280
SCREEN_H = 768

# piece sizes
TILE_SIZE = 64 * 4
CHAR_SIZE = int(TILE_SIZE / 4)

# window settings
TITLE = 'Betrayal at House on the Hill'
BG_COLOR = 'pink'
TRANSPARENCY = 0.8

# overlay positions
OVERLAY_POSITIONS = {
    'char': (40, SCREEN_H - 15)
}

LAYERS = {
    'board': 0,
    'token': 1,
    'players': 2
}

INNATE_ROOMS = ['Entrance Hall', 'Hallway', 'Ground Floor Staircase', 'Basement Landing', 'Upper Landing']
