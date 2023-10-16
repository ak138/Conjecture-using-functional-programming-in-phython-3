def myConjecture(x):
    seq = [x]                            #array to make the data esay to use
    if x < 1:                            #to make sure algo only works on numbers higher then 1
       return []
       
    while x > 1:
       if x % 2 == 0:                    #if number is even
         x = x / 2
         
       else:
         x =   1 + 3 * x                 #if odd
         
       seq.append(x)                     #adds new number to list   
    return seq                           #returns number to sequence

                                         #end of algorithm function


num = int(input("Enter an integer :"))   #ask for user input
print ("You have entered: ", num)        #prints user inputs

print(num)                               #prints number

print(myConjecture(num))                #prints result after sending nums to function


