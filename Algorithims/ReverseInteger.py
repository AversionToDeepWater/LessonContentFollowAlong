####################################################################
# 1. Reverse Integer

# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

x = 57

def reverse_int(integer:int) -> int:
    i = abs(integer)
    list_i = list(str(i))
    reverse_list = []
    for x in list_i[::-1]:
        reverse_list.append(x)
    reverse_int_list = ''.join(reverse_list)
    r_int = int(reverse_int_list)
    return r_int

print(reverse_int(x))



