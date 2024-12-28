import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
player_hand = []
dealer_hand = []

def calculate_score(player_hand, dealer_hand):
    player_score = sum(player_hand)
    dealer_score = sum(dealer_hand)
    return player_score, dealer_score

def deal_cards():
    player_hand.append(random.randint(1,11))
    player_hand.append(random.randint(1,11))
    if 11 in player_hand and sum(player_hand) > 21:
        i = player_hand.index(11)
        player_hand[i] = 1
    dealer_hand.append(random.randint(1,11))
    dealer_hand.append(random.randint(1,11))
    if 11 in dealer_hand and sum(dealer_hand) > 21:
        i = dealer_hand.index(11)
        dealer_hand[i] = 1
    return player_hand, dealer_hand

def hit(player_hand):
    player_hand.append(random.randint(1, 11))
    if 11 in player_hand and sum(player_hand) > 21:
        i = player_hand.index(11)
        player_hand[i] = 1
    return player_hand



check = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if check == "n":
    print()
else:
    deal_cards()
    player_score, dealer_score = calculate_score(player_hand, dealer_hand)
    print(logo)
    if dealer_score == 21:
        print("Dealer has blackjack. You Lose!")
    elif player_score == 21 and dealer_score != 21:
        print("You got blackjack. You win!")
    else:
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {dealer_hand[0]}")
    #The next part of the game

        should_continue = True

        player_should_continue = True
        while player_should_continue:
            play = input("Type 'y' to get another card, type 'n' to pass: ")
            if play == 'y':
                hit(player_hand)
                player_score, dealer_score = calculate_score(player_hand, dealer_hand)
                print(f"Your cards: {player_hand}, current score: {player_score} ")
                print(f"Computer's first card: {dealer_hand[0]}")
                if player_score > 21:
                    player_should_continue = False
                    print("You went over. You Lose")
                elif player_score == 21:
                    player_should_continue = False
                    print("You got blackjack. You win!")
            elif play == 'n':
                player_should_continue = False
                dealer_should_continue = True
                while dealer_should_continue:
                    if dealer_score < 16:
                        hit(dealer_hand)
                        player_score, dealer_score = calculate_score(player_hand, dealer_hand)
                    if dealer_score >= 16:
                        dealer_should_continue = False
                        calculate_score(player_hand, dealer_hand)
                        if dealer_score > 21:
                            print(f"Dealer went over. You win! Congrats!")
                        elif player_score>dealer_score:
                            print(f"Dealer score was: {dealer_score} You win! Congrats!")
                        elif player_score == dealer_score:
                            print(f"Dealer score was: {dealer_score} It's a draw!")
                        elif player_score < dealer_score:
                            print(f"Dealer score was: {dealer_score} You lose!")





