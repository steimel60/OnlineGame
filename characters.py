import pygame as pg

class CharacterSelector():
    def __init__(self, name, selected, hovered=False, pos=(0,0)):
        self.name = name
        self.selected = selected
        self.hovered = hovered
        self.pos = pos

    def draw(self, win):
        font = pg.font.Font('freesansbold.ttf', 16)
        if self.hovered and not self.selected: color = (250,250,250)
        elif self.hovered and self.selected: color = (155,0,0)
        elif self.selected: color = (255,0,0)
        else: color = (0,0,0)
        img = font.render(self.name, False, color)
        win.blit(img, self.pos)
