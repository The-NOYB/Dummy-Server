import pygame
from client import Network

class Player():
    def __init__(self, x, y):
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


def init( ):
    window = pygame.display.set_mode( (1280, 720) )
    pygame.display.set_caption("Test client")
    clock = pygame.time.Clock()

    return clock, window

def main( player ):
    clock, window = init()
    keys = pygame.key.get_pressed()
    player.update()

    while True:
       window.fill( (0,200,200) )
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               exit()

       pygame.display.update()
       clock.tick(60)

if __name__ == "__main__":
    pygame.init()
    x, y = ( map( int, input("Give the x and y for the player: ").split() ) )
    player = Player(x, y)
    main( player )
