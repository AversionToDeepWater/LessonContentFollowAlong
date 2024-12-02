def my_fave_animal(func):
    def inner_wrapper():
        print("My favourite animal:")
        func()
    return inner_wrapper()

@my_fave_animal
def cat():
    print("Cat :D")

cat()