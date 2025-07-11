#           0      1      2            3           4           5
user1 = ["dev", 22, 9876543210, "dev_207", "20-07-2003", "Dev@207"]
user2 = ["jaimin", "ASDF@1234", 25, 7041521968, "MrJemmy", "14-11-xxxx"]


user1 = { 
    "name" : "dev", 
    "age" : 22, 
    "phone_no": 9876543210, 
    "DOB": "20-7-2003", 
    "password": "Dev@207", 
    "username": "dev_207"
}

user2 = { 
    "name" : "jaimin", 
    "age" : 24, 
    "phone_no": 9876543210, 
    "DOB": "14-11-xxxx", 
    "password": "xyz", 
    "username": "mrjemmy"
}

empty_dict = {}
print(empty_dict)
print(type(empty_dict))

print(user1)
print(user1["name"])
print(user1["username"])
print(user2)
print(user2["name"])
print(user2["username"])