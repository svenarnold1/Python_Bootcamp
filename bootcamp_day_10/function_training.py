# first steps of day 10

# function that returns name in title case
def format_name(f_name, l_name):
    """ return input in title case"""
    first = f_name.title()
    last = l_name.title()
    return first + ' ' + last


print(format_name(input('input your first name:\n'), input('input your last name:\n')))

