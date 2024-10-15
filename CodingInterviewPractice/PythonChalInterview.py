'''

Write a function that accepts a number as an input and returns
a list of integers that stretch from 0 up to the given number
(including the number!) in the increments of 5. But your list must EXCLUDE
any numbers that can be divided by 7 without a remainder.

1. We only pass one integer to the function that is int > 0

- convert input to int
- make a list of ints up to len(value)?
- for i in list -- if i % 5 == 0 and if i % 7 =! 0 add to new empty list?

'''

#premise says that we can only pass one int > 0 so I won't check that user int is a number -- maybe do this anyways
#practice try/expect?? later tho
user_input = input("Please enter an integer larger than zero: ")
int_user = int(user_input)

#my lists -- actually only need one list
#initial_list = []
new_list = []

#adding numbers to list
def five_not_seven(input:int):
    for i in range(int_user): #have to use range for int, not len()! len is for strings
        if i % 5 == 0 and i % 7 != 0:
            new_list.append(i)
    return new_list

print(five_not_seven(user_input))


