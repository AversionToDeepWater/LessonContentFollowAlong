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

    def bark(self): #this is a method, it is a function that goes into a class
        print("bark")

d = Dog() #our variable d is assigned to an instance of the class Dog
# therefore d is an object of type dog

print(type(d))
# returns <class '__main__.Dog'>

# Using method on instance of type dog
d.bark()

