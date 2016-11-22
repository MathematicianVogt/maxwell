import math
import scipy.optimize as op
import scipy.integrate as sp
from pde import *
import time

a=0.0
b=10.0
N=50
t=onedinterval(a,b,N)
f0=onedfunc(lambda x : math.cos(x), t)
true = onedfunc(lambda x: x , t)
c1 = {'type': 'eq', 'fun': lambda x:x[0]-a}
c2={'type': 'eq', 'fun': lambda x:x[N]-b}
constrains_list = (c1,c2)
solutionSeqPlot=[]
def obj_func(f,t,dx):
	solutionSeqPlot.append(f)
	#print t
	#print "-----"
	#print f[0]
	#print f[len(f)-1]
	#print "-----"
	dervList=[]
	for i in range(0,len(f)):
		if i== len(f)-1:
			dervList.append((f[i]-f[i-1])/dx  )
		elif i== 0:
			dervList.append((f[i+1]-f[i])/dx )
		else:
			dervList.append((f[i+1]-f[i-1])/(2.0*dx) )
	#print dervList
	#time.sleep(2)
	finalList=[]
	for i in range(0,len(dervList)):
		finalList.append(math.sqrt(1.0 + dervList[i]**2))
	res = sp.simps(finalList,t)
	#print dervList
	return res

def grad(f,t,dx):
	grad=[]
	for i in range(0,len(f)):
		if i==0:
			grad.append((dx/3.0))
		elif i==len(f)-1:
			grad.append((dx/3.0))
		elif i%2==0:
			grad.append((2.0*dx/3.0))
		else:
			grad.append((4.0*dx/3.0))
	#print grad
	return grad


#res = op.minimize(obj_func, f0,constraints=constrains_list, method='SLSQP',options={"maxiter":100,"disp": True},args=(t,math.fabs(t[1]-t[0])))
res = op.minimize(obj_func, f0,constraints=constrains_list, method='SLSQP',options={"maxiter":100,"disp": True},args=(t,math.fabs(t[1]-t[0])))

print "finished"
print res.x[0]
print res.x[N]
diff=[]
for i in range(0,len(true)):
	diff.append(math.fabs(res.x[i]-true[i]))
print max(diff)


step_list=[]
for i in range(0,len(solutionSeqPlot)):
	step_list.append(i)



plt.plot(t,true, label="true solution")
plt.plot(t,res.x, '*' ,label = "numerical solution")
plt.xlim(a, b+5)
plt.legend()
plt.show()
makeMovie(t, solutionSeqPlot,step_list,"200 points Variational Problem cos(x)","x","y")

