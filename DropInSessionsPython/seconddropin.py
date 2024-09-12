'''
__ Common Values __

Given two lists, example:
["Orange", 6, "Pizza", "Driver", 16, "Software Engineer"]
and
["Pluto", "Driver", 16, 6, "Hide",  "Reverse"]

Count the number of common values between.
- The values do not have to share the same index
- The values do have to be of the same type. For example, "15" (String) and 15 (Integer) are not the same.

'''

list_one = ["Orange", 6, "Pizza", "Driver", 16, "Software Engineer"]
list_two = ["Pluto", "Driver", 16, 6, "Hide",  "Reverse"]


def comparison(one,two):
    a = 0
    b = 0
    for item in one:
        if str(one) == True and str(two) == True:
            a = a+1
            return a
        elif int(one) == True and int(two) == True:
            b = b+1
            return b
    print(a)
    print(b)

comparison(list_one,list_two)

