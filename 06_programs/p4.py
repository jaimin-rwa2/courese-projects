user = {
    "name": "jaimin",
    "age": 99,
    "email": "jbpatel1411@gmail.com"
}

# print(user["age"])

# key = "email"
# print(user[key])

if ("@" in user["email"]) and (".com" in user["email"]):
    print("user email is valid")
else:
    print("user email is in-valid")


if user["age"] > 0:
    if  user["age"] <= 10:
        print("child")
    elif user["age"] <= 19:
        print("teenager")
    elif user["age"] <= 35:
        print("younge")
    elif user["age"] <= 55:
        print("adult")
    else:
        print("old")
else:
    print("please enter valid age")