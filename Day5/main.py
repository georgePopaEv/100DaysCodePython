# fruits = ['Apple', 'Peach', 'Pear']
# for fruit in fruits:
#     print(fruit)
'''The average of list of students' heigth'''
# student_heights = input("Input a list of students heoghrs ").split()
# total_height = 0
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#     total_height += student_heights[n]
#
#
# print(round(total_height/len(student_heights)))

# You are going to write a program that calculates the highest score from a list of scores
# students_scores = input("Insert list of students score :").split()
# max_value = -1
# for x in students_scores:
#     x = int(x)
#     if x > max_value:
#         max_value = x;
#
# print(f"The highest score in the class is: {max_value}")
# print(type(students_scores[0]))

# total = 0
# for number in range(2,101,2):
#     total += number
#
# print(total)

# Fizz for number divisible with 3
# Buzz for number divisible with 5
# FizzBuzz for number divisible both 3 and 5

# for i in range(1,101):
#     if i%3 ==0 and i %5 == 0:
#         print("FizzBuzz")
#     elif i%3 ==0:
#         print("Fizz")
#     elif i%5 ==0:
#         print("Buzz")
#     else:
#         print(i)

'''Password Generator '''
import random as r
letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
numbers = '0 1 2 3 4 5 6 7 8 9'.split()
symbols = '! # $ % & ( ) * +'.split()
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password\n"))
C_letters = input("Do yoy need at least one Upper case ? Y or N ").lower()
nr_symbols = int(input("How many symbols would you like in your password\n"))
nr_numbers = int(input("How many numbers would you like in your password\n"))
password = ''
list_of_choice = [0,1,2]
for i in range(1, nr_letters+nr_numbers+nr_symbols + 1):
    lsn = r.choice(list_of_choice)
    if lsn == 0 and nr_letters:
        nr_letters -=1
        if nr_letters == 0:
            list_of_choice.remove(0)
        if C_letters == 'y':
            password += letters[r.randint(26,len(letters)-1)]
            C_letters = ''
        else:
            password += letters[r.randint(0, len(letters) - 1)]
    elif lsn == 1 and nr_numbers:
        nr_numbers -= 1
        if nr_numbers == 0:
            list_of_choice.remove(1)
        password += numbers[r.randint(0, len(numbers) - 1)]
    elif lsn == 2 and nr_symbols:
        nr_symbols -= 1
        if nr_symbols == 0:
            list_of_choice.remove(2)
        password += symbols[r.randint(0, len(symbols) - 1)]

print(password)
