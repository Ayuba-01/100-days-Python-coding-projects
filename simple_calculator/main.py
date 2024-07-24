from logo import logo
def addition(n1,n2):
    """Accepts 2 numbers and return the addition of the numbers"""
    return n1 + n2

def subtraction(n1,n2):
    """Accepts 2 numbers and return the subtraction of the second number from the first number"""
    return n1 - n2

def division(n1,n2):
    """Accepts 2 numbers and return the division of the second number from the first number"""
    return n1 / n2

def multiplication(n1,n2):
    """Accepts 2 numbers and return the multiplication of the numbers"""
    return n1 * n2

operations = {"+" : addition, "-" : subtraction, "/" : division, "*" : multiplication}

def calculator():
    print(logo)
    again = True
    num1 = int(input("Enter first number: "))
    while again:
        for key in operations:
            print(key)
        operation = input("choose operation: ")
        num2 = int(input("Enter next number: "))
        calc_functions = operations[operation]
        result = calc_functions(num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        answer = input("Do you want to continue calculation with your previous answer. Enter 'y' for Yes and 'n' for No.: ").lower()
        if answer == "n":
            again = False
            print("Thank you!")
        else:
            num1 = result
        



calculator()
