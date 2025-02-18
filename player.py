import pygame


class Player_data():
    def __init__(self, name, rect):
        self.name = name
        self.rect = rect
        self.x = rect.x
        self.y = rect.y

    # updating the data object along the sprite
    def update(self, player):
        self.rect = player.rect
        self.x = player.x
        self.y = player.y

class Player(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect(50, 50, 50, 50) 
        self.image = pygame.Surface(( 50, 50 ))
        self.image.fill( (100,100,100) )

        self.name = name
        self.x, self.y = x, y
        self.rect.x, self.rect.y = self.x, self.y

    def update_pos(self, x, y):
        self.x, self.y = x, y
        self.rect.x, self.rect.y = self.x, self.y
        print( "update_pos", self.x, self.y)
        
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

