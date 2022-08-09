'''
Abstraction - 

User is familiar with 
What function does  (Yes)
But not with 
how it does  (No)

Abstraction is used to hide the internal functionality of the function from the users.
eg: TV Remote, Smartphone

Why Abstraction is Important?

An abstraction is used to hide the irrelevant data/class in order to reduce the 
complexity.

How to achive abstraction inside python?
A class that consists of one or more abstract method is called abstract class.
'''
from abc import ABC, abstractmethod

class Car(ABC):
    def mileage(self):
        pass

class Tesla(Car):
    def mileage(self):
        print('The mileage is 30')

class Nexon(Car):
    def mileage(self):
        print('The mileage is 20')

class Baleno(Car):
    def mileage(self):
        print('The mileage is 25')

class Eon(Car):
    def mileage(self):
        print("The mileage is 25")


t = Tesla()
t.mileage()

r = Nexon()
r.mileage()

b = Baleno()
b.mileage()

e = Eon()
e.mileage()

















