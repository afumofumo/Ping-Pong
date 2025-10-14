import pygame
from pygame import *
from random import randint

pygame.init()

#escena del videojuego:
back = (200, 255, 255) # (fondo)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('PingPong Game')
window.fill(back)

font.init()
font = font.Font(None, 35)
scoretext1 = font.render('¡EL JUGADOR 1 ANOTA!', True, (180, 0, 0))
scoretext2 = font.render('¡EL JUGADOR 2 ANOTA!', True, (180, 0, 0))
lose1 = font.render('¡EL JUGADOR 1 PIERDE!', True, (180, 0, 0))
lose2 = font.render('EL JUGADOR 2 PIERDE!', True, (180, 0, 0))


#banderas responsables por el estado del juego
game = True
finish = False
clock = time.Clock()
FPS = 60
speed_x = 3
speed_y = 3

score1 = 0
score2 = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #por ejemplo. 55,55 - parámetros
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

def reset_ball(direction=1):
    global speed_x, speed_y
    ball.rect.x = win_width // 2 - ball.rect.width // 2
    ball.rect.y = win_height // 2 - ball.rect.height // 2
    speed_x = 5 * direction
    speed_y = randint(-4, 4)
    if speed_y == 0:
        speed_y = 3

ball = GameSprite('ball.png', 200, 200, 4, 50, 50)
racket1 = Player('stick.png', 30, 200, 4, 50, 100) 
racket2 = Player('stick2.png', 520, 200, 4, 50, 100)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back) 
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y >win_height-50 or ball.rect.y < 0:
            speed_y *=-1

        if sprite.collide_rect(racket1, ball):
            if speed_x < 0:
                speed_x *= -1
                ball.rect.left = racket1.rect.right
        
        if sprite.collide_rect(racket2, ball):
            if speed_x > 0:
                speed_x *= -1
                ball.rect.right = racket2.rect.left

        #si la pelota va más allá de la paleta, mostrar la condición de derrota para el jugador 1
        if ball.rect.x < 0:
            score2 += 1
            finish = True
            window.blit(scoretext2, (200, 200))
            


        #si la pelota va más allá de la paleta, mostrar la condición de derrota para el jugador 2
        if ball.rect.x > win_width:
            score1 += 1
            finish = True
            window.blit(scoretext1, (200, 200))
            




        ball.reset()
        racket1.reset()
        racket2.reset()

        score_display = font.render(f"{score1}    :    {score2}", True, (50, 50, 50))
        window.blit(score_display, (win_width // 2 - 60, 20))

    else:
        display.update()
        time.delay(2000)
        finish = False
        direction = 1 if ball.rect.x > win_width // 2 else -1
        reset_ball(direction)

    display.update()
    clock.tick(FPS)