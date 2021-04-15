#Ryan Branagan
#Collaborators: N/A
#Branagan_hw2_p1.py
#1/10/19

n=6 #This value determines the first N integers to square and add together
a=0 #We need a to start at a value of zero but it DOES NOT go in the loop
for i in range(1,n+1):
    a = a + i**2
    #print(a) #I used this for troubleshooting and don't want to get rid of it
print('The sum of the first',n,'integers squared is',a)