import pygame
from client import Network
from player import Player, Player_data


def init( ):
    window = pygame.display.set_mode( (1280, 720) )
    pygame.display.set_caption("Test client")
    clock = pygame.time.Clock()

    return clock, window

def add_players(sprite_group, players):
    try:
        for player in players:
            sprite_group.add( Player(player.name, player.x, player.y) )
    except Exception as e:
        print(e)

def main( local_player, local_player_data ):
    clock, window = init()

    online_players = []
    local_group = pygame.sprite.Group()     # for local entities
    online_group = pygame.sprite.Group()    # for online players

    local_group.add( local_player )
    connection_to_server = Network()
    online_players = connection_to_server.connect( local_player_data )

    while True:
        window.fill( (0,150,150) )
        keys = pygame.key.get_pressed()

        online_players = connection_to_server.send( local_player_data )

        add_players( online_group, online_players ) 

        local_group.update( keys )
        local_player_data.update( local_player ) # updating the player data
        local_group.draw( window )

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

    local_player = Player(name, x, y)
    local_player_data = Player_data(name, local_player.rect)

    main( local_player, local_player_data)
