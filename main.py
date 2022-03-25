from art import logo


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculate():
    continue_cal = True
    print("---------------------------------------------------")
    print(logo)
    first_number = float(input("What is the first number?: "))

    while continue_cal:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        next_number = float(input("What is the next number?: "))
        function = operations[operation]
        result = function(first_number, next_number)

        print(f"{first_number} {operation} {next_number} = {result}")
        cont_cal = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if cont_cal == "n":
            calculate()
        elif cont_cal == "y":
            first_number = result
        else:
            print("Invalid Input.")


calculate()
