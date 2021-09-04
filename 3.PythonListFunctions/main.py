
# Now in this program we will explore List Data Structures

# Lists are  somehow equlanat to arrays
# in list we store multiple values in a single variable

#list
AhleBait=["Muhammad","Ali","Fatima","Hassan","Hussain",]
print(AhleBait)
print(AhleBait[4])    # now in above list we store five names and we can print any name by putting index number

# now we will see lists in case of numbers
rollno=[12,13,15,11,5,8,9]
print(rollno)

# now we will explore functions and methods in list
# These given below functions cange the original list
rollno.sort()
rollno.reverse()
print(rollno)

print(max(rollno))  # will print max/largest number from list
print(min(rollno))   #will print min/smallest number from list




# List Slicing
# List Slicing can not chnage the oroginal list
print(rollno[0:7])  # in this slicing it will show all numbers
print(rollno[:])    # it will show the same results as above bcz if we dont put vale first will consider least and 2nd max
print(rollno[2:5])  # it will show from index 2 to 5

# Extended Slicing
print(rollno[::2]) # will print with the skipping of every 2nd number in the list
print(rollno[::3]) # will print with the skipping of every 3rd number in the list

# Negative slicing is not recommended except -1
print(rollno[::-1]) # it will print reverse direction
print(rollno[1:7:-1])  #print null



#now we will discuss how can we change the item from list
#Mutable  can change
#Immutable  can not change

#immutable
tp=(1,3,5)
tp[2]=4
print(tp)


#Mutable
#chnaging the value from list
myrollno[2]=4
print(myrollno)      #changing value in list from 7 to 4
