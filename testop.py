import scipy.optimize as op
import math


f= lambda x: -math.sin(x)
x0=[1.0]
bnds=((-math.pi/2,math.pi/2),)
res = op.minimize(f,x0,bounds=bnds)
print res.x