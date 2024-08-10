import random
import time

def main():
    yourMoney = 0
    while True:
        try:
            bet = int(input("How much would you like to bet? Please enter a number 1-100 "))
            winnings = blackjack(bet)
            
            if winnings == 1:
                yourMoney += bet * 1.5
            elif winnings == 0:
                yourMoney -= bet
            else:
                print("Draw")

            print(f"You have ${yourMoney}.")

        except EOFError:
            print(f"Final earnings: {yourMoney}")
            break

def blackjack(x):
    x = int(x)
    cards = {}

    def calc_total(hand):
        total = 0
        for i in list(hand.keys()):
            total += int(cards[hand[i][1]][1])
        return total
    
    def check_for_ace(hand):
        for i in list(hand.keys()):
            if (hand[i][1] == 14):
                return True
        return False

    # Assigning normal cards
    for i in range(1, 11):
        cards[str(i)] = [str(i), i, 4]
    
    # Assigning face cards
    cards["11"] = ["jack", 10, 4]
    cards["12"] = ["queen", 10, 4]
    cards["13"] = ["king", 10, 4]
    cards["14"] = ["ace", 1, 11, 4]

    # Assigning initial player and dealer hands
    draw = {
        "player": {
            1: ["player1", str(random.randint(1, 14))],
            2: ["player2", str(random.randint(1, 14))]},
        "dealer": {
            1: ["dealer1", str(random.randint(1, 14))],
            2: ["dealer2", str(random.randint(1, 14))]}
    }

    total_player = calc_total(draw["player"])
    total_dealer = calc_total(draw["dealer"])

    print(f"Your hand: {cards[draw['player'][1][1]][0]}, {cards[draw['player'][2][1]][0]} ({total_player})")
    print(f"Dealer's hand: {cards[draw['dealer'][1][1]][0]}, {cards[draw['dealer'][2][1]][0]} ({total_dealer})")


    # Game loop
    while True:
        if hitStand():

            #HIT...........................................................
            current_player_card = list(draw["player"].keys())[-1]

            draw["player"][current_player_card + 1] = ["player" + str(current_player_card + 1), str(random.randint(1, 14))]

            print(f"Your next card is {cards[draw['player'][current_player_card + 1][1]][0]}", end="\n\n")

            total_player = calc_total(draw["player"])
            print(f"Your total: {total_player}")

            #STAND.........................................................
                #IF LESS THAN DEALER, YOU LOSE.............................
        elif total_dealer > total_player:

                #CHECKING IF PLAYER HAS ACE, IN WHICH CASE THEY WOULDNT LOSE AUTOMATICALLY
            if check_for_ace(draw["player"]) and total_player + 10 >= total_dealer:
                break
            else:
                print("You lose!", end="\n\n")
                return 0
        elif total_dealer == total_player:
            return 2
        # else:
        #     print("Got it")

        time.sleep(0.5)

            #CHECKING FOR RESULT WITH PLAYER'S CARDS.......................
        if total_player > 21:
            print("Bust!", end="\n\n")
            return 0
        elif total_player == 21:
            print("Blackjack!", end="\n\n")
            return 1
        elif check_for_ace(draw["player"]) and total_player == 11:
            print("Blackjack!", end="\n\n")
            return 1
        else:
            current_dealer_card = list(draw["dealer"].keys())[-1]
            draw["dealer"][current_dealer_card + 1] = ["dealer" + str(current_dealer_card + 1), str(random.randint(1, 14))]
            print(f"Dealer's next card is {cards[draw['dealer'][current_dealer_card + 1][1]][0]}")

        total_dealer = calc_total(draw["dealer"])
        print(f"Dealer total: {total_dealer}")
        
        if total_dealer > 21:
            print("Dealer bust! You win!", end="\n\n")
            return 1
        elif total_dealer == 21:
            print("Dealer blackjack! You lose!", end="\n\n")
            return 0
        elif check_for_ace(draw["dealer"]) and total_dealer == 11:
            print("Dealer blackjack!", end="\n\n")
            return 2

def hitStand():
    while True:
        hitStand = input("Would you like to hit or stand? Please type H or S. ")
        if hitStand.lower() == "h":
            return True
        elif hitStand.lower() == "s":
            return False
        else:
            print('Please type either "H" or "S"')

if __name__ == "__main__":
    main()
