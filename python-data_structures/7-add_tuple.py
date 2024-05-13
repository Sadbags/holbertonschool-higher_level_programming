#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure tuples have at least two elements
    # by padding with zeros if necessary
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    # Return a new tuple that sums the first two elements of each tuple
    return (a[0] + b[0], a[1] + b[1])


if __name__ == "__main__":
    # Test code
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1,)))
    print(add_tuple(tuple_a, ()))
