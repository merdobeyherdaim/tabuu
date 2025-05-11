import random

# Game state
players = []
roles = ['Vampir', 'Köylü', 'Avcı']
player_roles = {}

# Game logic for assigning roles
def assign_roles(players):
    random.shuffle(players)
    for i, player in enumerate(players):
        role = roles[i % len(roles)]
        player_roles[player] = role
    return player_roles

# Sample function to start a game
def start_game(players):
    # Assign roles to players
    player_roles = assign_roles(players)
    return player_roles
