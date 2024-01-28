# Screen settings
SCREEN_W = 1280
SCREEN_H = 768

# piece sizes
TILE_SIZE = 64 * 4
CHAR_SIZE = int(TILE_SIZE / 4)
MENU_WIDTH = SCREEN_W / 5

# font
TITLE_FONT_SIZE = 20
LIST_FONT_SIZE = 20
MSG_FONT_SIZE = 12
SPACE = 10
MENU_CHARS = 30 #number of characters that fit across menu

# window settings
TITLE = 'Betrayal at House on the Hill'
BG_COLOR = 'pink'

TRANSPARENCY = 0.8
PANEL_BKG = (31,31,31)

# overlay positions
OVERLAY_POSITIONS = {
    'char': (SPACE, SPACE), 
    'traits': (0, SPACE + CHAR_SIZE + SPACE*2),
    'msg': (0, TILE_SIZE),
    'name': (SPACE + CHAR_SIZE + SPACE, SPACE)
}

LAYERS = {
    'board': 0,
    'token': 1,
    'players': 2
}

INNATE_ROOMS = ['Entrance Hall', 'Hallway', 'Ground Floor Staircase', 'Basement Landing', 'Upper Landing']
