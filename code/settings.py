# Screen settings
SCREEN_W = 1280
SCREEN_H = 768

# window settings
TITLE = 'Betrayal at House on the Hill'

# font sizes
TITLE_FONT_SIZE = 20
LIST_FONT_SIZE = 20
MSG_FONT_SIZE = 12
INFO_FONT_SIZE = 16
ROLLER_FONT_SIZE = TITLE_FONT_SIZE * 2
EVENT_TITLE_SIZE = 30
EVENT_TEXT_SIZE = 20

# other font settings
SPACE = 10
MARGIN = 16
MENU_CHARS = 30 # number of characters that fit across menu
LINE_SPACE = 8

# piece sizes
TILE_SIZE = 64 * 4
CHAR_SIZE = int(TILE_SIZE / 4)
DIE_SIZE = 2*CHAR_SIZE
PORTRAIT_SIZE = (96, 120)

# panel & pop up sizes
PANEL_WIDTH = SCREEN_W / 5
POPUP_WIDTH = SCREEN_W - TILE_SIZE - 200
POPUP_HEIGHT = SCREEN_H - 200

# color values
DKGREEN = (16, 41,0) # Pakistan green 102900
DKGRAY = (31,31,31) # Eerie black 1F1F1F
BROWN = (122,68,25) # Russet 7A4419
# DKRED = (64,4,6) # Black bean 400406
# DKRED = (142, 4, 2) # 8e0402
DKRED = (110, 24, 37)
GOLD_YELLOW = (200,150,62) # Satin sheen gold C8963E
DKBLUE = (64, 88, 108) # Paynes Gray 40586C
# DKGOLD = (161, 136, 37) # Dark goldenrod A18825
DKGOLD = (134, 98, 0) # 866200
LTGRAY = (94, 95, 94) # Davy's gray 5e5f5e
DKPURPLE = (60, 45, 65) # Dark purple 3c2d41
MOSS = (37, 93, 4) # 255D04

# color settings
BG_COLOR = DKGREEN
PANEL_BKG = DKGRAY
ROLLER_BKG = BROWN
EVENT_BKG = DKRED
TRANSPARENCY = 0.8

PANEL_COLORS = {'Blue': DKBLUE,
                'Yellow': DKGOLD,
                'Red': DKRED,
                'White': LTGRAY,
                'Purple': DKPURPLE,
                'Green': MOSS}

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
