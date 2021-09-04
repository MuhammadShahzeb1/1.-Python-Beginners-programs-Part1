"""
Before starting the new project of Dictionary we have to understand some concepts
() these braces used for tuples  e.g   num=()  etc
{} these curly brackets are used for Dictionary Type Variable or functions etc  e.g  dict= {"a":"apple","b":"ball"} etc
[] these Square brackets are used for List to store multiple items in a single variable fruits=["apple","banana","orange"] etc

() = Tuple immutable
{} = Dictionary mutable     Dict = { (item= )"Key":"value"}
[] = List mutable
"""

# Now we will start learning about Dictionary

"""
Basically in dictionary  an ordered collection of data values, used to store data values like a map,
which, unlike other Data Types that hold only a single value as an element, 
Dictionary holds key:value pair. Key-value is provided in the dictionary to make it more optimized.

"""

# so now we are going to make dictionary for students university names  when we enter a name  it will show us their uni name

uni = {"Shahzeb": "FURC", "Shoaib": "AUI", "Yasin": "CIIT", "Hasnat": "UET"}  # simple dictionary
print(uni)  # will print complete dictionary list
print(uni["Shahzeb"])  # now it will print only Shahzeb uni name store in a dictionary

# Now we will discuss more specically about Dictionary Inside A Dictionary or Nested dictionary.

# we are going to store cgpa for semester and we will store some imp Subjects influence on gpa
cgpa = {"sem1": "2.4", "sem2": {"ISE": "2.4", "DSt": "2.9"}, "sem3": {"LA": "2.6", "NLA": "3.0"}, "sem4": "3.0", }
print(cgpa)  # it will show complete dictioary list
print(cgpa["sem3"])  # it will show complete a new dictionary only stored in sem3
print(cgpa["sem3"]["NLA"])  # now it will show the cgpa of sem 3 without Linear Algebra as LA means with LA and NLA means without LA.

# Adding new items to the existing dictionary
cgpa["sem5"] = "3.3"  # this is syntax if we want to enter new items to the dictionary var name["key "]="info"
cgpa["sem6"] = "3.2"
cgpa["summer"] = "3.5"
print(cgpa)  # as we added information of more 3 semester the dictionary list will be updated

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

"""
For learning about other Dictionary functions visit these site
https://www.w3schools.com/python/python_ref_dictionary.asp
https://www.programiz.com/python-programming/dictionary
"""


