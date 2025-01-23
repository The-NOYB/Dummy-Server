import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.x, self.y = x, y

    def update(self, keys):
        if keys[pygame.K_w]:
            self.y -= 1
        if keys[pygame.K_a]:
            self.x -= 1
        if keys[pygame.K_s]:
            self.y += 1
        if keys[pygame.K_d]:
            self.x += 1
    
    def C(self):
        pass

