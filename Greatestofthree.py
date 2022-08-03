a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# max_o = max(a,b,c)
# print("The Greatest number is: ", max_o)
if a>=b and a>=c:
    print("The Greatest number is: ", a)
elif b>=a and b>=c:
    print("The Greatest number is: ", b)
else:
    print("The Greatest number is: ", c)