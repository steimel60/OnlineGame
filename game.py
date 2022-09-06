import pygame as pg
from player import playable_characters

class Game:
    def __init__(self):
        self.players = {}
        self.characters = {
            'Orlyn' : {
                'Color' : (150,150,255),
                'Selected' : False
            },
            'Dyffros' : {
                'Color' : (255,100,255),
                'Selected' : False
            },
            'Immis Wrax' : {
                'Color' : (200,200,50),
                'Selected' : False
            },
            'Entei' : {
                'Color' : (255,0,0),
                'Selected' : False
            }
        }

    def update_player(self, player, id):
        self.players[id] = player

    def remove_player(self, id):
        del self.players[id]
