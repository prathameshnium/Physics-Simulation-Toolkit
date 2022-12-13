#actual simulation test (canted magnetism)

%matplotlib notebook
from ipywidgets import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

X=[]
Y=[]
Z=[]
U=[]
V=[]
W=[]
'''
def update(A = 0.5, B = 0, C = 0.5):

    line.set_ydata(f(x,A,B,C))


    fig.canvas.draw_idle()
    
interact(update, A = (-1,1,0.1), B = (-1,1,0.1), C = (-1,1,0.1))
'''
k1=0.5
k2=0
k3=0.5
k11=k33=0
for i in range(40):
    X.append(0)
    Y.append(i)
    Z.append(0)
    k11=k11+k1
    k33=k33+k3
    U.append(2*pow(np.sin(k11*pi),1))
    V.append(0)
    W.append(2*pow(np.sin(-k33*pi),1))

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



#0,146
ax.view_init(0,146)
plt.show()

