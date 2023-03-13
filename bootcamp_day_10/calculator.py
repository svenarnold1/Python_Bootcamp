import calculator_functions


# operators available in calculator
operations = {
    '+': calculator_functions.add,
    '-': calculator_functions.subtract,
    '*': calculator_functions.multiply,
    '/': calculator_functions.divide
}


# first input for the program
def calculator():
    print(calculator_functions.logo)
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
    keep_going = True
    while keep_going:
        move_on = input(f"Type 'y' if you want to continue calculation with {result}, otherwise type 'n'!\n").lower()
        if move_on == 'y':
            # why return in function instead of print? - so we can set function as argument for other function!
            for key in operations:
                print(key)
            operation_symbol = input('Pick an operator from the line above? ')
            num_3 = float(input('Input your next number: '))
            calculation_function = operations[operation_symbol]
            result_2 = calculation_function(result, num_3)
            # print the result
            print(f"{result} {operation_symbol} {num_3} = {result_2}")
            result = result_2
        else:
            keep_going = False
            calculator()


# call the calcutator function above
calculator()
