
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations ={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculation():
    num1 = int(input("what is your first number?: "))
    should_continue = True
    while should_continue:
        
        num2 = int(input("what is your next number?: "))
        for symbol in operations:
            print(symbol)
        operation_symbol = input("pick an operation from the list: ")
        calculate_function = operations[operation_symbol]
        answer = calculate_function(num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {answer}')
        if input(f'if you have other calculation with {answer} type "y" and if you want to calculate again type "n": ') == "y":
            num1 = answer
        else:
            should_continue = False
            calculation()

calculation()        