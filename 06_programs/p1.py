# find a number is +ve or -ev



number = input("Please enter a Digit: ")
number = int(number)

if number > 0:
    print(f"Number {number} is +ve")
elif number < 0:
    print(f"Number {number} is -ve")
else:
    print("Number is zero")