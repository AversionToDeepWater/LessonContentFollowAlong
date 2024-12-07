"""
Using the previous Generator as an example,
write a Generator called "My_Fridge".
Each time the generator is called, it should read
out items you would find on that shelf of a fridge.

Return an object where the Key is the name of the
shelf, and the value is the list contents of that
shelf.
"""

fridge = {'shelf 1': ['brie', 'mushrooms'],
          'shelf 2': ['spring onions', 'tofu'],
          'shelf 3': ['Gu pot', 'pizza']}

def My_Fridge(fridge):
    for key, item in fridge.items():
        yield f"On {key} there is {item}"


my_fridge = My_Fridge(fridge)
print(next(my_fridge))
print(next(my_fridge))