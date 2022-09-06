import pygame as pg
from network import Network
from characters import CharacterSelector

#----- Network Settings -----#
DISCONNECT_MSG = "!Disconnect"

#------- Pygame Settings -------#
width = 500
height = 500
win = pg.display.set_mode((width, height))
pg.display.set_caption("Client")

def draw_window(win, game):
    win.fill((255,255,255))
    for id in game.players:
        game.players[id].draw(win)
    pg.display.update()

def draw_char_sel(win,game,curr_sel):
    win.fill((150,150,150))
    i = 0
    for name in game.characters:
        cs = CharacterSelector(name, game.characters[name]['Selected'], hovered=(i==curr_sel), pos=(width/2,i*100))
        cs.draw(win)
        del cs
        i += 1
    pg.display.update()

def character_selection(network, player_id):
    selecting = True
    clock = pg.time.Clock()

    sel_index = 0
    while selecting:
        clock.tick(60)
        #Get updated game
        try:
            game = network.get()
        except:
            selecting = False
            break

        chars = [CharacterSelector(name, game.characters[name]['Selected']) for name in game.characters]
        draw_char_sel(win,game,sel_index)

        #Send client updates
        keys = pg.key.get_pressed()
        msg = "Selecting Character"
        for event in pg.event.get():
            if event.type == pg.QUIT:
                selecting = False
                network.send(DISCONNECT_MSG)
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    sel_index = max(0, sel_index - 1)
                elif event.key == pg.K_DOWN:
                    sel_index = min(len(game.characters)-1, sel_index + 1)
                elif event.key == pg.K_SPACE:
                    if game.characters[chars[sel_index].name]['Selected'] == True:
                        print(f"{chars[sel_index]} has already been selected!")
                    else:
                        selecting = False
                        msg = chars[sel_index]
        network.send(msg)
        del chars
    #Get updated game
    try:
        game = network.get()
        return game.players[player_id]
    except:
        print("Lost Connection")


def main():
    run = True
    clock = pg.time.Clock()
    n = Network()
    player = character_selection(n, n.get_id())
    n.send("hi")
    print("Run game")
    while run:
        clock.tick(60)
        #Get updated game
        try:
            game = n.get()
        except:
            run = False
            break
        #Get input
        player.move()
        draw_window(win, game)
        #Send client updates
        n.send(player)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                n.send(DISCONNECT_MSG)
                pg.quit()

pg.init()
main()
