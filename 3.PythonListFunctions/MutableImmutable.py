
rollno=[12,13,15,11,5,8,9]
print(rollno)

myrollno=[]        # null list
myrollno.append(1) # this will  add 1 in null list
myrollno.append(1)
myrollno.append(7)
print("your roll no is")
print(myrollno)


#now we will discuss how can we change the item from list
#Mutable  can change
#Immutable  can not change

"""
Tuples values can not be changed  
tuples are represented in paranthesis instead of square brackets 
or in other words 
mutable are stored in square brackets 
immutable are stored in paranthesis

"""

#immutable
tp=(1,3,5)  #These type of values are called Tupples
#tp[2]=4   # will give error because value can not be changed in immutable
print(tp)

#tupple for storing 1 value we have to include comma after value
tp1=(1,)
print(tp1)


#Mutable
#chnaging the value from list
myrollno[2]=4
print(myrollno)      #changing value in list from 7 to 4

