from pygame import *


#escena del videojuego:
back = (200, 255, 255) # (fondo)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

font.init()
font = font.Font(None, 35)
lose1 = font.render('¡EL JUGADOR 1 PIERDE!', True, (180, 0, 0))
lose2 = font.render('EL JUGADOR 2 PIERDE!', True, (180, 0, 0))


#banderas responsables por el estado del juego
game = True
finish = False
clock = time.Clock()
FPS = 60
speed_x = 3
speed_y = 3


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

ball = GameSprite('balonSF.png', 200, 200, 4, 50, 50)
racket1 = Player('Raket1.png', 30, 200, 4, 25, 100) 
racket2 = Player('Raket2.png', 520, 200, 4, 25, 100)


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
    
    if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball): 
        speed_x *= -1 


#si la pelota va más allá de la paleta, mostrar la condición de derrota para el jugador 1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
        


    #si la pelota va más allá de la paleta, mostrar la condición de derrota para el jugador 2
    if ball.rect.x > win_width:
        finish = True
        window.blit(lose2, (200, 200))
        



    
    ball.reset()
    racket1.reset()
    racket2.reset()

    display.update()
    clock.tick(FPS)