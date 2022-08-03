# li1 = (21, 33, 40, 65)

# for i in li1:           
#     if i%2 == 0:
#         print(i, " is an even number")
#     else:
#         print(i, " is an odd number")

# name = "Codersdaily"

# for i in name:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#         print(i, " is a vowel")
#     else:
#         print(i, " is a consonant")
'''for i in range(4):
    print(li1[i])                   print(li1[0])
                                    print(li1[1])
                                    print(li1[2])
                                    print(li1[3])'''

# li1 = [21, 33, 40, 65]
# for i in range(len(li1)):  
#     print(li1[i])    

#Created a dictionary 
users = {'Mradul': 'active', 'Manal': 'inactive', 'Hardik': 'active'}

#Added for loop statement
for user, status in users.items(): #Here user is key and status is value
    print(user, status)
    # if status == 'inactive':
    #     del users[user]