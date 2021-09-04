#Need to be commented out
var1= 23

var2=int(input("enter number"))
if var2>var1:
    print("Greater")
else:
    print("smaller")

age=int(input("enter your age"))
if age>18:
    print("You can drive")
elif age==18:
    print("We can not decide you have to visit our office")
else:
    print("you cannot drive")


#In keyword

ls=[1,2,3,4,6]
if 5 in ls:
    print("present")
else:
    print("not present")

