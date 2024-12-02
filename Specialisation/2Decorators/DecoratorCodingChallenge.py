"""
Create a Decorator that tells you how long a function
has taken to run.

It should be called as @timer.

To do this, you'll need the `time` library imported.
the time library has many utilities within it,
consider using time.perf_counter(), but you may find another
alternative to this.

Maths hint:
To get the time between two moments,
subtract the start time away from the end time.

e.g:
I started timing at 16:36
I finished timing at 16:46

46 - 36 = 10
👆 a ten minute time difference.

However, your timer is going to be working with really
small time periods!
"""
#is it good practice to take *args for functions
#google says: no, as it can mask actual errors in your code
# you should also have good documentation for your code if you do use it
# one user said they use it if their function has a lot of optional fields
from time import perf_counter

# article that has a good explanation:
# https://builtin.com/articles/timing-functions-python#:~:text=To%20quickly%20time%20functions%20that,took%20to%20run%20that%20function.

#decorators should not rely on the function that it will decorate
def time_func(func):
    def inner_wrapper(*args, **kwargs): #*args and **kwargs so you can use this for any number of different functions
        start = perf_counter()
        func(*args, **kwargs) #this also needs to have *args and **kwargs so it can be used for any function
        end = perf_counter()
        time_taken = end - start
        #{func.__name__!r} meaning: func.__name__ returns the name of the function as a string
        #!r applies repr(), ensuring the string representation of an object is given
        #repr() helps give more detailed info than str(), and is useful for debugging
        #repr() returns an unambiguous string representation of the object
        print(f"Time to run {func.__name__!r} is: {time_taken} seconds")
    return inner_wrapper #need to return inner wrapper in the scope of the outer_wrapper

# Test your timer against this long running function:
# With an input reasonably large, around 1000.
# Don't go too high of a number! You might be waiting a while!

@time_func
def worker_function_numbers(num):
    total_sum = 0
    for n in range(num):
        total_sum = total_sum + sum([(i/2 + 5) for i in range(1000)])
    return total_sum


worker_function_numbers(1000)