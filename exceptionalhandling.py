from typing import final


def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Division by zero error"
    finally:
        return "Something else happend"
   

a = int(input())
b = int(input())
out = div(a,b)
print(out)
