import random

draw = {
    "player": {
        1: ["player1", str(random.randint(1, 13))],
        2: ["player2", str(random.randint(1, 13))]},
    "dealer": {
        1: ["dealer1", str(random.randint(1, 13))],
        2: ["dealer2", str(random.randint(1, 13))]}
}

current_player_card = list(draw["player"].keys())[-1]

print(current_player_card)