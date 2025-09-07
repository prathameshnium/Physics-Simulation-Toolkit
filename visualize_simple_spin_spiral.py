#actual simulation test (canted magnetism)
#Simulating_magnetic_ordering

'''
===================================================================
   Simple Visualization of a 1D Helical Magnetic Spin Structure
===================================================================
Author: [Your Name/Lab]
Date: 2025-09-07

Description:
-----------
This script generates and visualizes a simple model of a one-dimensional 
helical magnetic structure, often called a "spin spiral." It plots a 
series of vectors (representing magnetic moments or spins) arranged 
along the Y-axis, where each vector is progressively rotated in the 
X-Z plane.

This type of visualization is fundamental for understanding concepts 
like helimagnetism and canted magnetic ordering in condensed matter 
physics.

Method:
-------
1.  A chain of points is created along the Y-axis.
2.  At each point, a 3D vector is calculated with its X and Z components 
    determined by `sin(i)` and `cos(i)`, respectively. This creates a 
    circular rotation.
3.  The vectors are plotted using Matplotlib's 3D quiver plot.
4.  A red line is added to trace the tips of the vectors, clearly 
    showing the resulting helical path.
5.  Finally, it calculates and plots the net magnetic moment (the vector 
    sum of all individual spins), which illustrates that for a full spiral, 
    the net moment can approach zero.

'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

X=[]
Y=[]
Z=[]
U=[]
V=[]
W=[]
pi=3.14
for i in range(40):
    X.append(0)
    Y.append(i)
    Z.append(0)
    U.append(np.sin(i))
    V.append(0)
    W.append(np.cos(i))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X, Y, Z, U, V, W)
ax.set_xlim([-5, 5])
ax.set_ylim([0,20])
ax.set_zlim([-5, 5])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
X1=[]
Y1=[]
Z1=[]

for i in range(40):
    X1.append(X[i]+U[i])
    Y1.append(Y[i]+V[i])
    Z1.append(Z[i]+W[i])

ax.plot3D(X1,Y1,Z1,c="red")
U1=V1=W1=0
#vector addition of all magnetic moment
for i in range(40):
    U1=U1+U[i]
    V1=V1+V[i]
    W1=W1+W[i]
ax.quiver(0, 0, 0, U1, V1, W1,lw=5)
plt.show()
