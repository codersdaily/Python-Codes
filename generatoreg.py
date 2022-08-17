def my_gen():    #this is the function
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n = n +  1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

a = my_gen()    #this is the object
for i in a:
    print(i)