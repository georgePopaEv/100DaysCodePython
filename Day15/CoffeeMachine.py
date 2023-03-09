import  time
coffe_recipe = {
    'espresso': {
        'Water' : 100,
        'Milk' : 50,
        'Coffee' : 16,
        'Money' : 2
    },
    'latte': {
        'Water' : 200,
        'Milk' : 150,
        'Coffee' : 24,
        'Money' : 3
    },
    'cappuccino': {
        'Water' : 100,
        'Milk' : 75,
        'Coffee' : 31,
        'Money' : 2.5
    }
}

coffe_machine ={
    'Water' : 1000,
    'Milk' : 500,
    'Coffee' : 450,
    'Money' : 0,
    'profit':0
}

def report():
    for key in coffe_machine:
        if key != 'profit':
            print(coffe_machine[key])

def turn_off():
    print("The machine is turning off.")

def check_report():
    for ing in coffe_machine:
        if ing != 'profit':
            print(f'{ing} = {coffe_machine[ing]}')
def check_resources(inp_type_coffee):
    chosen_coffee = coffe_recipe[inp_type_coffee]
    for ing in chosen_coffee:
        if chosen_coffee[ing] >coffe_machine[ing] and ing != 'Money':
            print(f'I am so sorry there is not enough {ing} please call a person from staff')
            return False
    for ing in chosen_coffee:
        if ing != 'Money':
            coffe_machine[ing] -= chosen_coffee[ing]
    return True

def check_money(inp_type_coffee):
    chosen_coffee = coffe_recipe[inp_type_coffee]
    if chosen_coffee['Money'] > coffe_machine['Money']:
        print(
            f'You have to insert more coins. In machine you have inserted {coffe_machine["Money"]} and for this type you need to pay {chosen_coffee["Money"]}')
        return False
    else:
        coffe_machine['profit'] +=  chosen_coffee['Money']
        coffe_machine['Money'] -= chosen_coffee['Money']
        return True

def prompt():
    prop = input("What would you like ? espresso/latte/cappucino \n use 'report' function to know resource of machine \n").lower()
    return prop

def processing_coffe(coff):
    if check_resources(coff):
        print(f"You have to insert {coffe_recipe[coff]['Money']}")
        sum_inserted = 0
        while True:
            ins = input("please insert coins")
            if ins.isdigit()  == False or ins.isdecimal() == False:
                break
            sum_inserted += float(ins)
        coffe_machine['Money'] += sum_inserted
        if check_money(coff):
            print("The coffee is processing please wait until the end")
            for i in range(5):
                print('..', end='')
                time.sleep(0.5)
            print()
