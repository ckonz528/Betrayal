import pygame
import settings as s
from decks import Deck, RoomDeck
from rooms import Room
from explorers import Explorer
from timer import Timer


class Gameboard:
    def __init__(self):

        # get the display surface
        self.display_surf = pygame.display.get_surface()

        # sprite groups (to draw and update sprites)
        self.all_sprites = CameraGroup()

        self.setup()

    def setup(self):
        # Grid
        self.grid = {}

        # Room deck
        self.room_deck = RoomDeck('../data/rooms.json', 'room')

        # place starting room tiles
        self.place_tile('Ground Floor Staircase', (-2, 0))
        self.place_tile('Hallway', (-1, 0))
        self.place_tile('Entrance Hall', (0,0))
        self.place_tile('Upper Landing', (100,0))
        self.place_tile('Basement Landing', (-100,0))

        # TODO: dynamically choose the floor
        tile = self.room_deck.choose_card(floor="ground")  # test
        self.place_tile(tile.name,(0,-1)) # test

        # Card decks
        self.omen_deck = Deck('../data/omens.json', 'object')
        self.item_deck = Deck('../data/items.json', 'object')
        self.event_deck = Deck('../data/events.json', 'event')
        self.char_list = Deck('../data/characters.json', 'explorer')

        # Players
        # TODO: set up ability for players to select characters
        # TODO: make list of players and cycle through them
        self.player = self.char_list.obj_dict['Persephone Puleri'] # test
        self.player.init_player((0,0), self.all_sprites) # test

        # Timers
        self.timers = {
            'player_move': Timer(300)
        }

    def place_tile(self, tile_name: str, grid_pos: tuple):
        tile = self.room_deck.get_obj_by_name(tile_name)
        tile.set_pos(grid_pos)
        self.grid[grid_pos] = tile.name
        self.all_sprites.add(tile)
        print(tile.name)  # test

    def player_input(self,):
        keys = pygame.key.get_pressed()

        if not self.timers['player_move'].active:
            player_pos = self.player.grid_pos
            if keys[pygame.K_UP]:
                self.timers['player_move'].activate()
                if self.check_walls('N'):
                    self.player.set_pos((player_pos[0], player_pos[1] - 1))
                
            elif keys[pygame.K_DOWN]:
                self.timers['player_move'].activate()
                if self.check_walls('S'):
                    self.player.set_pos((player_pos[0], player_pos[1] + 1))

            elif keys[pygame.K_LEFT]:
                self.timers['player_move'].activate()
                if self.check_walls('W'):
                    self.player.set_pos((player_pos[0] - 1, player_pos[1]))

            elif keys[pygame.K_RIGHT]:
                self.timers['player_move'].activate()
                if self.check_walls('E'):
                    self.player.set_pos((player_pos[0] + 1, player_pos[1]))

    def check_walls(self, direction: str):
        # Check for walls in current tile
        room_name = self.grid[self.player.grid_pos]
        doors = self.room_deck.obj_dict[room_name].doors

        if direction == 'N':
            if not doors[0]:
                print(f'{room_name} {direction} blocked')
                return False
        elif direction == 'E':
            if not doors[1]:
                print(f'{room_name} {direction} blocked')
                return False
        elif direction == 'S':
            if not doors[2]:
                print(f'{room_name} {direction} blocked')
                return False
        elif direction == 'W':
            if not doors[3]:
                print(f'{room_name} {direction} blocked')
                return False
            
        # check for adjacent tile & walls
        if direction == 'N':
            target_pos = (self.player.grid_pos[0], self.player.grid_pos[1] - 1)
            print(f'Target pos: {target_pos}')
            if target_pos in self.grid.keys():
                target_room_name = self.grid[target_pos]
                target_doors = self.room_deck.obj_dict[target_room_name].doors
                if not target_doors[2]:
                    print(f'Movement blocked by {target_room_name}; doors = {target_doors}')
                    return False
            else:
                print(f'No tile {direction} of {room_name}')
                return False
        elif direction == 'E':
            target_pos = (self.player.grid_pos[0] - 1, self.player.grid_pos[1])
            print(f'Target pos: {target_pos}')
            if target_pos in self.grid.keys():
                target_room_name = self.grid[target_pos]
                target_doors = self.room_deck.obj_dict[target_room_name].doors
                if not target_doors[1]:
                    print(f'Movement blocked by {target_room_name}; doors = {target_doors}')
                    return False
            else:
                print(f'No tile {direction} of {room_name}')
                return False
        elif direction == 'S':
            target_pos = (self.player.grid_pos[0], self.player.grid_pos[1] + 1)
            print(f'Target pos: {target_pos}')
            if target_pos in self.grid.keys():
                target_room_name = self.grid[target_pos]
                target_doors = self.room_deck.obj_dict[target_room_name].doors
                if not target_doors[0]:
                    print(f'Movement blocked by {target_room_name}; doors = {target_doors}')
                    return False
            else:
                print(f'No tile {direction} of {room_name}')
                return False
        elif direction == 'W':
            target_pos = (self.player.grid_pos[0] + 1, self.player.grid_pos[1])
            print(f'Target pos: {target_pos}')
            if target_pos in self.grid.keys():
                target_room_name = self.grid[target_pos]
                target_doors = self.room_deck.obj_dict[target_room_name].doors
                if not target_doors[3]:
                    print(f'Movement blocked by {target_room_name}; doors = {target_doors}')
                    return False
            else:
                print(f'No tile {direction} of {room_name}')
                return False

        return True

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def run(self, dt):
        # drawing logic
        self.display_surf.fill(s.BG_COLOR)  # background
        self.player_input()
        self.update_timers()
        self.all_sprites.custom_draw()
        self.all_sprites.update(dt)


class CameraGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2((-3 * s.TILE_SIZE, -s.TILE_SIZE))  # offsets the map to move player

        # camera speed
        self.keyboard_speed = 3
    
    def keyboard_ctrl(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.offset.x -= self.keyboard_speed
        if keys[pygame.K_d]:
            self.offset.x += self.keyboard_speed
        if keys[pygame.K_w]:
            self.offset.y -= self.keyboard_speed
        if keys[pygame.K_s]:
            self.offset.y += self.keyboard_speed

        # TODO: set up to snap camera to player position
        # snap camera to original position
        if keys[pygame.K_g]: # ground floor (Entrance Hall)
            self.set_camera(pygame.math.Vector2((-3 * s.TILE_SIZE, -s.TILE_SIZE)))
        elif keys[pygame.K_u]: # upper landing
            self.set_camera(pygame.math.Vector2((98 * s.TILE_SIZE, -s.TILE_SIZE)))
        elif keys[pygame.K_b]: # basement landing
            self.set_camera(pygame.math.Vector2((-102 * s.TILE_SIZE, -s.TILE_SIZE)))

    def custom_draw(self):
        self.keyboard_ctrl()
        # TODO: Add box that moves with player camera

        # cycle through layers dict and draw layers in order
        for layer in s.LAYERS.values():
            for sprite in self.sprites():
                if sprite.layer == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)

    def set_camera(self, set_pos):
        # TODO: set up to snap camera to other positions
        self.offset = set_pos
