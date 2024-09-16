from art import logo
print(logo)


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    should_accumulate = True
    number_one = int(input("What's the first number? "))

    while should_accumulate:
        operator = input("+\n"
                         "-\n"
                         "*\n"
                         "/\n"
                         "Pick an operation: ")

        number_two = int(input("What's the next number? "))

        answer = operations[operator](number_one, number_two)
        print(f"{number_one} {operator} {number_two} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == 'y':
            number_one = answer
        elif choice == 'n':
            should_accumulate = False
            print("\n" * 20)
            calculator()



calculator()