class Evenit:                               #this is the class which will return all the even iterators

    def __init__(self, max=0):                     #This is the constructor which we created
        self.max = max
    
    def __iter__(self):                     #If there is an iterable so __iter__ will convert that into iterator
        self.n = 0
        return self
    
    def __next__(self):                     #This method is used to iterate the iterable one by one.
        if self.n <= self.max:              #2 <= 10
            if self.n % 2 == 0:
                result = self.n             #0
                self.n = self.n + 1         #1
                return result
            else:
                self.n = self.n + 1
                return 1
        else:
            raise StopIteration

numbers = Evenit(10)
for i in numbers:
    print(i)