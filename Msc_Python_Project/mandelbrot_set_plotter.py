"""
Msc Python Project (2021)
Name: Prathamesh k Deshmukh
Que 4 Plot of Mandelbrot set (fractal)

Description:
This script generates and plots a visual representation of the Mandelbrot set,
a famous mathematical fractal. It works by iterating over a grid of points in
the complex plane. For each complex number 'c', it applies the iterative
function z = z^2 + c for a fixed number of iterations. If the absolute value
of 'z' remains bounded (i.e., less than or equal to 2), the point 'c' is
considered to be part of the set.

The script collects all such points and uses Matplotlib to create a scatter
plot, revealing the characteristic shape of the Mandelbrot set. The resolution
of the plot can be adjusted by changing the step size and the number of
iterations. The final plot is displayed and also saved as an image file.

Dependencies:
- numpy
- matplotlib

Usage:
Run the script directly. The generation process may take some time depending
on the resolution settings. The plot will be shown on the screen and saved as
'IMG_Mandelbrot1.png' in the same directory.
"""

import numpy as np
import matplotlib.pyplot as plt

li1=[]

#fuction defination and loop

def fun(a):

 global z
 z=0
 for ind in range(25): #recommended value 10 to 25 (you can increase it depending on your computational power)

  z=z*z+a
 return z
 print(z)

#float range
start =- 2.5 #recc -2.5
stop = 2.5 #recc -2.5
step = 0.005 #recc 0.005

float_range_array = np.arange(start, stop, step)


def point():

 for x in  list(float_range_array) :
  for y in  list(float_range_array) :

    global c
    c = complex(x,y)

    if abs(fun(c))<=2:
     li1.append(c)


#function calling

point()
arr0=np.array(li1)


#Ploting the graph

plt.scatter(arr0.real,arr0.imag,s=5,color="black")
plt.xlim([-3, 3])
plt.ylim([-3, 3])

plt.xlabel("Real axis")
plt.ylabel("imaginary axis ")
plt.title("plot of Mandelbrot set ")
plt.savefig('IMG_Mandelbrot1.png')

plt.show()
