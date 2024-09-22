# Screen settings
SCREEN_W = 1280
SCREEN_H = 768

# piece sizes
TILE_SIZE = 64 * 4
CHAR_SIZE = int(TILE_SIZE / 4)
MENU_WIDTH = SCREEN_W / 5
DIE_SIZE = 2*CHAR_SIZE

# font
TITLE_FONT_SIZE = 20
LIST_FONT_SIZE = 20
MSG_FONT_SIZE = 12
ROLLER_FONT_SIZE = int(DIE_SIZE / 4)
SPACE = 10
MENU_CHARS = 30 #number of characters that fit across menu

# window settings
TITLE = 'Betrayal at House on the Hill'

# colors
BG_COLOR = (8,25,14)
TRANSPARENCY = 0.8
PANEL_BKG = (31,31,31)
ROLLER_BKG = 'chocolate4'

# set positions
POSITIONS = {
    'char': (SPACE, SPACE), 
    'traits': (0, SPACE + CHAR_SIZE + SPACE*2),
    'msg': (0, TILE_SIZE),
    'name': (SPACE + CHAR_SIZE + SPACE, SPACE),
    'roller': (TILE_SIZE + 100, 100)
}

LAYERS = {
    'board': 0,
    'token': 1,
    'players': 2
}

INNATE_ROOMS = ['Entrance Hall', 'Hallway', 'Ground Floor Staircase', 'Basement Landing', 'Upper Landing']
