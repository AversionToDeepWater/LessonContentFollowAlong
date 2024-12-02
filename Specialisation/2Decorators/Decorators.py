def outer_wrapper(func): #simple_funct will be taken as an argument
    def inner_wrapper():
        print("This is the first line")
        func()
        print("This is the last line")
    return inner_wrapper

@outer_wrapper
def simple_funct():
    print("This is the middle line")

simple_funct()
