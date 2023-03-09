import CoffeeMachine as coffeM

# coffeM.report()
# coffeM.check_resources('espresso')


while True:
    inp = coffeM.prompt()
    if inp == 'off':
        coffeM.turn_off()
        break
    elif inp == 'report':
        coffeM.check_report()
    else:
        coffeM.processing_coffe(inp)