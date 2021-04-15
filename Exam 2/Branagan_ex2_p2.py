#Ryan Branagan
#Collaborators: Mason Lovejoy-Johnson, Steven Boswell, Jack Featherstone, and Grant Sherril
#Branagan_ex2_p2.py
#3/21/19

import numpy as np
import pylab as p
#%%
#Parameters
N = 200
k = 1 #[N/m]
m = 1 #[kg]

#Creating an array to do Linear Algebra on
One = np.ones(N)
One2 = np.ones(N-1)
A = np.diagflat((-2*k*One))
B = np.diagflat((k*One2),k=1)
C = np.diagflat((k*One2),k=-1)
Springs = A+B+C

#Doing Linear Algebra
EigV,EigVec = np.linalg.eigh(Springs)

#Finding the eigenfrequencies
w = np.sqrt(-1*EigV/m)

#Eigen Vectors
Mode1 = EigVec[:,0]
Mode2 = EigVec[:,1]
Mode99 = EigVec[:,98]
Mode100 = EigVec[:,99]
Mode199 = EigVec[:,198]
Mode200 = EigVec[:,199]


#Plotting
Index = np.arange(0,N,1)
fig1,freq = p.subplots(1,1)
freq.plot(Index,w,"ro")
freq.set_title("Eigenfrequency vs Index Value")
freq.set_xlabel("Index Value")
freq.set_ylabel("Eigenfrequency [1/s]")

fig2,((M1,M2),(M99,M100),(M199,M200)) = p.subplots(3,2,figsize=(12,10))
M1.plot(Mode1,"r-")
M1.set_title("M1")
M2.plot(Mode2,"o-")
M2.set_title("M2")
M99.plot(Mode99,"y-")
M99.set_title("M99")
M100.plot(Mode100,"g-")
M100.set_title("M100")
M199.plot(Mode199,"b-")
M199.set_title("M199")
M200.plot(Mode200,"m-")
M200.set_title("M200")

fig3,Art = p.subplots(1,1)
Art.plot(EigVec)