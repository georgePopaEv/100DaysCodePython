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

total = 0
for number in range(2,101,2):
    total += number

print(total)