import pygame
import random
import math


class Rock(pygame.sprite.Sprite):
    def __init__(self, screen_dims):
        super(Rock, self).__init__()
        self.screen_width = screen_dims[0]
        self.screen_height = screen_dims[1]
        self.size_min = 20
        self.size_max = 80
        self.size = self.size_min + random.random() * (self.size_max - self.size_min)
        self.size = random.randint(self.size_min, self.size_max)
        self.speed_min = 2
        self.speed_max = 10
        self.speed = self.speed_min + random.random() * (self.speed_max - self.speed_min)
        self.angle = random.random() * 2 * math.pi
        self.dir_x = math.cos(self.angle)
        self.dir_y = math.sin(self.angle)
        if self.dir_x > 0 and self.dir_y <= 0:
            self.face = random.choice(['left', 'top'])
        elif self.dir_x > 0 and self.dir_y > 0:
            self.face = random.choice(['left', 'bottom'])
        elif self.dir_x <= 0 and self.dir_y <= 0:
            self.face = random.choice(['right', 'top'])
        elif self.dir_x <= 0 and self.dir_y > 0:
            self.face = random.choice(['right', 'bottom'])
        if self.face == 'left':
            self.center = (-self.size / 2, random.randint(0, self.screen_height))
        elif self.face == 'right':
            self.center = (self.screen_width + (self.size / 2), random.randint(0, self.screen_height))
        elif self.face == 'top':
            self.center = (random.randint(0, self.screen_width), -self.size / 2)
        elif self.face == 'bottom':
            self.center = (random.randint(0, self.screen_width), self.screen_height + (self.size / 2))
        self.surf = pygame.image.load("./kuiper_escape/static/asteroid.png")
        self.surf = pygame.transform.scale(self.surf, (self.size, self.size))
        self.surf = self.surf.convert_alpha()
        self.rect = self.surf.get_rect(center=self.center)

    # Update location, kill if moved off of the screen
    def update(self):
        self.rect.move_ip(self.speed * self.dir_x, -self.speed * self.dir_y)
        if self.rect.right < 0:
            self.kill()
        elif self.rect.left > self.screen_width:
            self.kill()
        elif self.rect.top > self.screen_height:
            self.kill()
        elif self.rect.bottom < 0:
            self.kill()
