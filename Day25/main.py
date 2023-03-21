# data = open("weather_data.csv").readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
#
# print(temperatures)
# print(type(data))

# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data['temp']))
# data_dict = data.to_dict()
# print(data_dict)
#
# temperatures = data["temp"].to_list()
# print(temperatures)
# print("The average of temperature is {}/{} = {:.2f}".format(sum(temperatures),len(temperatures),sum(temperatures)/len(temperatures)))
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get data in column
# print(data['condition'])
# print(data.condition)
#
# # Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# # print("{} Celsius into {} Fahrenheit".format(monday.temp.to_list()[0], (monday.temp.to_list()[0] * 9/5) + 32))
#
# data_dict = {
#     "Students": ["Amy", "James", "Angela"],
#     "Scores":[76, 56, 65]
# }
# data_from_dict = pandas.DataFrame(data_dict)
# print(data_from_dict)
# data_from_dict.to_csv("Students_list.csv")

# import pandas
# # Read all data from CSV and trasfer to DF
# data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
#
# # from DF extract only usefull data , to be more precise we will extract only prymary Fur Color and convert to a list
# primary_full_col = data["Primary Fur Color"].to_list()
#
# # Here we filter and select only original value from that list of colors result being all collors which are appearing in column
# colors = set(primary_full_col)
#
# # This How will looking final table , we will have 2 columns
# dict_collors = {
#     "Fur Color" : [],
#     "Count": []
# }
#
# # For each collor from original collors we will add and count how many times apear in file
# for coll in colors:
#     if type(coll) != type(2.4) :
#         dict_collors["Fur Color"].append(coll)
#         dict_collors["Count"].append(primary_full_col.count(coll))
#
# # Convert dict to a table ,
# df_final = pandas.DataFrame(dict_collors)
#
# # Once we have all date grouped into a DF it is prety straigtforward to export into a csv
# # df_final.to_csv("Table_chalange.csv")

import pandas
from turtle import Turtle,Screen

my_screen = Screen()
my_screen.setup(width=730, height=500)
my_screen.title("U.S States Game")
my_screen.bgpic("blank_states_img.gif")
scrie = Turtle("turtle")
scrie.penup()
scrie.hideturtle()


state_50 = pandas.read_csv("50_states.csv")
list_states = state_50.state.to_list()
print(list_states)
def check_among_50(answer):
    if answer in list_states:
        return True
    else:
        return False
def get_coordonates_input(answe):
    row_input = state_50[state_50.state == answe]
    coord_state = [int(row_input.x), int(row_input.y)]
    return coord_state


runing_game = True

list_coordonates = []
while runing_game:
    answer_input = my_screen.textinput("Guess the State", "What's another state's name?").title()
    if check_among_50(answer_input):
        list_coordonates = get_coordonates_input(answer_input)
        scrie.goto(list_coordonates[0],list_coordonates[1])
        scrie.write(f"{answer_input}", align="center", font=("Courier", 8, "normal"))
    else:
        runing_game = check_among_50(answer_input)
    print(list_coordonates)





# print(f"{row_input.x}  and {row_input.y}")






my_screen.exitonclick()
