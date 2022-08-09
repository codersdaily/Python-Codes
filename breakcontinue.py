'''
continue statement in Python
The continue statement is used to skip the remaining code inside a loop for the current iteration only.

As its name suggests, pass statement does nothing.
It is used when a statement or a condition is required to be present in the program but we do not want any command or code to execute.

pass statement is usually used while creating a method, which we do not want to use right now.

'''


a = 13
status = 0 #I am considering that by default the number is prime and if the number is prime the status would be 0
for i in range(2,a):
    if a%i == 0:   #this condition is true when the number is not prime
        status = 1
        break
    else:
        pass
    

if status == 1:
    print("The number is not prime number")
else:
    print("The number is prime number")