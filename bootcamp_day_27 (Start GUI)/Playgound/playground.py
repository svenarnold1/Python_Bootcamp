def add(*args):
    """Adds infinite amount of numbers."""
    # *args saves inputs as tuple.
    result = 0
    for n in args:
        result += n
    return result


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def calculate(start, **kwargs):
    """Unlimited keyword arguments can be inputed."""
    print(kwargs)
    result = start
    result += kwargs["add"]
    result *= kwargs["multiply"]
    return result


print(calculate(2, add=3, multiply=5))


class Car:

    def __init__(self, **kw):
        # get() allows to get item only if it exists.
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)



