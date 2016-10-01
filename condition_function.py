import math
import numpy
import matplotlib.pyplot as plt
def f(x):
	return (1+x-1)/x



inputstuff = numpy.linspace(math.pow(10.0,-16),math.pow(10.0,-14),100)
inputstufftwo =numpy.linspace(10.0,20.0,100)
print 
print inputstuff
output=[]
outputprime=[]
outputtwo=[]
for i in range(0,len(inputstuff)):
	output.append(f(inputstuff[i]))
	outputprime.append(1.0)
	outputtwo.append(f(inputstufftwo[i]))

'''
plt.plot(inputstuff,output , label=r"$f(x)=\frac{1+x-1}{x}$")
plt.plot(inputstuff,outputprime,'o',label=r"$f(x)=1$")
plt.xlabel(r"$x$")
plt.ylabel(r"$f(x)$")
plt.legend(loc='lower right')
plt.show()
'''

plt.plot(inputstufftwo,outputtwo , label=r"$f(x)=\frac{1+x-1}{x}$")
plt.plot(inputstufftwo,outputprime,'o',label=r"$f(x)=1$")
plt.xlabel(r"$x$")
plt.ylabel(r"$f(x)$")
plt.legend(loc='lower right')
plt.show()

