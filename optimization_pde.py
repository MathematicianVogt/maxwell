import math
import pylab as plt
from pde import *
import numpy.linalg as lin
import numpy as np 

n=1000
a=0
b=math.pi/2.0
t=onedinterval(a,b,n)
dx=(b-a)/float(n)
truesol=onedfunc(lambda x: math.sin(x)+math.cos(x),t)

A=np.zeros((n+1,n+1))
A[0,0]=1.0
A[n,n]=1.0
for i in range(1,n):
	A[i,i]=(-2.0/dx**2) +1.0
	A[i,i-1]= 1.0/dx**2
	A[i,i+1]=1.0/dx**2


b=np.zeros((n+1,1))
b[0,0]=1.0
b[n,0]=1.0

num_sol= lin.solve(A,b)

basis_list_sol=[]
number_of_basis=10

for i in range(0,number_of_basis):
	basis_list_sol.append(np.ones((n+1,1)))


empty_list=basis_list_sol
print empty_list







plt.plot(t,truesol,label="True Solution")
plt.plot(t,num_sol,label="Numerical Solution")
plt.legend()
plt.show()