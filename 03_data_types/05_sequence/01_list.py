#             0        1        2       3
students = ["dev", "prerita", "gopi", "diya"]

print(students) # ['dev', 'prerita', 'gopi', 'diya']
print(type(students)) # <class 'list'>

print(students[0], type(students[0]), students[0][1]) # dev <class 'str'> e
print(students[1])
print(students[2])
print(students[3])

""" we can have diff data type in single list """
#          0     1   2    3              4
value = ["dev", 22, True, 99.99, [11, 12, "13", 14, 13]]
print(value) # ['dev', 22, True, 99.99, [11, 12, '13', 14, 13]]
print(value[4]) # [11, 12, '13', 14, 13]

""" this is call muti dymention indexing"""
print(value[4][2]) # 13
print(value[4][2][0]) # 1  

marks1 = [11, 12, 13, 14, 15]
marks2 = [21, 22, 23, 24, 25]

"""  it duplicates list by 3  """ 
print(marks1*3) # [11, 12, 13, 14, 15, 11, 12, 13, 14, 15, 11, 12, 13, 14, 15]
"""  + perform concept for list and string and for int it perform multi """
print(marks1 + marks2) # [11, 12, 13, 14, 15, 21, 22, 23, 24, 25]


print("hello"*3 + "dev")  # hellohellohellodev

# empty list
new_list = []
