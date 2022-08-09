'''Proporties of OOPs

1. Inheritance
2. Encapsulation
3. Abstraction
4. Polymorphism

Encapsulation basically desicribes to put restrictions on some methods or variable.
So that while executing them using inheritance they cant get updated accidentaly.

so the variable which cant get updated globally or there native value cant get updated
globally. Such variables are know as private variables.

we define private variables using an underscore before there name.

age = 25 # global variable
_age = 25 # private variable

Constructor - Constructors are self defined functions which executes themself.
              They are functions which are used to initialize private variables or just initialize values.

How to define constructors in python

def __init__(self):
    self._a = 2

Self - self represents the instance of the class. By using the "self" we can 
access the attributes and methods of the class in python.
'''
class Base:
    def __init__(self):
        self._a = 2

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class: ", self._a)

        self._a = 3
        print("Calling modified protected member outside class: ", self._a)

obj1 = Derived()
obj2 = Base()

print("Accessing protected memeber of obj1: ", obj1._a)
print("Accessing protected member of obj2: ", obj2._a)

