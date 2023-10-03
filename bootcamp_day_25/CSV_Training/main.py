
# reading weather data as I knew before.
with open("weather_data.csv") as file:
    data = file.readlines()

import csv
# csv.reader creates an object I can loop through
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for temp in data:
        if temp[1] == 'temp':
            continue
        else:
            temperatures.append(int(temp[1]))

# introducing powerful libary called panda.
import pandas
data = pandas.read_csv("weather_data.csv")
print(data["temp"])

# convert dataframe to dictionary
# data_dict = data.to_dict()
# print(data_dict)


def avg_val(my_list):
    """return the average value of a list"""
    return sum(my_list) / len(my_list)


# converting to list.
temp_list = data["temp"].to_list()
# print(temp_list)

# average value of list without using panda
print(avg_val(data["temp"]))
# average() value of list using panda
print(data["temp"].mean())
# max value of data using panda and data.temp instead of data["temp"]
print(data.temp.max())

# Get data in row
print(data[data.day == "Monday"])
# Get row that includes highest value of temperature.
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
# temp in Fahrenheit
print(monday.temp[0] * (9/5) + 32)

# Create dataframe from scratch.
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

my_table = pandas.DataFrame(data_dict)

print(my_table)
my_table.to_csv("new_data.csv")


def count_furcolor(data):
    """counts color of data file."""
    gray = 0
    red = 0
    black = 0
    for color in data:
        if color == "Gray":
            gray += 1
        elif color == "Cinnamon":
            red += 1
        elif color == "Black":
            black += 1
    return gray, red, black


# open the file of data
with open("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") as data:
    data_file = pandas.read_csv(data)

# calling the count function and pass in only the color data
color_count = count_furcolor(data_file["Primary Fur Color"])

# dict that contains colors as well as counts
data_dict = {"Fur Color": ["Gray", "Red", "Black"],
             "Count": [color_count[0], color_count[1], color_count[2]]
             }
# converting dict to dataframe
count_table = pandas.DataFrame(data_dict)

# create csv
count_table.to_csv("squirrel_count.csv")



