my_dict = {
    "username": "MrJemmy",
    "email": "jbpatel1411@gmail.com",
    "phone_no": 7041521968,
    "DOB": "14-11-1999"
}

username1 = my_dict["username"]
print(username1)
username2 = my_dict.get("usernames", False)
print(username2)

my_dict_keys = my_dict.keys()
print(my_dict_keys)

my_dict_values = my_dict.values()
print(my_dict_values)

my_dict_items = my_dict.items()
print(my_dict_items)

print("========= 1 ===========")
print(dir(my_dict))

print("========= 2 ===========")
# print(my_dict)
# my_dict.clear()
# print(my_dict)

print("========= 3 ===========")
key_sque = ("username", "password")
my_dict_fromkeys = my_dict.fromkeys(key_sque, "default")
print(my_dict)
print(my_dict_fromkeys)
print(my_dict)

print("========= 4 ===========")

is_has = "username" in my_dict.keys()
print(is_has)


print("========= 5 ===========")
pop_value = my_dict.pop("DOB")
print(pop_value)
print(my_dict)


print("========= 6 ===========")
popitem_value = my_dict.popitem()
print(popitem_value)
print(my_dict)


print("========= 7 ===========")
username3 = my_dict.setdefault("usernames", False)
print(username3)
print(my_dict)


print("========= 8 ===========")
print(my_dict)
user_other_data = {
    "DOB": "14-11-1999",
    "location": "Ahmedabad",
    "gender": "male"
}

new_dict = my_dict.update(user_other_data)
print(my_dict)  # inplace (memory ma new dic nathi bani, exicting maj change thaya 6e)
print(new_dict) # not inplace (memory ma new dic bani)

