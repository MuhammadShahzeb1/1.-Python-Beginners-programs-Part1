
# In this program we will learn about the Break Statement
# The main purpose of break statement is that we can stop the loop on our required value or we can stop the infinity loop that never stops
# for imolementing break statement  we usually use if statement


#break statement program that never stops or loop that keeps on running because we dant set the limit
"""i=0
while i<45:
    print(i)         Now this progrsm will keep on executing as limit is not defined so we have to put limit
    i=i+1 """

i=0
while i<45:
    print(i)
    if i==44:     # we use if statement and set the limit that when it reaches 44 perform following function
        break     #this will stop the program execution so after 44 program will be stoped
    i=i+1