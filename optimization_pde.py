import math
import pylab as plt
from pde import *
import numpy.linalg as lin
import numpy as np 
import scipy.integrate as sp
import scipy.optimize as op
def even_divide(lst, num_piece):
    return [
        [lst[i] for i in range(len(lst)) if (i % num_piece) == r]
        for r in range(num_piece)
    ]

def innerproduct(u,u_j):
	#print u
	#print "--"
	#print u_j
	product=[]
	for i in range(0,len(u)):
		product.append(u[i,0]*u_j[i])
	#print "f"
	#print len(t)
	#print len(product)
	#print product
	#print t
	
	#print product
	
	#print "--"
	res=sp.simps(product,t)
	#print res
	return res

def innerproduct_end(u,u_j):
	#print u
	#print "--"
	#print u_j
	product=[]
	for i in range(0,len(u)):
		product.append(u[i]*u_j[i])
	#print "f"
	#print len(t)
	#print len(product)
	#print product
	#print t
	
	#print product
	
	#print "--"
	res=sp.simps(product,t)
	#print t
	#print res
	return res

def objectiveFuncEval(u,uList,numberofBasis):
	#print uList.shape
	parsedList= even_divide(uList,numberofBasis)
	temp=parsedList
	for i in range(0,len(parsedList)):
		res=innerproduct(u,parsedList[i])
		#print res
		#print res
		temp[i] = [x * res for x in temp[i]]
		#print temp[i]
	diffsumU=[]
	for ele in range(0,len(temp[1])):
		elementnum=0
		for i in range(0,len(temp)):
			elementnum= elementnum + temp[i][ele]

		diffsumU.append(elementnum)
	finalU=[]
	for i in range(0,len(u)):
		finalU.append((u[i,0]-diffsumU[i])**2)
	res=sp.simps(finalU,t)
	return res


def buildConstrains(uList,i,j,numberofBasis):
	parsedList= even_divide(uList,numberofBasis)
	return innerproduct_end(parsedList[i],parsedList[j])







n=50
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
u=num_sol
#print num_sol
number_of_basis_functions=10


starting=np.ones(((n+1)*number_of_basis_functions,1))
for i in range(0,(n+1)*number_of_basis_functions):
	#starting[i,0] = 0.0
	starting[i,0] = math.cos(i) + math.sin(i)
	#starting[i,0] = i



obj_func = lambda x : objectiveFuncEval(u,x,number_of_basis_functions)

xo=starting
#print xo.shape
#print xo
constraint_list=[]
for i in range(0,number_of_basis_functions):
	for j in range(0,number_of_basis_functions):
		if (i!=j):
			constraint_list.append({'type': 'eq', 'fun': lambda x: buildConstrains(x,i,j,number_of_basis_functions)})
		else:
			constraint_list.append({'type': 'eq', 'fun': lambda x: buildConstrains(x,i,j,number_of_basis_functions) -1.0 })

constraint_list=tuple(constraint_list)
print "done"
res = op.minimize(obj_func, xo,constraints=constraint_list, method='SLSQP',tol=.001,options={"maxiter":10000,"disp": True})
print "finished"
sol =  res.x
parts_of_sol=even_divide(sol,number_of_basis_functions)

'''
for i in parts_of_sol:
	print i
	plt.plot(t,i)
	plt.show()
'''
temp=onedfunc(lambda x: 0.0,t)
firstArray=onedfunc(lambda x: 0.0,t)

for i in range(0,len(parts_of_sol)):
	res=innerproduct(u,parts_of_sol[i])
	second=[x * res for x in parts_of_sol[i]]
	firstArray = [x + y for x, y in zip(firstArray,second )]

for i in range(0,len(parts_of_sol)):
	for j in range(0,len(parts_of_sol)):
		#print (i,j)
		print innerproduct_end(parts_of_sol[i],parts_of_sol[j])

plt.plot(t,firstArray,label="Idiots Approach")







plt.plot(t,truesol,label="True Solution")
plt.plot(t,num_sol,'-',label="Numerical Solution")
plt.legend()
plt.show()