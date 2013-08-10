"""Totals numbers passed individually.
Takes a group of numbers passed as individual arguments and totals them
Args:
    *numbers    An indefinite number of integers
Returns:
    total       The total of the arguments as an integer 
"""
def total_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

"""Totals a list of numbers passed as an argument.
Takes a list of numbers and totals the entire list.
Args:
    numbers:    A single list of integers
Returns:
    total:      A single integer
"""
def total_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

"""Totals the values in a dictionary of integers.
Takes a dictionary of integers and returns the total of the values.
Args:
    numbers:    Dictionary of integer values
Returns:
    total:      The total as an integer
"""
def total_dict(numbers):
    total = 0
    for keys in numbers:
        total += numbers[keys]
    return total

"""Averages numbers passed individually.
Takes an indefinite number of integers as arguments and averages them.
Args:
    *numbers:   Indefinte number of integers
Returns:
    average:    The average as an integer
"""
def average_numbers(*numbers):
    """
    TODO: Figure out how to implement this using the total_numbers() 
    function as this is a temporary hack.
    """
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

"""Averages a list of integers.
Takes a list of integers and averages them.
Args:
    numbers:    List of integers
Returns:
    average:    The average as an integer
"""
def average_list(numbers):
    return total_list(numbers) / len(numbers)

"""Averages a dictionary of integers.
Takes a dictionary of integer values and averages them.
Args:
    numbers:    Dicitionary of integer values
Returns:
    average:    The average as an integer.
"""
def average_dict(numbers):
    return total_dict(numbers) / len(numbers)
