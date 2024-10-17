#
# a = [1,2,3]
# b = [2]

#Students code
def array_diff(a:list, b:list) -> list:
    my_list = []
    for y in a:
        if y not in b:
            my_list.append(y)
    return my_list

print(array_diff([1,2,3],[1,2]))

'''
1. The variable 'my_list' was not called again in your function. Instead, a new variable 'new_list' was called
Solution: make sure you are using the right variable names across your function

2. You did not return your variable in your function 

Printing is not the same as a return in a function. Print will just display the answer on the Python console,
however, return will signal to Python it needs to store the value for later use.
Solution: You should return your variable at the end of the function

3. Insert was used instead of .append()
You want to add the unique value to a your new list. Therefore, you will want to use .append() as .insert() is not
compatible 


'''