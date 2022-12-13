#actual simulation test (canted magnetism)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

X=[]
Y=[]
Z=[]
U=[]
V=[]
W=[]

k1=0.4
k2=0
k3=0.6
k11=k33=0
for i in range(40):
    X.append(0)
    Y.append(i)
    Z.append(0)
    k11=k11+k1
    k33=k33+k3
    U.append(pow(np.sin(k11),1))
    V.append(0)
    W.append(pow(np.sin(-k33),1))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X, Y, Z, U, V, W)
ax.set_xlim([-5, 5])
ax.set_ylim([5,20])
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


""""
#vector addition of all magnetic moment
for i in range(40):
    U1=U1+U[i]
    V1=V1+V[i]
    W1=W1+W[i]
ax.quiver(0, 0, 0, U1, V1, W1,lw=5)

"""
ax.view_init(0,146)
plt.show()
