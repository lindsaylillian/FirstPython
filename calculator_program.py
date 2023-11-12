


def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply (n1,n2):
    return n1 * n2

def divide (n1,n2):
    return n1 / n2

operation={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }
#from this step you place in the numbers you would like to calculate

num1=int(input("what is the first number"))
num2=int(input("what is the second number"))

for operand in operation:
    print(operand)

operation_symbol=input("what operand would you like to pick\n?")

calculation_function=operation[operation_symbol]
answer=calculation_function(num1,num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
