import random as ra
import mymodule as mm

# print(ra.randint(10,20))
# print(ra.randrange(10,20))
# print(mm.pi)

# random_float = ra.random() * 5
# print(random_float)

# Ex1 head or tails
# if ra.randint(0,1) == 1:
#     print("Head")
# else:
#     print("Tails")

# states_of_America = ["Delaware", "Pennsylvania", "Arizona", "New Jersey", "Georgia"]

# '''
#     Example input:
#         Angela, Ben, Jenny
#     Example Output:
#         Angela is going to buy meal today
# '''
#
# list_of_names = input("Give me everybody's names, separated by a comma. \n").split(", ")
#
# print(f'{list_of_names[ra.randint(0,len(list_of_names)-1)]} is going to buy meal today')

# row1 = [' ', ' ', ' ']
# row2 = [' ', ' ', ' ']
# row3 = [' ', ' ', ' ']
#
# map = [row1, row2, row3]
# print(f'{row1}\n{row2}\n{row3}')
# position= input("Where do you want to put the treasure? column and row ")
# i = int(position[1])-1
# j = int(position[0])-1
#
# map[i][j] = 'X'
# print(f'{row1}\n{row2}\n{row3}')


# Final Project Rock paper scissors

signs = [
'''
    _______
___.   ____)
       (_____)
       (_____)
       (____)
----.__(___)
        ''',
'''
    _______
___.   ____)____
         _______)
         ________)
          ______)
----._________)
        ''',
'''
    _______
___.   ____)____
         _______)
       __________)
       (____)
----.__(___)
        '''
          ]

user_choice = int(input("What to you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer_choice = ra.randint(0,2)
print(f"Computer chose {computer_choice} \n {signs[computer_choice]}")

if user_choice >=3 or user_choice < 0:
    print("Invalid number, you lose")
elif computer_choice == 2 and user_choice == 0:
    print("You win")
elif computer_choice > user_choice:
    print('you lose')
elif computer_choice < user_choice:
    print('you Win')
elif computer_choice == user_choice:
    print("Draw")
