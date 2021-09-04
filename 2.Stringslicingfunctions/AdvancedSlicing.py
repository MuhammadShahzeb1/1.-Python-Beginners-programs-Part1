"""
Now we will start advanced slicing or extended slicing
in this type of slicing we learn how to skip the letters ,how to print by giving the gap etc.

[a:b:c] in this bracket the first will always considered 0 if value not provided
 2nd will be consider max len if value is not provided
 3rd will be considered 1 if value is not provided
 and can be written as (lets say max lenght is 8 so)[0:8:1]

"""
mystr= "I am Muhammad Shahzeb"
print(mystr[::])
print(mystr[::2])  # if 2 is provided than will skip every 2nd letter from index
print(mystr[::3])  # if 3 is provided than will skip every 3rd letter from index
print(mystr[::300])  # if provided value is more than max lentgh than will only give(print) 1st value.

print(mystr[3:9:3])  # we cover between range and skipping at te same time

# Now we will deal with the -ve index
print(mystr[::-1])  # it will be printed in reverse form like shah  into hahs

print(mystr[::-2]) # it will be [rinted with two letter skipping

# now we are going to understand how these negative indexes works
"""
like in a str = shahzeb  max lenght is  so it starts from to 6 in asscending order 0=s,1=h,2=a, and onwards
now in negative it starts reverse counting like 0=s so now -1=b -2=e and onwards at the same time max length = -1
like in shahzeb  -1=6=b 
"""

print(len(mystr))
print(mystr[-1])   #will last letter
print(mystr[20])   #max length last letter =-1

