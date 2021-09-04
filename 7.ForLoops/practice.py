# we will find a larget number in list

l=-1                                 #initialize a variable so that we can compare the numbers
list4=[1,2,3,4,5,8,9,23,34,678]
for item in list4:
    if item>l:                       #comparison with the variable
        l=item                       #new value of l
        #print(l)
print(l)                              #for printing the latet value at the end of loop

"""
for more information about loops  plz visit  
https://www.programiz.com/python-programming/for-loop 
"""