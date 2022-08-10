import pygame
import random
import os

pygame.init()
screen = pygame.display.set_mode((600, 650,))
pygame.display.set_caption("car-game")
clock = pygame.time.Clock()
pygame.mixer.init()

#load 
BG = pygame.image.load(os.path.join("img", "road650.jpg"))
MENU = pygame.image.load(os.path.join("img", "menu.jpg"))
AMG = pygame.image.load(os.path.join("img", "amg.png")).convert_alpha()
FERRARI = pygame.image.load(os.path.join("img", "ferrari.png")).convert_alpha()
CORVETTE = pygame.image.load(os.path.join("img", "corvette.png")).convert_alpha()
BUGATTY = pygame.image.load(os.path.join("img", "bugatty.png")).convert_alpha()
DODGE= pygame.image.load(os.path.join("img", "dodge.png")).convert_alpha()
SUPRA = pygame.image.load(os.path.join("img", "supra.png")).convert_alpha()
cOIN1 = pygame.image.load(os.path.join("img", "an_coin1.png")).convert_alpha()
cOIN2 = pygame.image.load(os.path.join("img", "an_coin2.png")).convert_alpha()
cOIN3 = pygame.image.load(os.path.join("img", "an_coin3.png")).convert_alpha()
cOIN4 = pygame.image.load(os.path.join("img", "an_coin4.png")).convert_alpha()
cOIN5 = pygame.image.load(os.path.join("img", "an_coin5.png")).convert_alpha()
cOIN6 = pygame.image.load(os.path.join("img", "an_coin6.png")).convert_alpha()
GAME_OVER= pygame.image.load(os.path.join("img", "game_over.png")).convert_alpha()
PRIX = pygame.image.load(os.path.join("img", "prix.png")).convert_alpha()
TREE_BUT = pygame.image.load(os.path.join("img", "tree_but.png")).convert_alpha()
LEVEL_UP_ICON = pygame.image.load(os.path.join("img", "level_up_icon.png")).convert_alpha()
LEVEL_UP = pygame.image.load(os.path.join("img", "level_up.png")).convert_alpha()
amg = pygame.transform.scale(AMG, (65, 120))
dodge = pygame.transform.scale(DODGE, (65, 120))
ferrari = pygame.transform.scale(FERRARI, (65, 120))
bugatty = pygame.transform.scale(BUGATTY, (65, 120))
supra = pygame.transform.scale(SUPRA, (65,120))
tree_but = pygame.transform.scale(TREE_BUT, (80, 35))
corvette = pygame.transform.scale(CORVETTE, (65, 120))
COIN1 = pygame.transform.scale(cOIN1, (50, 50))
level_up = pygame.transform.scale(LEVEL_UP, (130, 50))
COIN_BUT = pygame.transform.scale(cOIN1, (40, 40))
level_up_icon = pygame.transform.scale(LEVEL_UP_ICON, (40, 43))
game_over_icon = pygame.transform.scale(GAME_OVER, (250, 250))
prix = pygame.transform.scale(PRIX, (40, 40))
COIN2 = pygame.transform.scale(cOIN2, (50, 50))
COIN3 = pygame.transform.scale(cOIN3, (50, 50))
COIN4 = pygame.transform.scale(cOIN4, (40, 50))
COIN5 = pygame.transform.scale(cOIN5, (50, 50))
COIN6 = pygame.transform.scale(cOIN6, (50, 50))
WIDTH = 600
HEIGHT = 650
FPS = 60
font = pygame.font.SysFont('Arial', 40)
objects = []
SCORE = 0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
font_name = pygame.font.match_font('arial')
passed = 0
coin_pos = [130, 315, 220, 405]
CARS = [amg, corvette, supra, ferrari, dodge, bugatty]
CRASH = pygame.mixer.Sound('sounds\\crash.mp3')
coin_sound = pygame.mixer.Sound('sounds\\coin_drop.mp3')
coin_sound.set_volume(0.5)
level_up_sound = pygame.mixer.Sound("sounds\\level_up.mp3")
level = 0

#objects
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = supra
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 35 
        self.speedx = 0
    def update(self):
        self.speedx = 0
        self.speedy= 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -9
        if keystate[pygame.K_RIGHT]:
            self.speedx = 9
        if keystate[pygame.K_UP]:
            self.speedy = -2
        if keystate[pygame.K_DOWN]:
            self.speedy = +4
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > 0.85*WIDTH:
            self.rect.right = 0.85*WIDTH
        if self.rect.left < 96:
            self.rect.left = 96
        if self.rect.bottom > 650:
            self.rect.bottom = 650
        if self.rect.top < 0:
            self.rect.top = 0
        self.mask = pygame.mask.from_surface(self.image)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(CARS)
        self.rect = self.image.get_rect(center = (400,400))
        self.rect.x = 405
        self.rect.y = random.randrange(-2000, -1100)
        self.speedy = 5
        self.passed = 0
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.image = random.choice(CARS) 
            self.rect.y = random.randrange(-2000, -1100)
            self.mask = pygame.mask.from_surface(self.image)
            self.passed += 1

class Mob2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(CARS)
        self.rect = self.image.get_rect()
        self.rect.x = 220
        self.rect.y = random.randrange(-1000, -40)
        self.speedy = 5
        self.passed = 0

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.image = random.choice(CARS)
            self.rect.y = random.randrange(-6000, -4000)
            self.mask = pygame.mask.from_surface(self.image)
            self.passed += 1

class Mob3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(CARS)
        self.rect = self.image.get_rect()
        self.rect.x = 315
        self.rect.y = random.randrange(-2500, -1000)
        self.speedy = 5
        self.passed = 0
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.image = random.choice(CARS)
            self.rect.y = random.randrange(-3000, -2000)
            self.mask = pygame.mask.from_surface(self.image)
            self.passed += 1
class Mob4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(CARS)
        self.rect = self.image.get_rect()
        self.rect.x = 130
        self.rect.y = random.randrange(-2000, -500)
        self.speedy =5
        self.mask = pygame.mask.from_surface(self.image)
        self.passed = 0
        self.level = 1
        self.stat = 0
        self.check = 0

    def update(self):
        self.rect.y += self.speedy
        self.check += 1
        if self.rect.top > HEIGHT + 10 :
            self.image = random.choice(CARS)
            self.rect.y = random.randrange(-2000, -40)
            self.mask = pygame.mask.from_surface(self.image)
            self.passed += 1
            self.level += 0.1
            self.stat +=1
            
class LevelUp(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = level_up
        self.rect = self.image.get_rect()
        self.rect.y = -30
        self.rect.x = -30
    def update(self):
        self.rect.y = -100
        self.rect.x = -100

class Mob5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [COIN1, COIN2, COIN3, COIN4, COIN5, COIN6, COIN1]
        self.speedy = 5
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(coin_pos)
        self.rect.y = random.randrange(-200, -10)
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        self.rect.y += self.speedy
        self.current_sprite += 0.1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.image = self.sprites[int(self.current_sprite)]
        if self.rect.top > HEIGHT + 50:
            self.rect.x = random.choice(coin_pos)
            self.rect.y = random.randrange(-200, -100)
            self.mask = pygame.mask.from_surface(self.image)

#functions
def draw_text (surf, text, size, x, y, color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)       


def show_go_screen():
    screen.blit(game_over_icon, (180,110))
    pygame.mixer.music.load("sounds\\bg_menu.wav")
    pygame.mixer.music.play(-1)
    draw_text(screen, "Press space to restart", 30, WIDTH / 2,615, GREEN)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = 0
def show_menu():
    screen.blit(MENU, (0,0))
    pygame.mixer.music.load("sounds\\bg_menu.wav")
    pygame.mixer.music.play(-1)
    draw_text(screen, "Press a key to begin", 30, WIDTH / 2,585, WHITE)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
menu = 1
pause = 0
game_over = 0
running = True
#game loop
while running:
    
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                draw_text(screen, "PAUSED", 60, WIDTH / 2,200, BLACK)
                pygame.display.flip()
                pygame.mixer.music.unpause()
                pause = not pause
    if pause == 1:
        pygame.mixer.music.pause()
        continue
    if game_over:
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        player = Player()
        coins = pygame.sprite.Group()
        all_sprites.add(player)
        m = Mob()
        m1 = Mob2()
        m2= Mob3()
        m3 = Mob4()
        m4 = Mob5()
        l = LevelUp()
        all_sprites.add(m, m1, m2, m3, m4, l)
        mobs.add(m, m1, m2, m3)
        i = 0
        level = 0
        passed = 0
        SCORE = 0
        show_go_screen()
        game_over = False
        pygame.mixer.music.load("sounds\\bg_main.mp3")
        pygame.mixer.music.play(-1)
    if menu:
            all_sprites = pygame.sprite.Group()
            mobs = pygame.sprite.Group()
            player = Player()
            coins = pygame.sprite.Group()
            all_sprites.add(player)
            m = Mob()
            m1 = Mob2()
            m2= Mob3()
            m3 = Mob4()
            m4 = Mob5()
            l = LevelUp()
            all_sprites.add(m, m1, m2, m3, m4, l)
            mobs.add(m, m1, m2, m3)
            i = 0
            level = 0
            passed = 0
            SCORE = 0
            show_menu()
            pygame.mixer.music.load("sounds\\bg_main.mp3")
            pygame.mixer.music.play(-1)
            menu = 0
 

    #UPDATE
    all_sprites.update()
    if pygame.sprite.collide_mask(player,m4):
        SCORE += 1
        coin_sound.play()
        m4.rect.x = random.choice(coin_pos)
        m4.rect.y = random.randrange(-200, -10)
    
    if pygame.sprite.spritecollide(m4, mobs, 0):
        m4.rect.x = random.choice(coin_pos)
        m4.rect.y = random.randrange(-200, -10)

    if pygame.sprite.spritecollide(player, mobs, 0, pygame.sprite.collide_mask):
        pygame.mixer.music.pause()
        CRASH.play()
        pygame.time.delay(2000)
        game_over = True

    # RENDER
    screen.fill(BLACK)
    screen.blit(BG,(0,i))
    screen.blit(BG,(0, -HEIGHT+i))
    #looping background
    if i == HEIGHT:
        screen.blit(BG,(0, -10*HEIGHT+i))
        i = 0
    i+=10
    passed = (m.passed + m1.passed + m2.passed + m3.passed)*15
    screen.blit(tree_but, (520,3))
    screen.blit(tree_but, (520,44))
    screen.blit(tree_but, (520,90))
    screen.blit(COIN_BUT, (510,0))
    screen.blit(level_up_icon,(510, 87))
    screen.blit(prix,(510, 43))
    draw_text(screen, str(SCORE), 21, 575, 10, WHITE)
    draw_text(screen, str(passed), 18, 570, 50, WHITE)
    if m3.check % 2000 == 0:
        level += 1
        m.speedy += 1
        m1.speedy +=1
        m2.speedy +=1
        m4.speedy +=1
        m3.speedy +=1
    if len(str(m3.check)) == 4:
        if int(str(m3.check)[-3:]) < 200 and int(str(m3.check)[0:1]) % 2 == 0:
          l.rect.y = 10
          l.rect.x = 230
          level_up_sound.play()
    elif len(str(m3.check)) == 5:
        if int(str(m3.check)[-3:]) < 200 and int(str(m3.check)[0:2]) % 2 == 0:
          l.rect.y = 10
          l.rect.x = 230
          level_up_sound.play()
    draw_text(screen, str(level), 21, 570, 97, WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()  