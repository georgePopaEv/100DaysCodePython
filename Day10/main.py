def format_name(first_name:str, last_name):
    return (first_name + " " + last_name).capitalize()


# print(format_name("george", "popa"))

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def days_in_month(year, moth):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year) and moth==2:
        return 29
    return month_days[moth-1]

# Calculator project
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1- n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations ={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

# print(operations["+"](2,3))
num1 = int(input("What it is first number? : "))
operations_symbol = '+ - / *'.split()

while True:
    cont = input("Do you want to continue ? Y or N").lower()
    if cont == 'n':
        break
    num_next = int(input("What it next number? : "))
    operation_symbol = input(
        "Ce operatie doresti sa faci cu aceste 2 numere \n + \n - \n * \n / \n Te rog alege :").lower()
    ans = operations[operation_symbol](ans,num_next)
    print(f"The result of {operation_symbol} is \n {ans}")

print(f'The pr0gram has ended and last result is {ans}')