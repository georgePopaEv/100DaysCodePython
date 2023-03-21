# List Comprehension

# simple new list =>>> new_list = [new_item for item in list]
# even numbers    =>>> even_nums = [n*2 for n in range(1,5)]

# Conditional List Comprehension
# new_list = [new_item for item in list if test]


# names = ['Alex', "Beth", 'Caroline', 'Dave', 'Elanor', 'Freddie']
# short_names = [name for name in names if len(name) < 5]
# uppercase_names = [name.upper() for name in names if len(name) > 5]
#
# # Exercise 1
# # print all squared numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# squared_numbers = [n**2 for n in numbers]
# print(squared_numbers)

# Exercise 2 -> Print all even numbers
# result = [n for n in numbers if n%2==0]
# print(result)

# f1 = open("file1.txt")
# f2 = open("file2.txt")
# rows_f1 = f1.readlines()
# rows_f2 = f2.readlines()
# f1.close()
# f2.close()
# rows_f1 = [int(n.strip('\n')) for n in rows_f1]
# rows_f2 = [int(n.strip('\n')) for n in rows_f2]
#
# f_result = [ n for n in rows_f1 if n in rows_f2]
# print(rows_f1)
# print(rows_f2)
# print(f_result)

# Dictionary Comprehension
# new_dict = {new_key: new_value for (key,value) in dict.items() if test}

# Exercise 1
# Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}
# print(result)

# Exercise 2
# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature
# in degrees Celcius and converts it into degrees Farenheight
# weather_c ={
#     'Monday' : 12,
#     'Tuesday' : 14,
#     'Wednesday' : 15,
#     'Thursday' : 14,
#     'Friday' : 21,
#     'Saturday' : 22,
#     'Sunday' : 24
# }
#
# weather_f = {key:value * 9/5 + 32 for (key,value) in weather_c.items()}
#
# print(weather_f)

# import pandas
# student_dict = {
#     "Students" : ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
# student_data_frame = pandas.DataFrame(student_dict)
# # print(student_data_frame)
#
#
# # Loop through a  data Frame
# # for (key,value) in student_data_frame.items():
# #     print(value)
#
# # Loop through rows of a data Frame
# for (index, row) in student_data_frame.iterrows():
#     print(row.Students)









# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas
df_alphabet_phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_alphabet_phonetic_words = {row.letter:row.code for (index,row) in df_alphabet_phonetic.iterrows()}
print(dict_alphabet_phonetic_words)
#. Create a list of the phonetic code words from a word that the user inputs.
name_input = input("What name do you want to spell it ? : ").upper()
list_phonetic_word_spelled_name = [dict_alphabet_phonetic_words[letter] for letter in name_input]
print(list_phonetic_word_spelled_name)



