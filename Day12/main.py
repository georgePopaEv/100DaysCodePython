# def increase_enemies():
#     enemies = 2
#     print(f'Enemies inside function: {enemies}')
#
# increase_enemies()
# print(f'Enemies outside function: {enemies}')
#
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
# print(potion_strength)

# # Global Scope
# player_health = 10
# def drink_potion():
#     potion_strength = 2
#     print(player_health)
#
# # drink_potion()
# enemies = 1
# def increase_enemy():
#     return enemies + 1


# Global constant
# PI = 3.14159
# URL = "https://www.google"
logo ='''
  ___  _  _  ____  ____   ____    ____  _  _  ____    __ _  _  _  _  _  ____  ____  ____ 
 / __)/ )( \(  __)/ ___) / ___)  (_  _)/ )( \(  __)  (  ( \/ )( \( \/ )(  _ \(  __)(  _ \ 
( (_ \) \/ ( ) _) \___ \ \___ \    )(  ) __ ( ) _)   /    /) \/ (/ \/ \ ) _ ( ) _)  )   /
 \___/\____/(____)(____/ (____/   (__) \_)(_/(____)  \_)__)\____/\_)(_/(____/(____)(__\_)'''

print(logo)
print("Welcome to GUESS THE NUMBER game")
import random as r
def choose_dificulty():
    dificulty = input("Please choose the dificulty for this time. Type 'hard' or 'easy' ").lower()
    while dificulty != 'hard' and dificulty != 'easy':
        dificulty = input("I could not recocnize the dificulty try again. Type 'hard' or 'easy' ").lower()
    return dificulty

def run_guess_game(attemps):
    r_numb = r.randint(1,101)
    g_number = -1
    while attemps and r_numb != g_number:
        attemps -= 1
        g_number = int(input("Guess the number please"))
        if g_number < r_numb:
            print(f"Too low ->> You remain with nr {attemps}")
        elif g_number > r_numb:
            print(f"Too high ->> You remain with nr {attemps}")
        else:
            print(f'Congrats, you have guessed the number I was thinking')

    if attemps == 0:
        print("You lost")
    return r_numb



while True:
    if choose_dificulty() == 'easy':
        run_guess_game(10)
    else:
        print(f"The number was {run_guess_game(5)}")

    if input("You have finished the game do you want to play again? Y ot N").lower() =='n':
        break


