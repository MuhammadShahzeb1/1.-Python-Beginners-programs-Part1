# now we will discuss continue statement the purpose of continue statement is that it can ignore the rest of loop after its execution

# like in this program i want to print only first 6 numbers so i apply continue statemnt when it reaches 6 it will give us our result and that jumps out of the loop
#Continue Statement
i=0
while i<45:
    if i>6:
        i=i+1
        continue     #it will print out only 6 numbers than terminate the jumps out of the loop
    print(i)
    if i==44:
        break
    i=i+1
