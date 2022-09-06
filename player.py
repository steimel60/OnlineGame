import pygame as pg

class Character():
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 2

    def draw(self, win):
        pg.draw.rect(win, self.color, self.rect)

    def move(self):
        pass

    def set_color(self, color):
        self.color = color

    def update(self):
        self.rect = (self.x,self.y,self.width,self.height)

class Player(Character):
    def __init__(self,Character,id):
        super().__init__(Character.x,Character.y,Character.width,Character.height,Character.color)
        self.id = id
    def move(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.x -= self.vel
        if keys[pg.K_RIGHT]:
            self.x += self.vel
        if keys[pg.K_UP]:
            self.y -= self.vel
        if keys[pg.K_DOWN]:
            self.y += self.vel

        self.update()

playable_characters = {
    "Dyffros" : Character(0,0,50,50,(255,0,255)),
    "Orlyn" : Character(75,0,50,50,(0,255,0)),
    "Immis Wrax" : Character(75*2, 0, 50,50, (50,50,50)),
    "Entei" : Character(75*3, 0, 50,50, (255,0,0))
}
