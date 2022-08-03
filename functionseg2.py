'''
OOPs -----    Object Oriented Programming 
Function - Class dono ko agar call - Objects

1. Inheritance
2. Encapsulation
3. Abstraction
4. Polymorphism
'''

def evenodd(num):         #Function 
    if num%2 == 0:
        return "Even"       
    else:
        return "Odd"

a = int(input())          #Input
out = evenodd(a)          #Object
print(out)                #Output of Function
