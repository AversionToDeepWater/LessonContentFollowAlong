# Question 1

Here is the challenge given to a student:

```
Description:
Your goal in this is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]

If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
```

The solution they have provided is nearly working, but there are some problems with the code. 

Identify and describe the rectifications you have made to the non-working code to get it working. Explain these in a way the student is able to understand and learn from.

Also describe any general improvements that could be made to the code, if any.

Student's Code:
```
def array_diff(a, b):  
    my_list = []
    for y in a:
        if y not in b:
            new_list.insert(y)
    print(new_list)

print(array_diff([1,2,3],[1,2]))
```
