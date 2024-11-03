# Class attributes are specific to the class, not to an instance or an object of that class

''' EXAMPLE
#want to make your classes as robust as possible so you can export them as needed
class Person():
    number_of_people = 0
    # number of people is a class attribute we say this bc it does not use self, so is not defined in any method
    # and does not have access to an instance of the class
    # Therefore, it does not change from person to person, such as another attribute like name

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1 #autoincrements as you add more people


p1 = Person("Socks")
print(p1.number_of_people)
p2 = Person("Hat")
print(p2.number_of_people)
'''

class Person:
    number_of_people = 0
    GRAVITY = -9.81

    def __init__(self,name):
        self.name = name
        Person.add_person() #calls our class method we made

    @classmethod #this is a decorator, denotes that this specific method is a class method
    #this means it is not specific to an instance, but it acts on the class itself
    def number_of_people_(cls): #cls instead of self as this is a class method
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Socks")
p2 = Person("Hat")
print(Person.number_of_people_())