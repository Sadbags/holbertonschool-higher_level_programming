#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end=" ")
            count += 1
    except IndexError:
        pass
    print()
    return count

my_list = [1, 2, 3, 4, 5]
num_printed = safe_print_list(my_list, 3)
print("Number of elements printed:", num_printed)
