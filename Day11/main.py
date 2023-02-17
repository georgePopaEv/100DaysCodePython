import rules as rl
# I could make a dictionair with key as name and value list of cards
'''
    players = {
        'computer':{    'cards': []
                        'isPlaying' : True/False
                        'balance' : float  3512.021
                        'bet' : float
                        'wantMoreCards' : True/False
                },
        'name1':{       'cards': []
                        'isPlaying' : True/False
                        'balance' : float  3512.021
                        'bet' : float
                        'wantMoreCards' : True/False
                },
    }
'''
players = rl.create_table_of_players()
rl.add_a_dealer_to_this_table(players)



# print(players)
print("Welcome to the best game of BlackJAck from World \n")
score = []
while True:
    if rl.stop_game():
        break
    rl.add_new_player(players)

    print("The cards are splitting ..... Wait a second to finish")
    rl.deal_cards_for_all_players(players)
    print("The cards have been splitted...") # Cartile au fost impartite
    rl.show_cards(players)
    for player in players:
        if player == "computer":
            continue
        #     big funtion with analize score of player and encapsulatel all below function in it
        rl.check_for_AS(players, player)
        if rl.check_21_2cards(players, player):
            print(f"Wooooow , we have a BlackJack, Congrats {player }your bet was doubled and returned into your balance")
            players[player]['wantMoreCards'] = False
            players['computer']['nrLost'] += 1
        while players[player]['wantMoreCards'] and rl.calc_score(players,player)<= 21:
            take_or_not = input(f"{player} have {players[player]['cards']} cards , Do you want to take one card ? Y or N ").lower()
            if take_or_not == 'n':
                players[player]['wantMoreCards'] = False
            else:
                rl.add_one_more_card(players[player])
                rl.check_for_AS(players,player)
        if rl.calc_score(players,player) > 21:
            print(f"You are out with {players[player]['cards']} care au suma {sum(players[player]['cards'])}")
            players[player]['wantMoreCards'] = False
            players[player]['BUSTED'] = True
    # Here the dealer begin to show his cards and try to do all his best to win
    rl.run_dealer(players)
    # rl.run_dealer(players)

    # To do for each player to add card if they need to win