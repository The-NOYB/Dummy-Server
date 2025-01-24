import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect(50, 50, 50, 50) 
#        self.image = pygame.Surface(( 50, 50 ))
#        self.image.fill( (100,100,100) )

        self.name = name
        self.x, self.y = x, y
        self.rect.x, self.rect.y = self.x, self.y

    def update(self, keys):
        if keys[pygame.K_w]:
            self.y -= 1
        if keys[pygame.K_a]:
            self.x -= 1
        if keys[pygame.K_s]:
            self.y += 1
        if keys[pygame.K_d]:
            self.x += 1

        self.rect.x, self.rect.y = self.x, self.y
        print( self.rect.x, self.rect.y)
    
class player_data():
    def __init__(self, name, x, y, rect):
        self.name = name
        self.x, self.y = x, y
        self.rect = rect

    def B(self):
        pass
    
    def C(self):
        pass
