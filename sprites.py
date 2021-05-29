import pygame

class Sprite:
    def __init__(self, x, y, img):
        self.image = img
        self.speed = 0
        self.x = x
        self.y = y
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height

class Player(Sprite):
    def __init__(self,x,y):
        Sprite.__init__(self, x, y, pygame.image.load(r'images/sonic.png'))
        self.speed = 4

    def update(self,keys):
        if keys[pygame.K_RIGHT]:
            self.x+=self.speed
        if keys[pygame.K_LEFT]:
            self.x-=self.speed
        if keys[pygame.K_UP]:
            self.y-=self.speed
        if keys[pygame.K_DOWN]:
            self.y+=self.speed


class Camera:
    def __init__(self, world_width,world_height,screen_width,screen_height):
        self.x = 0
        self.y =-800
        self.world_width = world_width
        self.world_height =  world_height
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self, sprite):
        if (sprite.x < self.world_width - self.screen_width/2
                and sprite.x > self.screen_width/2):
            self.x = int(self.screen_width/2)-sprite.x

        if (sprite.y < self.world_height - self.screen_height/2
                and sprite.y > self.screen_height/2):
            self.y = int(self.screen_height/2)-sprite.y