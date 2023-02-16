world_list = ['ardvark', 'baboon', 'camel']
stages = ['''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========
''',
'''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========
''',
'''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========
''',
'''
   +---+
   |   |
   O   |
   |\  |
       |
       |
=========
''',
'''
   +---+
   |   |
   O   |
   |   |
       |
       |
=========
''',
'''
   +---+
   |   |
   O   |
       |
       |
       |
=========
''',
'''
   +---+
   |   |
       |
       |
       |
       |
=========
''']
letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
# print(f'suntem la comparatie iar chose[{i}]={chosen_word[i]}, and final_word[{i}] = {final_word[i]}')
# final_word = final_word[:i] + ask_for_a_letter + final_word[i + 1:]