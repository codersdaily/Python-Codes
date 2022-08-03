list1 = [52, 52, 52, 35, 44, 67, 78.0, "CD"]
#indexV  0   1   2   3   4      5

#indexing of list 
# print(list1[0])
# print(list1[4])
# print(list1[-1])
# print(list1[-3])  

#Slicing
#a = list1[startpoint: endpoint-1 : difference]
# a = list1[0: 4: 1]
# print(a)

#b = list1[::1]
# if we are using :: then we consider two arguments inside the bracket. 1. is the start point. 2. Is the difference value. 3. If the value is in negative the list will start printing its value backwards and if the value is positive it will print values forward.
# print(b)
# print(len(list1))

# list1.append("920")
# print(list1)

# x = list1.copy()
# print(x)

# x = list1
# print(x)

list1.remove(52)
print("Remove Output: ",list1)

a = list1.count(52)
print(a)

a = list1.index(52)
print(a)

# list1.insert(2, 44)
# print(list1)

list1[2] = 44
print(list1)

list1.pop()
print(list1)

list1.reverse()
print(list1)

list1.sort()
print