
#we will discuss the use of operators in python programming language
#mostly comments are single line in this program

#There are 8  majors operators used in pyhton
# Operators In Pythons
# Arithmetic Operators
# Assignment Operators
# Comparison Operators
# Logical Operators
# Identity Operators
# Membership Operators
# Bitwise Operators

# Arithmetic Operators              This operator will perform arithmatic operations like..
print("5 + 6 is ", 5+6)                #addition
print("5 - 6 is ", 5-6)                #substraction
print("5 * 6 is ", 5*6)                #multiplication
print("5 / 6 is ", 5/6)                #division
print("5 ** 3 is ", 5**3)              #Power   * one star only multiplies while ** for square or it raise the power and keeps on going *** for cube.
print("5 % 5 is ", 5%5)                #modules operator this will devide the numbers and gives the leftover substracted value (application: use to find odd even numbrs)
print("15 // 6 is ", 15//6)            # double division

# Assignment Operators
print("Assignment Operators")
x = 5                                     #this operators does not mean equals to or also doenst store value in x its basiccaly refer or assign 5 to x
print(x)
x %=7
#x = x%7
print(x)

# Comparison Operators
i = 5
print(i==4)    #will compare as i is not equal to 4 so will return False and vice versa

# Logical Operators
a = True                   # In logical Operators we work on boolean algebra as a and a is true while a and b is false etc.
b = False
# print(a and a)
# print(a and b)

# Identity Operators         #is or is not
# print(a is not a)          #will return false
# print(a is a)              #will return True
# print(a is b)              #False
# print(a is not b)          #True applying boolean algebra

# Membership Operators        #in or in not
list = [3, 3,2, 2,39, 33, 35,32]
# print(3 in list)               #true
# print(324  in list)             #false
# print(324 not in list)          #true  applying not with false return true



# Bitwise Operators         #Binary values of digits
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11

print(0 & 2)    #will perform and operation on 00 and 10
print(0 | 3)    #will perform Or operation between 00 and 11