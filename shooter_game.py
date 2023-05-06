from pygame import *

font.init()
font1 = font.Font(None, 80)
font2 = font.Font(None, 36)
lost = 0
score = 0
max_lost = 3
life = 3
class GameSprite(sprite.Sprite):
   #конструктор класса
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
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 5, 10, -15)
        bullets.add(bullet)

num_fire = 0
rel_time = False
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Shooter Game")



run = True
finish = False
ship = Player('rocket.png', 350, 420, 80, 100, 10)
clock = time.Clock()
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
   display.update() 
   clock.tick(50)
