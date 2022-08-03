from audioop import reverse
from unicodedata import name


dict1={"name": "mradul","age": 23,"city": "indore"}
print(dict1)

dict1 = {"name":"mradul","age":23,"city":"indore"}
print(dict1.keys())

dict1 = {"name":["Mradul", "Surbhi", "Kumud", "Vaibhav"],"jeescore":[23, 24, 25, 26],"city":["Indore", "Dewas", "Ujjain", "Dewas"]}
print(dict1)
print(dict1["name"][0])


#Problem - Find out the jee score of candidate with name Mradul
name_index = (dict1["name"].index("Mradul"))
print(name_index)
print(dict1['jeescore'][name_index])

dict1['jeescore'].sort(reverse=True)
print(max(dict1['jeescore']))


