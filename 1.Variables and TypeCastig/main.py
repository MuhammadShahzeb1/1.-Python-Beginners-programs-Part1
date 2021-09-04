"""
Variables ,Data Types,Concatenation,Type Casting
"""

var1 = "hello world"
var2 = "78"
var3=475
var4=21.6
#simply printing the line by storing string in variable
print(var1)

#Concatinating the same datatypes string
print(var1+var2)

# giving error because we can not concatenate different variables types
"""
this line of code is commented
print(var1+var2+var3+var4)

"""
#Type Casting
# we can contenate the two different variable by type casting

print(int(var2)+var3)
# in above line we concatenate two different types of variables.
print(var1+ str(var3+var4))

#Now we will learn how to print out multiple times without using loop
# this method is only applicable in STRING
print(5*var1)
# to shift on next line
print(5*"Bye World \n")

# now we will print int multiples time by typecasting
print(10*str(int(var3+var4)))

