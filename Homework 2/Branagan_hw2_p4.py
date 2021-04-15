#Ryan Branagan
#Collaborators: N/A
#Branagan_hw2_p4.py
#1/15/19

N = 25 #This is the input integer

a = [] #This is an empty list

for i in range(N):
    if i % 3 == 0 or i % 5 == 0:
        a.append(i) #Instead of using a list full of zeroes, I wanted to just append the list

print(a)