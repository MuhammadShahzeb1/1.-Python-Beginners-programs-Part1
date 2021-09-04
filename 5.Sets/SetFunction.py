#Some imp  set methods /functions

#some imp functions in sets


#pop function will delete last or 1st value
k=[1,2,3,9]
s4=set(k)

s4.pop()
print(s4)

#clear fnction
s4.clear()   #will wipe out all data from set
print(s4)

#Union Intersection function

list1=[1,2,3,4,6]
list2=[2,4,5]
s5=set(list1)
s6=set(list2)
print(s5.union(s6))               #will show union between set s5 and s6
print(s5.intersection(s6))        #will show intersection between set s5 and s6

#disjoint checking function
print(s5.isdisjoint(s6))


"""
To explore more functions in set visit
https://www.w3schools.com/python/python_ref_set.asp
"""
