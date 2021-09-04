"""
we are going to make a small program as a quiz and also as a exercise as well
"""
name=input("enter your name")
print("your name is "+name)

# This will also give an error because of concatenating two different types of datatypes
"""
semester=input(enter your semester)
print(name+semester)
"""
semester=input("enter your semester") # as strng
print(name + semester)

sem1= input("enter value you want to add to semester")
print(semester+sem1)
# above line gives logical error 2+4 is 6 not 24
print(int(semester)+int(sem1))


"""
now about the playlist quiz
"""

# without typecasting
num1=input("enter 1st num")
num2=input("enter 2nd num")
print(num1+num2)

# with typecasting
num3=input("enter 1st num")
num4=input("enter 2nd num")
print(int(num3)+int(num4))

