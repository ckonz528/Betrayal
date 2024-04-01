import pygame
import settings as s
from timer import Timer
import random as r

class Roller:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.input_timer = Timer()
        self.animation_timer = Timer(3000)

        self.setup()

    def setup(self):
        self.dice_objs = []
        x = s.POSITIONS['roller'][0] + s.DIE_SIZE
        y = s.POSITIONS['roller'][1] + s.DIE_SIZE
        for i in range(8):
            self.dice_objs.append(Die(x,y))
            if i == 3:
                y += 1.5 * s.DIE_SIZE
                x = s.POSITIONS['roller'][0] + s.DIE_SIZE
            else:
                x += s.DIE_SIZE * 1.5


    def roll_dice(self, num_dice:str):
        for i in range(num_dice):
            self.dice_objs[i].visible = True


    def roller_window(self):
        self.roller_rect = pygame.Rect((s.POSITIONS['roller']), (s.SCREEN_W - s.TILE_SIZE - 200, s.SCREEN_H - 200))
        pygame.draw.rect(self.display_surface, s.ROLLER_BKG, self.roller_rect, border_radius=12)

        for die in self.dice_objs:
            if die.visible:
                self.display_surface.blit(die.image, die.rect)

    def input(self):
        keys = pygame.key.get_pressed()
        self.input_timer.update()

        if not self.input_timer.active:
            if keys[pygame.K_SPACE]:
                self.input_timer.activate()

                for die in self.dice_objs:
                    die.visible = False

                self.roll_dice(r.randint(1,8))

    def update(self):
        self.roller_window()
        self.input()


class Die():
    def __init__(self, die_x, die_y) -> None:

        self.sides = [0,1,2]
        self.visible = True # use this to control which dice are visible/ being used

        # faces
        self.faces = []
        for i in self.sides:
            image = pygame.image.load(f'../graphics/dice/{i}.png').convert_alpha()
            image = pygame.transform.scale(image, (s.DIE_SIZE, s.DIE_SIZE))
            self.faces.append(image)

        # position
        self.die_x = die_x
        self.die_y = die_y
        
        self.roll()

    def roll(self) -> int:
        result = r.choice(self.sides)
        self.image = self.faces[result]
        self.rect = self.image.get_rect(center=(self.die_x,self.die_y))
