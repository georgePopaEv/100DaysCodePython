import random
import hangman_game as hg

chosen_word = list(random.choice(hg.world_list))
letters = hg.letters
lifes = 6
final_word = []
for i in chosen_word:
    final_word.append('_')
print(final_word)
while lifes> 0 and final_word != chosen_word:
    ask_for_a_letter = input("Guess a letter please : ").lower()
    if ask_for_a_letter not in letters:
        print("You already have intered this letter you have lost a life Sorry ")
        lifes-=1
    else:
        letters.remove(ask_for_a_letter)
        if ask_for_a_letter in chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == ask_for_a_letter:
                    final_word[i]  = ask_for_a_letter
        else:
            print("I am sorry but this letter doesn't exists in this word")
            lifes-=1
    print(hg.stages[lifes])
    print(''.join(final_word))
if lifes > 0:
    print(f"Congratulation you have guessed the word and remain with {lifes} lifes")
else:
    print(f"Sorry but you didn;t guess the word, It was {''.join(chosen_word)}")