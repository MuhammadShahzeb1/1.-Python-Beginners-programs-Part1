rollno=[12,13,15,11,5,8,9]
print(rollno)


"""
Now will go through  some more important functions  
"""
# Append Function: in append function we add values to the existing list or null list

rollno.append(117)  #add 117 in the existing list
print(rollno)

#testing with new list
myrollno=[]        # null list
myrollno.append(1) # this will  add 1 in null list
myrollno.append(1)
myrollno.append(7)
print("your roll no is")
print(myrollno)
myrollno.insert(3,8)
myrollno.remove(8)
print(myrollno)

#This Pop function will delete last item from the list
rollno.pop()
print(rollno)

#This insert function will insert value to list
rollno.insert(8,118)  # (index,value) first parametre is no of index in which we want to enter value and 2nd one is the value
print(rollno)

#This remove function will remove from list
rollno.remove(118)   #(value) we just put the value we want to remove from list we dont need to put index number
print(rollno)




"""
To explore more list functions visit
https://www.w3schools.com/python/python_ref_list.asp          and
https://www.programiz.com/python-programming/methods/list
"""