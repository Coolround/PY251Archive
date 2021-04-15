#Ryan Branagan
#Collaborators: N/A
#Branagan_hw2_p5.py
#1/16/19

N = 5 #This is the input integer

a = [] #This is an empty list
y = 0 #Just like in previous routines this is needed to start our adding at first to start form one

for i in range(1,N+1):
    for x in range(1,i+1): #Nested for loop that takes input from the first for loop to find the sum of integers from 1 to N_i
       y = y + x
    a.append(y) #Once the nested for loop has added the first N_i integers together we add it to the list
    y=0 #We need to clear y in each step so we can start over from 1 instead of the result from the previous step

print(a)