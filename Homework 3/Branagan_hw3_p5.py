#Ryan Branagan
#Collaborators: N/A
#Branagan_hw3_p5.py
#1/24/19

from scipy.integrate import quad

def square(x):
    return x**2

print(quad(square,0,6))