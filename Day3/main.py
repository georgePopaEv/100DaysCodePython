# Ex 1
'''
print("Welcome to the rollercoster!")
heoght = int(input("what is yout height in cm? "))
bill = 0;
if heoght >= 120:
    print("You can ride the rollercoster!")
    age = int(input("waht is your age? "))
    if age >=45 and age <= 55:
        print("You enjoy of a free ride. Have enjoy")
    elif age > 18:
        print("You will pay 12$")
        bill = 12
    elif age < 12:
        print("You will pay 5$")
        bill = 5
    else:
        bill = 7
        print("You will pay 7$")
    wants_photo = input("Do you want a photo taken> Y or N.?")
    if wants_photo.upper() == "Y":
        bill += 3
    print(f'You finally will pay ${bill}')
else:
    print("Sorry, you have to grow taller before you can ride")

# Ex 2
number = int(input("which number do you want to check?"))
if number%2==0:
    print("This is an even number")
else:
    print("This is an odd number")
'''


'''
# Leap year
year = int(input("enter the age"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The year is a leap")
        else:
            print("The year is not a leap")
    else:
        print("The year is a leap")
else:
    print("The year is not a leap")
'''


'''
Ex 3
print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want ? S, M or L ")
add_peperoni = input("Do you want to add peperonu ? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
price = 0

if size.upper() == "S":
    price += 15
elif size.upper() == 'M':
    price += 20
elif size.upper() == 'L':
    price += 25

if add_peperoni.upper() == 'Y' and size.upper() == "S":
    price += 2
else:
    price += 3

if extra_cheese.upper() == 'Y':
    price += 1

print(f'Your final bill is ${price}')
'''

#  Love calculator
'''Example 
George
Alina
T - 0       L - 1
R - 1       O - 1
U - 0       V - 0
E - 2       E - 2
    3           4    => 34 
'''
'''
print("Welcome to the Love Calculator!!")
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()
cnt1 = name1.count('t') + name1.count('r') + name1.count('u') + name1.count('e') + \
       name2.count('t') + name2.count('r') + name2.count('u') + name2.count('e')
cnt2 = name1.count('l') + name1.count('o') + name1.count('v') + name1.count('e') + \
       name2.count('l') + name2.count('o') + name2.count('v') + name2.count('e')
score = int(str(cnt1)+ str(cnt2))
if score < 10 or score > 90 :
    print(f"Your socre is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your socre is {score}, you are alright together.")
else:
    print(f'Your score is {score}.')
'''

# Final Project
print("Welcome to Treasure Island. \n Your mission is to find the treasure.")
first_choice = input('This is first choice, where do you want to go? Type "left" or "right".').lower()
if first_choice == 'right':
    print("You fell into a hole. Game Over")
else:
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "Swim" to swim across.').lower()
    if choice2 == 'swim':
        print("You got attacked by an angry shark. Game Over.")
    else:
        choice3 = input('You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.'
                        'Which colour do you choose?').lower()
        if choice3 == 'red':
            print("It's a room full of fire. Game Over.")
        elif choice3 == 'yellow':
            print("You found the treasure! You Win!")
        elif choice3 == 'blue':
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")