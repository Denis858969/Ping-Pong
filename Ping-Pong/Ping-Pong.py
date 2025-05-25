from pygame import *
from random import randint 
from time import time as timer
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
font.init()
font1 = font.SysFont('Arial', 36)
clock = time.Clock()
FPS = 60
speed = 10
game = True
finish = False
back = (255,255,255)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -=self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


racket1 = Player('racat.png', 30, 200, 150, 200, 5)
racket2 = Player('racat.png', 500, 200, 150, 200, 5)
ball = Player('ball.png', 300, 250, 60, 50, 150)    
speed_x = 3
speed_y = 3
font1 = font.Font(None , 35)
lose1 = font1.render('PLAYER 1 LOSE!', True,  (180,0,0))
font2 = font.Font(None , 35)
lose2 = font1.render('PLAYER 2 LOSE!', True,  (180,0,0))


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.fill(back)
        racket1.update_l()    
        racket2.update_r() 
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1    
    if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish= True
        window.blit(lose1,(200,200))
    if ball.rect.x > win_width:
        finish= True
        window.blit(lose2,(200,200))
            
    ball.reset()
    racket2.reset()
    racket1.reset()
    display.update()
    clock.tick(FPS)