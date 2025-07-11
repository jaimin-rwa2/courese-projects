# unpacking : distructuring 
my_tuple = (11, 12)
my_list = ["v1", "v2", "v3", "v4", "v5", "v6", "v7"]
my_dict = {
    "username": "MrJemmy",
    "email": "jbpatel1411@gmail.com",
    "phone_no": 7041521968,
    "DOB": "14-11-1999"
}

#  noraml
v1 = my_tuple[0]
v2 = my_tuple[1]

print(v1, v2)

v11, v12 = my_tuple
print(v11, v12)

# mentos 
my_tuple_2 = v11, v12
print(my_tuple_2)

lv1, lv2, lv3, *extra = my_list
print(lv1, lv2, lv3, extra )

# by default key unpack


email, username, dateofbirth, phone_ka_no = my_dict.values()
print(username, email, phone_ka_no, dateofbirth)


