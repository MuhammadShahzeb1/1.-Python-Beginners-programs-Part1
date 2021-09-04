# now we discuss about the for loop
# Basically loops are used ofr iterations like if we want to do something repetative we dont have to write it many times we can simply ise loop
# for loop is a definite loop because we know the limitations in our loop that how many times we need repeptiotions

list1=["Muhammad Shahzeb","Hamid Zeeshan","Muhammad Aayyan","Ali Haider"]
print(list1[0],list1[1],list1[2],list1[3])  #This is how we generally print something if we want to print all

# #Now lets say i have a very big list and i want to print all items specifically that i have to write each one them
# #to solve this issue we use concept of loops

# #FOR LOOP
for item in list1:    #it will run for all the items present in the list
    print(item)       #print all the items in list1

# now we will perform for loop for the list inside a list

list2=[["Muhammad Shahzeb",21],["Hamid Zeeshan",13],["Muhammad Aayyan",1],["Ali Haider",25]]
# we assume that other element in item is age it can be autoinitialzed

for item ,age in list2:     #syntax item ,anyname  in list
    # print(item,age)         #now this loop will specifically work for the age inside the item    This will print item and age
    # print(age)              #we can specifically print out age as well
    print(item+" age is "+str(age))    #we can modify it according to our requirments  Imp thing is that dont forget to typecast int into str


# Applying conditon on for loop
# Now we will see that how can we take specifiacally values from list instead of taking all values or items
list3 =["ahmed" ,30 ,"abdullah" ,10 ,"yousaf"
         ,4]  # more names with age but in a single list or string and int in a same list
for item in list3:

    if str(item).isnumeric():  # as there are str and int a=in a same list and we want only numbers or int so for that we apply if condition
        if item >6:  # now more specifically in numbers we want only those numbers which are greater than 6
            print("the age above 6 is  " +str(item))  # after twice applying if condition we will get the numbers greater than 6 in a list
            # if str(item).isnumeric() and item>6:           #we can add two if statements in a single line as well






