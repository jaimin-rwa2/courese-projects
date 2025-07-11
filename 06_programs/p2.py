# + - / * %
# val1 symbol val2


val1 = float(input("Please enter value 1: "))
val2 = float(input("Please enter value 2: "))

oprator = input("Please select opration : +, /, -, *  :")


if oprator == "+":
    print(val1 + val2)
elif oprator == "-":
    print(val1 - val2)
elif oprator == "/":
    print(val1 / val2)
elif oprator == "*":
    print(val1 * val2)
else:
    print("please enter correct oprator")