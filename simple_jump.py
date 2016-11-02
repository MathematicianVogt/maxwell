import math
import numpy as np
import matplotlib.pyplot as plt

class solver:
	def __init__(self,number):
		a=0
		b=1
		n=number
		alpha=.5
		dx= (b-a)/float(n)
		pos=None
		x_list=[]
		for i in range(0,n+1):
			x_list.append(a+i*dx)

		for j in range(0,n):
			if(x_list[j] <= alpha and x_list[j+1]>alpha):
				pos=j






		A=np.zeros((n+1,n+1))
		b=np.zeros((n+1,1))
		c=np.zeros((n+1,1))
		A[0,0]=1.0
		for i in range(1,n+1):
			A[i,i-1]=-(1.0+dx)
			A[i,i]=1.0

		truesol=[]
		for i in x_list:
			if i < alpha:
				truesol.append(math.exp(i))
			else:
				truesol.append(0.0)



		c[0,0]=1.0
		step=x_list[pos+1]-alpha
		#c[pos,0]=((1.0)/step)*(-math.exp(alpha) - (x_list[pos+1] -alpha)*math.exp(alpha)) +((1.0)/step)*math.exp(alpha)
		c[pos,0]=(1.0/dx)*(-math.exp(alpha)-math.exp(alpha)*(x_list[pos+1]-alpha)) -(1.0/dx)*(-math.exp(alpha)-math.exp(alpha)*(x_list[pos]-alpha))
		sol = np.linalg.solve(A,c)

		regular_error=0
		special_error=0
		for i in range(0,len(x_list)):
			if(i==pos+1):
				special_error=math.fabs(sol[i]-truesol[i])
			else:
				if(math.fabs(sol[i]-truesol[i])>regular_error):
					regular_error=math.fabs(sol[i]-truesol[i])


		self.re=regular_error
		self.se=special_error
		plt.plot(x_list,sol, "--",label="Numerical Solution")
		plt.plot(x_list,truesol, label="True Solution")
		plt.legend()
		plt.show()

	def errors(self):
		return (self.re,self.se)

	
point_list=[]
for i in range(0,9):
	points=16
	n=points*(2**i)
	x=solver(n)
	tup_err=x.errors()
	point_list.append((n,tup_err[0],tup_err[1]))

print "n     regular error rate     special error rate"
for i in range(0,len(point_list)-1):
	print str(point_list[i+1][0]) + " - " + str(point_list[i][1]/point_list[i+1][1]) + " - " + str(point_list[i][2]/point_list[i+1][2])



