import pygame
import settings as s
from timer import Timer
import random as r

class Roller:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('../font/Semi-Coder-Regular.otf', s.ROLLER_FONT_SIZE)

        self.window_width = s.POPUP_WIDTH
        self.window_height = s.POPUP_HEIGHT

        # timers
        self.roller_timers = {
            'input': Timer(),
            'frame': Timer(50, self.roll_dice),
            'animation': Timer(2000, self.end_animation)
        }

        self.dice_rolled = False

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


    def roll_dice(self):
        self.roll_result = 0

        for i, die in enumerate(self.dice_objs):
            if die.visible:
                die_result = die.roll()
                self.roll_result += die_result

        if not self.dice_rolled:
            self.roller_timers['frame'].activate()

    
    def end_animation(self):
        self.dice_rolled = True


    def roller_window(self):
        self.roller_rect = pygame.Rect((s.POSITIONS['roller']), (self.window_width, self.window_height))
        pygame.draw.rect(self.display_surface, s.ROLLER_BKG, self.roller_rect, border_radius=12)

        for die in self.dice_objs:
            if die.visible:
                self.display_surface.blit(die.image, die.rect)

        if self.dice_rolled:
            text = f'Roll Result: {self.roll_result}'
        elif self.roller_timers['animation'].active:
            text = 'Rolling...'
        else:
            text = '[PRESS SPACE TO ROLL]'

        text_surf = self.font.render(text, False, 'white')
        text_rect = text_surf.get_rect(midbottom=(self.roller_rect.midbottom[0], self.roller_rect.midbottom[1]- s.DIE_SIZE/2))
        self.display_surface.blit(text_surf, text_rect)


    def input(self):
        keys = pygame.key.get_pressed()

        if not self.roller_timers['input'].active:
            if keys[pygame.K_SPACE] and not self.dice_rolled:
                self.roller_timers['input'].activate()

                num_dice = r.randint(1,8)

                for i, die in enumerate(self.dice_objs):
                    if i < num_dice:
                        die.visible = True
                    else:
                        die.visible = False

                self.roller_timers['frame'].activate()
                self.roller_timers['animation'].activate()


    def update(self):
        self.roller_window()
        for timer in self.roller_timers.values():
            timer.update()
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

        return result
