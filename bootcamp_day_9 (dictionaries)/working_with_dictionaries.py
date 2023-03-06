student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# set dictionary student_grades as given in excercise
student_grades = {}
for key in student_scores:
    score = student_scores[key]
    if score >= 91 and score <= 100:
        student_grades[key] = "Outstanding"
    elif score >= 81 and score <= 90:
        student_grades[key] = "Exceed Expectation"
    elif score >= 71 and score <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)

# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a dictionary

travel_log0 = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a dictionary in a dictionary
travel_log1 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 3},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 4},
}

# print(travel_log["France"]["total_visits"])

# Nesting a dictionary in a list

travel_log2 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 3
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 4
    },
]

# interactive coding challenge


# write a function called add_new_country that allows us to add new countries inside of travel_log2
def add_new_country(country, number, cities):
    add_dict = {"country": country, "cities_visited": cities, "total_visits": number}
    travel_log2.append(add_dict)
    return travel_log2


# Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log2)

