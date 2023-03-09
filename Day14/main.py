'''
In day 14 i have to make an game like higher Lower
And compare 2 celebrity followers
'''

import data as d
import random as r

def match(p1, p2):
    print(f'{p1["name"]} is a {p1["description"]} from {p1["country"]} \n {d.vs_logo}')
    print(f'{p2["name"]} is a {p2["description"]} from {p2["country"]}')

def compare(p1,p2):
    if p1['followers'] > p2['followers']:
        return 'l'
    else:
        return 'h'
def guess_H_or_L(result_compare):
    h_or_l = input("H or L").lower()
    if h_or_l == result_compare:
        return True

high_score = 0
score = 0
data = d.data

p1 = r.choice(data)
while True:
    p2 = r.choice(data)
    match(p1,p2)
    if guess_H_or_L(compare(p1,p2)):
        score +=1
        p1 = p2
    else:
        if input(f"You have lost with {score} score , sorry, If you want to continue press Y or N to finish the game").lower() == 'n':
            break
        else:
            score = 0
            p1 = r.choice(data)


