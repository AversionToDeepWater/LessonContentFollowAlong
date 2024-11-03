class Pet: #General class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I do not know what to say")


class Cat(Pet): #specific class inheriting from general pet class
    def __init__(self, name, age, colour):
        #still want to call parameters from parent initialisation as it may be important (e.g., may call another method)
        #super() means we reference the super class, i.e., the class we inherit from
        #__init__() defines the method we want to call
        # name and age are the arguments we want to pass to that method
        # NOTE we do not need to call self
        super().__init__(name, age)
        self.colour = colour
    def speak(self):
        print("Meow")
        # if there is a method that is defined in the parent class as well as the child class, the child class will
        # overwrite the method from the parent class

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old. I am a {self.colour} cat.")


class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Olive", 6)
p.show()
c = Cat("Fig", 3, "tuxedo")
#Though the cat class doesn't have an __init__ it has inherited that from the general Pet class
c.show()
c.speak() # specific to cat and dog

d = Dog("Pistachio", 2)
d.show()
d.speak()

f = Fish("Bubbles", 8)
f.speak()
