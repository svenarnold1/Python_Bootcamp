# This is a calculator
# function to add two numbers
def add(n1, n2):
    return n1 + n2


# function to subtract two numbers
def subtract(n1,n2):
    return n1 - n2


# function to multiply two numbers
def multiply(n1,n2):
    return n1 * n2


# function to divide two numbers
def divide(n1, n2):
    return n1 / n2


# operators available in calculator
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# first input for the program
num_1 = float(input('Input your first number: '))
for key in operations:
    print(key)
operation_symbol = input('Pick an operator from the line above? ')
num_2 = float(input('Input your second number: '))

# choose the function we need and store result inside of variable
calculation_function = operations[operation_symbol]
result = calculation_function(num_1, num_2)

# print the result
print(f"{num_1} {operation_symbol} {num_2} = {result}")

# why return in function instead of print? - so we can set function as argument for other function!
num_3 = float(input('Input your next number: '))
for key in operations:
    print(key)
operation_symbol = input('Pick an operator from the line above? ')
calculation_function = operations[operation_symbol]
result_2 = calculation_function(result, num_3)

# print the result
print(f"{result} {operation_symbol} {num_3} = {result_2}")