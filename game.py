import pygame as pg
from player import playable_characters

class Game:
    def __init__(self):
        self.players = {}
        self.characters = {
            'Orlyn' : {
                'Selected' : False,
                'ID'    : None
            },
            'Dyffros' : {
                'Selected' : False,
                'ID'    : None
            },
            'Immis Wrax' : {
                'Selected' : False,
                'ID'    : None
            },
            'Entei' : {
                'Selected' : False,
                'ID'    : None
            }
        }

    def update_player(self, player, id):
        self.players[id] = player

    def remove_player(self, id):
        del self.players[id]
        for character in self.characters:
            if self.characters[character]["ID"] == id:
                self.characters[character]["ID"] = None
                self.characters[character]["Selected"] = False
