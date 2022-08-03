class Calculator:
    def sum(a, b):      #Also known as methods
        return a+b
    
    def sub(a, b):
        return a-b

    def mult(a, b):
        return a * b
    
    def div(a, b):
        if b == 0:
            return "Cant operate"
        else:
            return a/b
    
    def lent(l1):
        count = 0
        for i in l1:
            count = count + 1
        return count


