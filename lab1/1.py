import pygame
import random
from pygame import mixer

pygame.font.init()
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Catch me if you can")

mixer.music.load("Music/game.wav")
mixer.music.play(-1)
mixer.music.set_volume(0.1)
soundLoose = mixer.Sound("Music/loose.wav")
soundCatch = mixer.Sound("Music/catch.wav")
soundMiss = mixer.Sound("Music/miss.wav")

class Box:
    def __init__(self, x, speed, color):
        self.x = x
        self.y = 500
        self.speed = speed
        self.width = 150
        self.height = 80
        self.color = color
        self.width1 = 130
        self.height1 = 70
        self.button = pygame.key.get_pressed()

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (125, 125, 125), (self.x + 20, self.y, self.width1 - 20, self.height1 - 10))

    def left(self):
        self.x -= self.speed
        if self.x > screen.get_size()[0]:
            self.x = 0 - self.width
        if self.x < 0 - self.width:
            self.x = screen.get_size()[0]

    def right(self):
        self.x += self.speed
        if self.x > screen.get_size()[0]:
            self.x = 0 - self.width
        if self.x < 0 - self.width:
            self.x = screen.get_size()[0]

    def collision(self, ball):
        lx1 = self.x + 10
        lx2 = ball.x - ball.radius
        rx1 = self.x + self.width1
        rx2 = ball.x + ball.radius
        ty1 = self.y
        ty2 = ball.y - ball.radius
        by1 = self.y + self.height1
        by2 = ball.y + ball.radius
        lx = max(lx1, lx2)
        rx = min(rx1, rx2)
        ty = max(ty1, ty2)
        by = min(by1, by2)

        if lx <= rx and ty <= by:
            return True
        return False

class Ball:
    def __init__(self):
        self.x = random.randint(50, 700)
        self.y = random.randint(20, 60)
        self.speed = 12
        self.radius = 10
        self.cnt = 0
        
    def draw(self):
        Centre = (self.x, self.y)
        pygame.draw.circle(screen, (255, 255, 255), Centre, self.radius)
        
    def move(self):
        self.y += self.speed
        self.draw()

    def new(self):
        self.x = random.randint(50, 750)
        self.y = random.randint(20, 60)
        self.cnt += 1

    def miss(self):
        if self.y >= screen.get_size()[1] - 40:
            self.new()
            self.cnt -= 3
            if self.cnt >= 0:
                soundMiss.play()
    
    def cnt_count(self):
        font = pygame.font.SysFont("Arial", 36)
        text = font.render("Points: " + str(self.cnt), 1, (255, 255, 255))
        place = text.get_rect(center = (720, 50))
        screen.blit(text, place)

is_game = True
musicloose = False
loose = 0

box = Box(300, 20, (225, 225, 0))

ball = Ball()

FPS = 30

clock = pygame.time.Clock()

while is_game:
    mills = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game = False
    screen.fill((0, 0, 0))

    button = pygame.key.get_pressed()
    if button[pygame.K_LEFT]:
        box.left()
    if button[pygame.K_RIGHT]:
        box.right()
    
    ball.move()
    box.draw()

    if box.collision(ball):
        ball.new()
        soundCatch.play()
    ball.miss()

    if ball.cnt < 0:
        font1 = pygame.font.SysFont("Arial", 80)
        text1 = font1.render("GAME OVER", 1, (255, 255, 255))
        place1 = text1.get_rect(center = (400, 300))

        screen.blit(text1, place1)
        box.speed = 0
        ball.speed = 0
        mixer.music.stop()
        musicloose = True
        pygame.display.flip()

    if loose == 0 and musicloose:
        soundLoose.play()
        loose = 1

    ball.cnt_count()

    pygame.display.flip()