import math
def greet():
    print("hello")
    print("Buna")
    print("Bonjour")
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

def greet_with(name, location):
    print(f"Hello {name} from {location}")

def paint_calc(height, width, cover):
    print(f'You will need {math.ceil(height*width/cover)} cans of paint')

def prime_checker(number):
    for i in range(2,number//2+1):
        if number % 2 == 0:
            return 'It\'s not a prime number'
    return 'It\'s a prime number'

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height = test_h, width = test_w, cover = coverage)

# print(prime_checker(18))

def encrypt(text, shift_amount):
    text_nou = ''
    for i in text:
        text_nou += alphabet[alphabet.index(i) + shift_amount]
    print(f"The encrypted text is {text_nou}")
def decrypt(text, shift_amount):
    text_nou = ''
    for i in text:
        text_nou += alphabet[alphabet.index(i) - shift_amount]
    print(f"The decoded text is {text_nou}")



#           0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type shift number:\n"))

# if direction == 'encode':
#     encrypt(text,shift)
# elif direction == 'decode':
#     decrypt(text,shift)
def caesar(start_text, shift_amount, cipher_direction):
    ent_text = ''
    if shift_amount > 26:
        shift_amount = 45%26
    if cipher_direction == "decode":
        shift_amount *= -1
    for i in start_text:
        if i.isalpha():
            ent_text += alphabet[alphabet.index(i) + shift_amount]
        else:
            ent_text += i
    print(f"The {cipher_direction}d text is {ent_text}")

caesar(text,shift,direction)
























