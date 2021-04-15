#Ryan Branagan
#Collaborators: N/A
#Branagan_hw2_p1.py
#1/10/19

a=0 #This is needed to start with 1 and be able to even run the code with "a" unassigned
for i in range(1,100):
    if i % 3 == 0 or i % 5 == 0:
        a = a + i
print('The sum of the numbers less than 100 divisible by 3 or 5 is',a)