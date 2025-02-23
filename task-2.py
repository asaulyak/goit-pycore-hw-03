import random

def get_numbers_ticket(min, max, quantity):
    if min < 1:
        raise ValueError("min should be greater than 1")

    if max > 1000:
        raise ValueError("max should be less than 1000")

    if min > max:
        raise ValueError("min should be less than max")

    if quantity > max or quantity < min:
        raise ValueError("quantity should be between min and max")

    if quantity > max - min:
        raise ValueError("quantity should be less than or equal to a number of possible values")

    possible_numbers = list(range(min, max))

    return sorted(random.sample(possible_numbers, quantity))
