cgpa = {"sem1": "2.4", "sem2": {"ISE": "2.4", "DSt": "2.9"}, "sem3": {"LA": "2.6", "NLA": "3.0"}, "sem4": "3.0", }
cgpa["sem5"] = "3.3"
cgpa["sem6"] = "3.2"
cgpa["summer"] = "3.5"
print(cgpa)


#Some important functions in Dictionary

# Deleting item from current dictionary


del cgpa["summer"]  # this is how item delelted from dictionary syntax del dictionaryname["key"]
print(cgpa)  # summer sem will be removed from current dictionary

# using Copy function
# why we use copy function
"""
basically when we write  gpa=cgpa it does not means that gpa get all value of cgpa
but it means that gpa is now assigned or refrenced to cgpa
If we delete something from gpa it will also be deleted from cgpa as well

that's why we create a copy function so that new assigned variable or dict get the copy of old
var dic and it saved old dictionary to be edited/alterd etc.

"""
# Without using copy function
gpa = cgpa  # gpa is assigned to cgpa   means both are same gpa will not create its own dict
del gpa["sem6"]  # it will deleted from both dictionary.
print(gpa)
print(cgpa)  # also deleted from old dictionary

# with using copy function
newgpa = cgpa.copy()  # now the copy of old dict is assigned
del newgpa["sem4"]  # delete from copy of cgpa
print(newgpa)  # Sem 4 info deleted
print(cgpa)  # No effect on original dictionary it shows semester 4 information as well

# get function
# in get function we simply fetch the value from dictionary

print(cgpa.get("sem1"))  # syntax dictionaryname.get("item or key ") it will show result of sem 1

# Update Function
# in update function it just simply update the value in dictionary

print(cgpa.update({"sem6": "3.2"}))  #if we print inside the function it will return None
print(cgpa)

cgpa.update({"sem6": "3.2"})   #update function must be applied outside the print function
print(cgpa)                    #will add gpa of 6th sem

#Keys function
#to find out the keys in a dictionary

print(cgpa.keys())     # will shows all keys of a dictionary

#items function
#to find out the items in a dictionary

print(cgpa.items())    #will shows all items of a dictionary
