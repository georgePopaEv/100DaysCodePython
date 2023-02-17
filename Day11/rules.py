import random as r
import math

card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# card =[11, 11, 11, 10, 11, 10, 11, 11, 10, 10, 10, 10, 10]
# card =[11, 11,11,11,11,11,11,11,11,11,11]
def create_table_of_players():
    players = {}
    return players


def add_a_dealer_to_this_table(players):
    players['computer'] = {}
    players['computer']['cards'] = []
    players['computer']['nrPlayers'] = 0
    players['computer']['nrLost'] = 0


def deal_cards(pr):
    """This function manage the cards to be dealed for one player
    Receive a list and will add 2 cards for each list received"""
    pr.append(r.choice(card))
    pr.append(r.choice(card))


def deal_cards_for_all_players(dict_players):
    for player in dict_players:
        dict_players[player]["cards"] = []
        dict_players[player]["wantMoreCards"] = True
        dict_players[player]["bet"] = True
        dict_players[player]["BUSTED"] = False
        deal_cards(dict_players[player]["cards"])


def add_one_more_card(pr):
    pr['cards'].append(r.choice(card))


def check_21_2cards(players, player):
    if sum(players[player]['cards']) == 21 and len(players[player]['cards']) == 2:
        return True
    return False


def check_21(pr):
    if sum(pr) == 21:
        return True
    return False


def clear_cards(dict_player):
    """this fucntions is going to clear all cards for each player"""
    for key in dict_player:
        dict_player[key] = []


def calc_score(players, player):
    return sum(players[player]['cards'])


def add_new_player(players):
    """This function ask dealer if there is new players on table to know to add on our dictionair"""
    while input("There is new player on this game? Y or N ?").lower() == 'y':
        players['computer']['nrPlayers'] += 1
        new_name = input("Care este numele noului jucator? ").title()
        players[new_name] = {'cards': [],
                             'isPlaying': True,
                             'wantMoreCards': True,
                             'BUSTED': False,
                             'bet': 0,
                             'balance': 0
                             }
        # balance = input("How much money do you want to invest in our casino? ").split('.')
        # balance = float(balance[0] + '.' + balance[1][:2])
        # players[new_name]['balance'] = balance



def check_for_AS(players, player):
    if calc_score(players, player) > 21 and 11 in players[player]['cards']:
        players[player]['cards'].remove(11)
        players[player]['cards'].append(1)
        if calc_score(players, player) > 21 and 11 in players[player]['cards']:
            players[player]['cards'].remove(11)
            players[player]['cards'].append(1)


def stop_game():
    "Ask the player if he wants to continue"
    if input("Do you want to play and continue the game? N or Y ").lower() == 'n':
        return True


def show_cards(players):
    for player in players:
        if player == "computer":
            print(f'First computer\'s card is {players[player]["cards"][0]}')
            continue
        print(f"For player {player} you have {players[player]['cards']}")


def show_players_cards(players):
    for player in players:
        if player == "computer":
            continue
        print(f"For player {player} you have {players[player]['cards']}")


def show_card_for_one_player(players, player):
    return players[player]['cards']


def run_dealer(players):
    print(show_card_for_one_player(players,'computer'))
    while input("Dealer? do you want more cards?").lower() == 'y':
        add_one_more_card(players['computer'])
        check_for_AS(players, 'computer')
        print(show_card_for_one_player(players,'computer'))
        if calc_score(players, 'computer') > 21:
            break
    if calc_score(players, 'computer') > 21:
        print("ALL players won , DEALER BUSTED")
    else:
        for player in players:
            if player == "computer":
                continue
            if calc_score(players, player) > calc_score(players, 'computer') and not players[player]['BUSTED']:
                print(f"{player} WON agains dealer ")
            elif calc_score(players, player) == calc_score(players, 'computer'):
                print(f"{player} DRAW agains dealer ")
            else:
                print(f"{player} LOST agains dealer ")


# def run_dealer(players):
#     print(f"The dealer show his cards \n {players['computer']['cards']} "
#           f"\n {players['computer']['nrLost']}"
#           f"\n {players['computer']['nrPlayers']}")
#     score_wins_draws_loss = calc_how_lose(players)
#     score_wins_draws_loss[2] += players['computer']['nrLost']
#     print("final dealer")
#     print(f"{score_wins_draws_loss} and {players['computer']['nrLost']}")
#     # print(score_wins_and_draws) # will print a set of date first position represent number of wins agains player and second one number of draws
#     while score_wins_draws_loss[0] <= players['computer']['nrLost'] and score_wins_draws_loss[1] < :
#         print(score_wins_draws_loss)
#         print("The dealer will take a card")
#         add_one_more_card(players['computer'])
#         print(players['computer']['cards'])
#         if calc_score(players,'computer')> 21:
#             print("All players won")
#             break
#         score_wins_draws_loss = calc_how_lose(players)
#     # players['computer']['nrWins'] will contain number of players remained in game

def calc_how_lose(players):
    sdealer = calc_score(players, 'computer')
    wins_draws_loss = [0, 0, 0]
    for player in players:
        if player == "computer":
            continue
        if sdealer > calc_score(players, player):
            wins_draws_loss[0] += 1
        elif sdealer == calc_score(players, player):
            wins_draws_loss[1] += 1
        else:
            wins_draws_loss[2] += 1

    return wins_draws_loss
