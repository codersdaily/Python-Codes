my_set = {1, 2, 3, 4, 5, 5}
my_set2 = {1, 2, 4, 5, 6, 7}

my_set.add(7)
print(len(my_set))
print(my_set2.difference(my_set))
print(my_set.intersection(my_set2))
print(my_set.union(my_set2))
print("Disjoint", my_set.isdisjoint(my_set2)) 

print("Subset", my_set2.issubset(my_set))

print("Symmetric Difference", my_set2.symmetric_difference(my_set))
print(my_set)

print(type(my_set)) 

class_list = ["aditya", "mradul", "surbhi", "kumud", "vaibhav", "vijay", "vijay"]
class_set = list(set(class_list))

print(class_set)