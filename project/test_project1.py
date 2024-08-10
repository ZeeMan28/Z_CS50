from project1 import check_for_ace

def test_check_for_ace():
    hand = {
        "player": {
            1: ["player1", 1],
            2: ["player2", 2]},
        "dealer": {
            1: ["dealer1", 1],
            2: ["dealer2", 14]}
    }

    cards = {}
    for i in range(1, 11):
        cards[str(i)] = [str(i), i, 4]
    
    # Assigning face cards
    cards["11"] = ["jack", 10, 4]
    cards["12"] = ["queen", 10, 4]
    cards["13"] = ["king", 10, 4]
    cards["14"] = ["ace", 1, 11, 4]

    assert check_for_ace(hand["dealer"]) == True
    assert check_for_ace(hand["player"]) == False

