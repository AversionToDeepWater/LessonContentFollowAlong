"""
Python program to find the sum of all items in a dictionary.

Input : {'a': 100, 'b':200, 'c':300}
Output : 600
"""

example =  {'a': 100, 'b':200, 'c':300}

def value_output (d:dict):
    total = 0
    for key in d: #iterates through dictionary
        total += d[key] #adds the value from each key value pair to starting value of zero
    return total
    #Another solution
    # for i in d.values():
    #     total += i
    # return total
print(value_output(example))
