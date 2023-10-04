# list comprehension

# exercise 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squares = [num * num for num in numbers]
print(squares)

# exercise 2
str_list = [str(num) for num in numbers]
int_list = [int(num) for num in str_list]
even_nums = [num for num in int_list if num % 2 == 0]

print(even_nums)
