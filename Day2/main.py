#Data types

#String
#    "Hello"[] inside square brace we can put the possition (a index of a letter)
# print("Gello"[0])

# print("123" + "345")

#Integer
# 123 + 345
# print(123_456_789)

#Float
# 3.14

#Boolean
#  True or false

# num_char = len(input("What is your name ? "))
#
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters")
# print(type(num_char))

#Data types exercise
# two_digit_number = input("Type a two digit number: ")
# print (int(two_digit_number[0]) + int(two_digit_number[1]))


# print(3 * (3 + 3) / 3 - 3)

# Write a program that calculates the Body Mass Index(BMI) from a user
#  Normal BMI sould be between 18.5 and 25
#  overweight is when BMI is higher than 25
#  overweight is when BMI is higher than 25

# # height = input("enter your height in m: ")
# weight = int(input("enter your weight in kg: "))
# # #  The formula for BMI is weight(kg)/(height**2)
# # print("your BMI is = " + str(float(weight)/float(height)**2))
#
# # f-String
# print(f"your weight is {weight}")
ex = int(input("Waht exercise do you want to run? "))
if( ex == 1):
    age = int(input('Your acctuar age is = '))
    print(f"You have {(80 - age) * 365} days, {4000 - age * 52} weeks, and {(80 - age) * 12} months left.")
elif ex == 2:
    print("Welcome to the tip calculator.")
    total_bill = float(input("What was the total bill? $"))
    procent_tip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
    while procent_tip != 10 and procent_tip != 12 and procent_tip != 15:
        procent_tip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
    persons = int(input("How many persons to spit the bill? "))
    print(f'Each person shoudl pay : ${"{:.2f}".format(round((total_bill / persons) * (1 + procent_tip/100), 2))}')


#     Ex2 if the bill was $150.00, split between 5 people with 12% tip.
#       Each person should pay( 150.00) / 5) * 1.12
# Your life in weeks













