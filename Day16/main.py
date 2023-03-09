# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('coral1')
# timmy.forward(100)
#
# tommy = Turtle()
# tommy.shape('turtle')
# tommy.left(120)
# tommy.fd(100)
#
# my_screen = Screen()
# my_screen.exitonclick()
# print(my_screen.canvheight)
#
# import prettytable
# x = prettytable.PrettyTable()
# x.add_column('Name', ['Popa', 'Bujenita'])
# x.add_column('Prenume', ['George', 'Alina'], align='l')
# print(x)
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money = MoneyMachine()
coff = CoffeeMaker()
while True:
    ans = input(f"What exactly do you want to serve? {menu.get_items()}")
    if ans =='off':
        print('The machine is turning off')
        break
    elif ans =='report':
        money.report()
        coff.report()
        ans = input(f"What exactly do you want to serve? {menu.get_items()}")
    ans = menu.find_drink(ans)
    if ans not in menu.menu:
        continue
    else:
        if coff.is_resource_sufficient(ans) and money.make_payment(ans.cost):
            coff.make_coffee(ans)


