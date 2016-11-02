import math
from pde import *
import numpy as np
import matplotlib.pyplot as plt
def secant(func,x0,esp,title):
	xm1=.99*x0
	x0=x0
	temp = x0

	it_num=[0]
	val_num=[x0]
	counter=1
	while(math.fabs(xm1-x0)>esp):
		temp = x0
		x0 = x0 - func(x0)*(x0-xm1)/(func(x0)-func(xm1))
		it_num.append(counter)
		val_num.append(x0)
		counter+=1
		xm1 = temp

	return (it_num,val_num,title)


def newton(func,x0,esp,title):
	preval=x0+1

	it_num=[0]
	val_num=[x0]
	counter=1
	while(math.fabs(x0-preval)>esp):
		preval=x0
		x0 = x0 - func(x0)/derv(func,x0,.001)
		it_num.append(counter)
		val_num.append(x0)
		counter+=1


	return (it_num,val_num,title)


def chord(func,x0,esp,title):
	preval=x0+1

	it_num=[0]
	val_num=[x0]
	counter=1
	derval=derv(func,x0,.001)
	while(math.fabs(x0-preval)>esp):
		preval=x0
		x0 = x0 - func(x0)/derval
		it_num.append(counter)
		val_num.append(x0)
		counter+=1


	return (it_num,val_num,title)


def mainFunc(f,x0,esp,title):
	(a1,a2,a3)  = secant(f,x0,esp,title)
	(b1,b2,b3)  = newton(f,x0,esp,title)
	(c1,c2,c3)  = chord(f,x0,esp,title)
	


	plt.plot(a1,a2,label="Secant Method")
	plt.plot(b1,b2,label="Newton Method")
	plt.plot(c1,c2,label="Chord Method")
	#plt.title(r'%s' %(title))
	plt.legend()
	plt.show()

f1=lambda x: math.cos(x) -x
f2=lambda x: np.arctan(x)
f3=lambda x: math.sin(x)
f4=lambda x: x**2
f5=lambda x: x**2 +1




mainFunc(f1,.5,.01,"$cos(x) -x$")
mainFunc(f2,1.0,.01,"$arctan(x)$")
mainFunc(f3,3.0,.01,"$sin(x) $")
mainFunc(f4,.5,.01,"$x^2$")
#mainFunc(f5,10.0,.01,"$x^2+1$")





