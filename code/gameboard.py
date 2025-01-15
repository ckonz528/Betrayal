import pygame
import settings as s
from decks import Deck, RoomDeck
from rooms import Room
from explorers import Explorer
from timer import Timer
from overlay import Overlay
from inventory import Inventory
from roller import Roller
from event import Event
from messenger import Messenger
from start_screen import StartScreen
from character_select import Selector


class Gameboard:
    def __init__(self):

        # get the display surface
        self.display_surf = pygame.display.get_surface()

        # sprite groups (to draw and update sprites)
        self.all_sprites = CameraGroup()
        self.messenger = Messenger()

        self.setup()

    def setup(self):
        # Grid
        self.grid = {}

        # Room deck
        self.room_deck = RoomDeck('../data/rooms.json', 'room', self.messenger)

        # place starting room tiles
        self.place_tile('Ground Floor Staircase', (-2, 0))
        self.place_tile('Hallway', (-1, 0))
        self.place_tile('Entrance Hall', (0,0))
        self.place_tile('Upper Landing', (100,0))
        self.place_tile('Basement Landing', (-100,0))

        # Card decks
        self.omen_deck = Deck('../data/omens.json', 'object', obj_type='omen')
        self.item_deck = Deck('../data/items.json', 'object', obj_type='item')
        self.event_deck = Deck('../data/events.json', 'event')
        self.char_deck = Deck('../data/characters.json', 'explorer')

        # Players
        # TODO: set up ability for players to select characters
        self.selector = Selector(self.char_deck)

        # TODO: make list of players and cycle through them
        self.players = []
        self.turn_index = 0
        self.add_player('Persephone Puleri')
        self.add_player('Isa Valencia')

        current_player_name = self.players[self.turn_index]
        self.current_player = self.char_deck.obj_dict[f'{current_player_name}']
        self.current_player.allow_move = True

        # Timers
        self.timers = {
            'player_move': Timer(300),
            'inv_panel': Timer(),
            'roller': Timer(),
            'game_play': Timer()
        }

        # overlay
        self.overlay = Overlay()

        # inventory panel
        self.inventory_panel = Inventory()
        self.inventory_active = False

        # pop up windows
        self.roller = Roller()
        self.roller_active = False
        self.event = Event()
        self.event_active = False

        self.messenger.clear_queue()

        self.start_screen = StartScreen()
        self.game_state = "start" # options: start, select, play

    def add_player(self, char_name: str):
        chosen_player = self.char_deck.obj_dict[f'{char_name}']
        chosen_player.set_pos((0,0))
        self.all_sprites.add(chosen_player)
        self.players.append(char_name)
        self.messenger.add_entry(f'{chosen_player.name} added to player list')

    def place_tile(self, tile_name: str, grid_pos: tuple, direction:str = 'N'):
        tile = self.room_deck.get_obj_by_name(tile_name)
        self.recent_room = tile

        # add tile to grid
        tile.set_pos(grid_pos, direction)
        self.grid[grid_pos] = tile.name
        self.all_sprites.add(tile)
        self.messenger.add_entry(f'Discovered: {tile.name}', 'green')

        # draw designated card
        self.draw_tile_card(tile.card)

    def draw_tile_card(self, card_type: str):
        if card_type == "none":
            self.messenger.add_entry('No cards drawn for this tile')
        elif card_type == 'omen':
            card_obj = self.omen_deck.choose_card()
            self.current_player.add_item(card_obj)
            self.messenger.add_entry(f'Omen: {card_obj.name}')
        elif card_type == 'item':
            card_obj = self.item_deck.choose_card()
            self.current_player.add_item(card_obj)
            self.messenger.add_entry(f'Item: {card_obj.name}')
        elif card_type == 'event':
            card_obj = self.event_deck.choose_card()
            self.messenger.add_entry(f'Event: {card_obj.name}')
            #TODO: settle room rotation before event starts
            self.event_active = True
            self.event.run_event(card_obj)

    def end_turn(self):
        # check last placed tile rotation
        if self.recent_room.rotation_check(): # if rotation check is invalid
            # stop room rotation
            self.recent_room.stop_rotation()

            # switch turn to next player
            self.messenger.add_entry(f'Turn ended for {self.current_player.name}')
            self.turn_index += 1
            if self.turn_index >= len(self.players):
                self.turn_index = 0

            current_player_name = self.players[self.turn_index]
            self.current_player = self.char_deck.obj_dict[current_player_name]
            self.messenger.add_entry(f"{self.current_player.name}'s turn")
            self.current_player.allow_move = True


        #TODO: center camera on next player 
        # self.all_sprites.set_camera(pygame.math.Vector2((self.current_player.rect.centerx + s.SCREEN_W / 2, self.current_player.rect.centery + s.SCREEN_H / 2)))

    def adjust_tokens(self):
        directions = ['NW','N','NE','E','SE','S','SW','W']
        adjust_counter = 0
        for token in self.players:
            token = self.char_deck.obj_dict[token]
            if token.name != self.current_player.name and token.grid_pos == self.current_player.grid_pos:
                token.adjust_pos(directions[adjust_counter])
                adjust_counter += 1

    def player_input(self):
        keys = pygame.key.get_pressed()

        # start screen
        if self.game_state == "start":
            if keys[pygame.K_SPACE]:
                self.timers['game_play'].activate()
                self.game_state = "select"
                print(f'after start screen: {self.game_state}')

        # character selection
        elif self.game_state == "select" and not(self.timers['game_play'].active):
            print(f'game state: {self.game_state}')
            if keys[pygame.K_SPACE]:
                self.game_state = "play"
                print(f'after selection: {self.game_state}')

        # game play
        else:
            move_criteria = [
                not self.timers['player_move'].active,
                self.current_player.allow_move,
                not self.inventory_active
            ]

            # player movement
            if all(move_criteria):
                player_pos = self.current_player.grid_pos
                if keys[pygame.K_UP]:
                    self.timers['player_move'].activate()
                    if self.check_walls('N'):
                        self.current_player.set_pos((player_pos[0], player_pos[1] - 1))                
                elif keys[pygame.K_DOWN]:
                    self.timers['player_move'].activate()
                    if self.check_walls('S'):
                        self.current_player.set_pos((player_pos[0], player_pos[1] + 1))
                elif keys[pygame.K_LEFT]:
                    self.timers['player_move'].activate()
                    if self.check_walls('W'):
                        if self.current_player.grid_pos == self.room_deck.obj_dict['Ground Floor Staircase'].grid_pos:
                            self.current_player.set_pos(self.room_deck.obj_dict['Upper Landing'].grid_pos)
                            self.current_player.floor = 'upper'
                        else:
                            self.current_player.set_pos((player_pos[0] - 1, player_pos[1]))
                elif keys[pygame.K_RIGHT]:
                    self.timers['player_move'].activate()
                    if self.check_walls('E'):
                        self.current_player.set_pos((player_pos[0] + 1, player_pos[1]))

            self.adjust_tokens()

            # inventory panel toggle
            if not self.timers['inv_panel'].active:
                if keys[pygame.K_i]:
                    self.timers['inv_panel'].activate()
                    self.inventory_active = not self.inventory_active

            # roller toggle
            if not self.timers['roller'].active:
                #TODO: activate roller automatically / keep roller from activating during events
                if keys[pygame.K_r]:
                    self.timers['roller'].activate()
                    self.roller.dice_rolled = False
                    self.roller_active = not self.roller_active

            # event window
            if self.event_active:
                if keys[pygame.K_RETURN]:
                    self.event_active = False

            # end turn
            if not self.timers['player_move'].active and keys[pygame.K_e]:
                self.timers['player_move'].activate()
                self.end_turn()

    def check_walls(self, direction: str):
        # Check for walls in current tile
        room_name = self.grid[self.current_player.grid_pos]
        doors = self.room_deck.obj_dict[room_name].doors

        if direction == 'N':
            if not doors[0]:
                self.messenger.add_entry(f'{room_name} {direction} blocked', 'red')
                return False
        elif direction == 'E':
            if not doors[1]:
                self.messenger.add_entry(f'{room_name} {direction} blocked', 'red')
                return False
        elif direction == 'S':
            if not doors[2]:
                self.messenger.add_entry(f'{room_name} {direction} blocked', 'red')
                return False
        elif direction == 'W':
            if room_name == 'Ground Floor Staircase':
                return True
            elif not doors[3]:
                self.messenger.add_entry(f'{room_name} {direction} blocked', 'red')
                return False
            
        # check for adjacent tile & walls
        if direction == 'N':
            target_pos = (self.current_player.grid_pos[0], self.current_player.grid_pos[1] - 1)
            if target_pos in self.grid.keys():
                target_room_name = self.grid[target_pos]
                target_doors = self.room_deck.obj_dict[target_room_name].doors
                if not target_doors[2]:
                    self.messenger.add_entry(f'Movement blocked by {target_room_name}', 'red')
                    return False
            else:
                new_tile = self.room_deck.choose_card(floor=self.current_player.floor)
                self.place_tile(new_tile.name, target_pos, direction)
                self.current_player.allow_move = False
                self.messenger.add_entry(f'Movement stopped for {self.current_player.name}', 'red')
        elif direction == 'E':
            target_pos = (self.current_player.grid_pos[0] + 1, self.current_player.grid_pos[1])
            if target_pos in self.grid.keys():
                target_room_name = self.grid[target_pos]
                target_doors = self.room_deck.obj_dict[target_room_name].doors
                if not target_doors[3]:
                    self.messenger.add_entry(f'Movement blocked by {target_room_name}', 'red')
                    return False
            else:
                new_tile = self.room_deck.choose_card(floor=self.current_player.floor)
                self.place_tile(new_tile.name, target_pos, direction)
                self.current_player.allow_move = False
                self.messenger.add_entry(f'Movement stopped for {self.current_player.name}', 'red')
        elif direction == 'S':
            target_pos = (self.current_player.grid_pos[0], self.current_player.grid_pos[1] + 1)
            if target_pos in self.grid.keys():
                target_room_name = self.grid[target_pos]
                target_doors = self.room_deck.obj_dict[target_room_name].doors
                if not target_doors[0]:
                    self.messenger.add_entry(f'Movement blocked by {target_room_name}', 'red')
                    return False
            else:
                new_tile = self.room_deck.choose_card(floor=self.current_player.floor)
                self.place_tile(new_tile.name, target_pos, direction)
                self.current_player.allow_move = False
                self.messenger.add_entry(f'Movement stopped for {self.current_player.name}', 'red')
        elif direction == 'W':
            target_pos = (self.current_player.grid_pos[0] - 1, self.current_player.grid_pos[1])
            if target_pos in self.grid.keys():
                target_room_name = self.grid[target_pos]
                target_doors = self.room_deck.obj_dict[target_room_name].doors
                if not target_doors[1]:
                    self.messenger.add_entry(f'Movement blocked by {target_room_name}', 'red')
                    return False
            else:
                new_tile = self.room_deck.choose_card(floor=self.current_player.floor)
                self.place_tile(new_tile.name, target_pos, direction)
                self.current_player.allow_move = False
                self.messenger.add_entry(f'Movement stopped for {self.current_player.name}', 'red')

        return True

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def run(self, dt):
        self.player_input()
        
        if self.game_state == "start":
            self.start_screen.update()
        elif self.game_state == "select":
            self.selector.update()
        else:        
            # drawing logic
            self.display_surf.fill(s.BG_COLOR)  # background
            self.update_timers()
            self.all_sprites.custom_draw(self.current_player)

            # updates
            if self.inventory_active:
                self.inventory_panel.update(self.current_player)
            elif self.roller_active:
                self.roller.update()
            elif self.event_active:
                self.event.update()
            else:
                self.all_sprites.update(dt)

            # overlay
            self.overlay.display(self.current_player)
            self.messenger.update()


class CameraGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2((-3 * s.TILE_SIZE, -s.TILE_SIZE))  # offsets the map to move player

        # camera speed for keyboard
        self.keyboard_speed = 3
    
    def keyboard_ctrl(self, player):
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
        # snap camera to specific position
        if keys[pygame.K_g]: # ground floor (Entrance Hall)
            self.set_camera(pygame.math.Vector2((-3 * s.TILE_SIZE, -s.TILE_SIZE)))
        elif keys[pygame.K_u]: # upper landing
            self.set_camera(pygame.math.Vector2((98 * s.TILE_SIZE, -s.TILE_SIZE)))
        elif keys[pygame.K_b]: # basement landing
            self.set_camera(pygame.math.Vector2((-102 * s.TILE_SIZE, -s.TILE_SIZE)))
        elif keys[pygame.K_p]: # player
            x = player.grid_pos[0] * s.TILE_SIZE - 2 * s.TILE_SIZE
            y = player.grid_pos[1]* s.TILE_SIZE + 1 * s.TILE_SIZE
            self.set_camera(pygame.math.Vector2((x, -y)))

    def custom_draw(self, player):
        self.keyboard_ctrl(player)
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
