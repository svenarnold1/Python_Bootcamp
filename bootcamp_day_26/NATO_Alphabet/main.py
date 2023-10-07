import pandas

with open("nato_phonetic_alphabet.csv") as file:
    data = pandas.read_csv(file)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# helps me to understand the dict comprehension
# code_dict = {}
# for key, row in data.iterrows():
#     new_key = row.letter
#     new_code = row.code
#     code_dict[new_key] = new_code

# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
code_dict = {row.letter: row.code for index, row in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()
code_list = [code_dict[letter] for letter in user_word]
print(code_list)

