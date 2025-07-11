# +	    Addition	    a + b = 30
# -	    Subtraction	    a b = -10
# *	    Multiplication	a * b = 200
# /	    Division	    b / a = 2
# %	    Modulus	        b % a = 0
# **	Exponent	    a**b =10**20
# //	Floor Division	9//2 = 4


a = 20
b = 10
result = None

# +
result = a + b
print("a + b : ", result)


# -
result = a - b
print("a - b : ", result)

result = b - a
print("b - a : ", result)


# *
result = a * b
print("a * b : ", result)


# /  output in always Float value
result = a / b
print("a / b : ", result)  

result = b / a
print("b / a : ", result) 


# **
result = b ** a
print("b ** a : ", result)

result = a ** b
print("a ** b : ", result)


# //  output in always int value
result = a // b
print("a // b : ", result)  

result = b // a
print("b // a : ", result) 


# % modulus
a = 1545641561
b = 2
print("a % b : ",a % b)