
#program for String Slicing

mystr= "I am Muhammad Shahzeb"
#to find the length of string
print(len(mystr))

#to find the specific index of a string
print(mystr[3])

#to find out the text between the range
print(mystr[0:5])

#if its exceeding the limit without providing range (range = 0:8 ,0:90 etc) it will show the error
# print(mystr[90])   commented bcz of error

#if its exceeding the limit by  providing range (range = 0:8 ,0:90 etc) it will not show the error
print(mystr[0:90])  #show upto max length limit

print(mystr[2:9]) #for print between this range
