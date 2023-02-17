'''programming_dictionary = {
    "Bug":"An error in a program that prevents the program from running as expected.",
    "Function":"A piece of code that you can easily call over and over again"
}

# print(programming_dictionary["Function"])

programming_dictionary["Loop"] = "The accytion of doing something over and over again."


empty_dictionary = {}
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

travel_log = [
    {"country":"France" ,
        "cities_visited": ["Paris", "lille", "Dijon"],
         "visits" : 12
     },
    {"country":'Germany' ,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
         "visits": 12
     },
]
def add_new_Country(country_visited, time_visited, cities_visited):
    new_country = {}
    new_country["country"] =country_visited
    new_country["cities_visited"] =cities_visited
    new_country["visits"] =time_visited
    travel_log.append(new_country)


add_new_Country("Croatia", 22, ["Zalsburg"])
# print(travel_log)
'''
import art
bid_dict ={}
print(art.logo)
run = True
max_bid = 0
max_name = ''
while run:
    name = input("What is your name ?").capitalize()
    bid = int(input("What it is your bid? "))
    bid_dict[name] = bid
    if bid > max_bid:
        max_bid = bid
        max_name = name
    ifrun = input("There is anywant to bid to this item ? Y or N").lower()
    if ifrun == 'n':
        run = False

print(f"The winner is {max_name} with a bid of {max_bid}")

