import scipy
import numpy as np
import math
import pylab as p
#import matplotlib.axes3d as p3
import mpl_toolkits.mplot3d.axes3d as p3

def z_out(p,q,x,y):
	return np.sin(p*math.pi*x)*np.sin(q*math.pi*y)


x = np.linspace(0, 1,100 )
y = np.linspace(0, 1, 100)
xx, yy = np.meshgrid(x, y, sparse=True)

z1=z_out(1.0,1.0,xx,yy)
z2=z_out(2.0,1.0,xx,yy)
z3=z_out(2.0,2.0,xx,yy)


fig=p.figure()
ax = p3.Axes3D(fig)
# x, y, and z are 100x100 arrays
ax.plot_surface(xx,yy,z1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Eigenfunction p=1,q=1')
p.show()

fig=p.figure()
ax = p3.Axes3D(fig)
# x, y, and z are 100x100 arrays
ax.plot_surface(xx,yy,z2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Eigenfunction p=2,q=1')
p.show()


fig=p.figure()
ax = p3.Axes3D(fig)
# x, y, and z are 100x100 arrays
ax.plot_surface(xx,yy,z3)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Eigenfunction p=2,q=2')
p.show()