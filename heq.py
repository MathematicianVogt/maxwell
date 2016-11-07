import math
import scipy.optimize as sp
from pde import *
import numpy.linalg as np
h_array=[]
counter=1

counter=1

def f(x,t,c,N):
	global counter
	fList=[]
	for i in range(0,len(x)):
		integralSum=0
		for j in range(0,len(x)):
			integralSum = integralSum + (t[i]*x[i]*x[j])/(t[i]+t[j])


		fList.append(x[i] - 1.0 -(c/2.0)*(1.0/float(N))*(integralSum))
	h_array.append(fList)
	innteration.append(counter)
	counter=counter+1
	return fList

N=100
tList = onedinterval(0.0,1.0,N)
tList=tList[1:]
first=1.0
h_int = onedfunc(lambda x : math.cos(x),tList)
c=.9
h_array.append(h_int)
innteration=[0]
res=sp.fsolve(f,h_int,args=(tList,c,N))
print res
res=list(res)
res.insert(0,first)
tList=list(tList)
tList.insert(0,0.0)

normvals=onedfunc(lambda x: np.norm(x,2),h_array)
plt.plot(tList,res)
plt.title("Chandrasekhar H-equation")
plt.xlabel("t")
plt.ylabel("H(t)")
plt.show()
plt.plot(innteration,normvals)
plt.title("Norm of F(x)")
plt.xlabel("Itteration step")
plt.ylabel("||F(x)||")
plt.show()
