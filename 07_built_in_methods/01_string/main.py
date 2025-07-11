# lower(), upper(), strip() = rstrip() + lstrip() , split(), join(), find(), replace(), startswith(), endswith(), count(), index(sub, beg, end)

first_name = "Jemmy"
last_name = "Aakhja"

print(first_name + " " + last_name)
print(f"{first_name} {last_name}")


my_string = "Hello Jaimin, How are you?"

print(my_string, type(my_string))
print(my_string.lower())
print(my_string.upper())

username = "  jaimin   "
print(username, "end")
print(username.strip(), "end")
print(username.lstrip(), "end")
print(username.rstrip(), "end")


print("======================================")
print(my_string.split())
print(my_string.lower().split("j"))   # method chaing


my_string_list = ['Hello', 'Jaimin,', 'How', 'are', 'you?']
print("-".join(my_string_list))

print(my_string.find("j")) # -1: not fount
print(my_string.lower().find("j")) # Number: index of value
print(my_string[my_string.lower().find("j")])

print(my_string.replace("Jaimin", "Diya"))
print(my_string.startswith("Hello"))
print(my_string.endswith("/"))

print(username.count(" "))
print(len(username))
print(username.index("j"))