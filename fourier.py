from pde import *
import math
import pylab as plt

interval  = onedinterval(0,math.pi/2.0,1000)


func = lambda x: (8.0/(math.pi *3.0)) * math.sin(2*x) +(16.0/(15.0* math.pi)) * math.sin(4*x) +(24.0/(35.0* math.pi)) * math.sin(6*x) +(32.0/(63.0* math.pi)) * math.sin(8*x) + (40.0/(99.0* math.pi)) * math.sin(10*x) +(48.0/(143.0* math.pi)) * math.sin(12*x)
cos = lambda x: math.cos(x)
output =[]
output2=[]

for i in interval:
	output.append(func(i))
	output2.append(cos(i))




plt.plot(interval,output,"*",label="sin series")
plt.plot(interval,output2,label="cosx")
plt.legend()
plt.show()
