import pygame
from client import Network
from player import Player, Player_data


def init( ):
    window = pygame.display.set_mode( (1280, 720) )
    pygame.display.set_caption("Test client")
    clock = pygame.time.Clock()

    return clock, window

def remove_local(online_players, local_player_data):
    for player in online_players:
        if player.name == local_player_data.name:
            online_players.remove( player )
    return online_players

def add_players(sprite_group, players, local_player_data):
    try:
        check_list = players.copy()
        for player in players:      # loop for online players
            for sprite in sprite_group:
                # if the player exists in sprite group then update its postiion and remove from check_list
                if player.name == sprite.name:
                    sprite.update_pos( player.x, player.y)
                    check_list.remove( player )

        # all the players that not have been added to sprite group to be added
        for new_player in check_list:
            sprite_group.add( Player(new_player.name, new_player.x, new_player.y) )

    except Exception as e:
        print(e)

def main( local_player, local_player_data ):
    clock, window = init()

    online_players = []
    local_group = pygame.sprite.Group()     # for local entities
    online_group = pygame.sprite.Group()    # for online players

    local_group.add( local_player )
    connection_to_server = Network()
    connection_to_server.connect( local_player_data )
    online_players = []

    while True:
        window.fill( (0,150,150) )
        keys = pygame.key.get_pressed()

        # get the players data from server and remove the local player from it
        online_players = remove_local( connection_to_server.send(local_player_data), local_player_data)
        # 
        add_players( online_group, online_players, local_player_data) 

        if online_players:
            print( local_player_data.name,local_player_data.x,local_player_data.y )
            print( [ (sp.name, sp.x, sp.y) for sp in online_group ] )

#        print( f" online_group: {[ player.name for player in online_group ]}" ) 

        local_group.update( keys )
        local_player_data.update( local_player ) # updating the player data
        local_group.draw( window )

        online_group.draw( window )

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
