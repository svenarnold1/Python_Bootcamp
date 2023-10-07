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

# looping through dataframes
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

stundet_df = pandas.DataFrame(student_dict)

# for key, value in stundet_df.items():
   #  print(f" key: {key}, value: {value}")

# Loop through ros of DF

for (index, row) in stundet_df.iterrows():
    # print(f" index: {index}, row: {row}")
    print(row.student)
