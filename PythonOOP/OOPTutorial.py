'''
OBJECT ORIENTED PROGRAMMING IN PYTHON

x = 1
Consider the type() function, which returns what data type you have

print(type(x)) returns <class 'int'> to the console
Our data type 'int' is part of a class

Therefore, when we write x = 1, we set x equal to the object which is a type integer, with the value '1'

Everything we work with in python is an object of some type of class
- There are many in-build types (i.e., built into the python language)
- When you create something in Python, you are creating an object which is an instance of a specific class
- That class defines the way the object can interact with other things in our programme
    - For example, will return TypeError when you try to add str with int

METHODS
.xyz(arg) is a method that is acting on our object

string = "hello"
print(string.upper()) where .upper() is a method acting on an object type str

methods we can use are dependent on what class our object belongs to
'''

#Making our own class :D

#When naming our class we use camel case
class Dog: #blueprint for any object that is of type dog, and defining what operations it can perform

#self argument is always needed, so we can pass the object itself so we know what data to access

    def __init__(self, name, age): #instantiate object right when it is created, and assign attribute(s)
        #attributes can be referenced later on or within the class
        self.name = name #created an attribute of the class dog which is name.
        self.age = age

        #self is there to denote the object itself
        #whenever we create a new dog object, we will pass a name through this parameter

    #therefore whenever we create a new dog instance using Dog(), it will pass any arguments to this method
    #e.g. whenever a Dog() object is made, we say that the dog needs to have a name

    def bark(self): #this is a method, it is a function that goes into a class
        print("bark")

    def add_one(self, x):
        return x+1

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age



#creating an object of the class dog, with a different name, so we can access attributes specific to each dog
#this is stored permanently for each specific object
d = Dog("Bagel", 5)
#d2 = Dog("Baguette")

print(d.get_age())

# print(d.name) # not needed with get_name method
# print(d2.name)

# d = Dog() #our variable d is assigned to an instance of the class Dog
# # therefore d is an object of type dog
#
# print(type(d))
# # returns <class '__main__.Dog'>
#
# # Using method on instance of type dog
# d.bark()
#
# # Using another method from out dog class, which has different arguments and parameters
# print(d.add_one(5))
#
# # Using