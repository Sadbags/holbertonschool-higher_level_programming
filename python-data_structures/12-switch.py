#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # If tuple_a or tuple_b is smaller than 2, add zeros for missing integers
    if len(tuple_a) < 2:
        tuple_a += (0, ) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0, ) * (2 - len(tuple_b))

    # Add the first elements of the tuples and the second elements of the tuples
    sum_first = tuple_a[0] + tuple_b[0]
    sum_second = tuple_a[1] + tuple_b[1]

    # Return the tuple containing the sums
    return (sum_first, sum_second)
