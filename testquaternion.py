import numpy as np
import matplotlib.pyplot as plt
from pyquaternion import Quaternion
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D

q1 = Quaternion([0.297503, 0.732980, -0.609154, -0.056238])
q2 = Quaternion([0.295055, 0.734368, -0.609348, -0.048385])
q3 = Quaternion([0.171573, 0.749697, -0.637742, 0.042468])
angle = q3.degrees - q1.degrees
print(angle)
print(q1.axis, q1.degrees)
print(q3.axis, q3.degrees)
print(q1)
print(q2)
print(q3)

s = np.linspace(0,2*np.pi,100)
x = np.cos(s)
y = np.sin(s)
z = np.zeros_like(x)
#fig = plt.figure()
#ax = fig.gca(projection='3d')
#ax.plot(x,y,zs=0,zdir='z',label='transformation with Quaternions')
#plt.show()

q = Quaternion(axis=[0, 1, 0], angle=np.pi / 2)
P = np.stack((x,y,z))
# make an empty matrix
Pr = np.zeros((len(s),3))
# rotate points one by one
for i in range(len(s)):
    Pr[i][:] = q3.rotate([x[i], y[i], z[i]])
 
# transpose for shape consistency
Pr = Pr.transpose()
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x,y,zs=0,zdir='z',label='transformation with Quaternions')
ax.plot(Pr[:][0], Pr[:][1], Pr[:][2],'r')
plt.show()

