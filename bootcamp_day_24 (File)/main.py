# read the starting letter with relative path.

def create_name_list(link):
    """returns list of all names in input file."""
    with open(link) as name_file:
        name_list = name_file.readlines()

    names = []
    for name in name_list:
        names.append(name.rstrip())
    return names


invited_names = create_name_list("Input/Names/invited_names.txt")

with open("Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

for name in invited_names:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as f:
        f.write(starting_letter.replace("[name]", name))

