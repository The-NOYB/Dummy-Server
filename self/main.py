import pygame
from client import Network
from player import Player


def init( ):
    window = pygame.display.set_mode( (1280, 720) )
    pygame.display.set_caption("Test client")
    clock = pygame.time.Clock()

    return clock, window

def main( player ):
    clock, window = init()
    keys = pygame.key.get_pressed()
    player.update(keys)
    connection_to_server = Network()
    connection_to_server.connect( player )

    while True:
       window.fill( (0,150,150) )
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               exit()

       pygame.display.update()
       clock.tick(60)

if __name__ == "__main__":
    pygame.init()
    x, y = ( map( int, input("Give the x and y for the player: ").split() ) )
    name = input("Give name for the player: ")
    player = Player(name, x, y)
    main( player )
