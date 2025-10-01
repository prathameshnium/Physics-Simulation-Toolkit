"""
Msc Python Project (2021)
Name: Prathamesh k Deshmukh
Que 3 Projectile motion

Description:
This script simulates and plots the trajectory of a projectile launched from an
initial height with a given initial velocity. It calculates and compares the
motion for several predefined launch angles (30, 45, and 60 degrees).

For each angle, the script computes key physical quantities:
- Time of flight (by solving the quadratic equation for vertical displacement)
- Horizontal range
- Maximum height achieved
- Final velocity components upon impact

The script generates a comparative plot showing the trajectory for each launch
angle on a single graph using Matplotlib. Additionally, it logs the calculated
physical quantities to 'myfile02.txt' and the time-stamped coordinates of
each trajectory to 'myfile01.txt'.

Dependencies:
- numpy
- matplotlib

Usage:
Run the script directly. The initial conditions like height 'h', initial
speed 'u', and the list of angles can be modified in the script to simulate
different scenarios. The output will be a plot displayed on the screen and two
data files saved in the same directory.
"""

import matplotlib.pyplot as plt
import numpy as np

#data
h=10#m
u=30 #m/sec
g=9.8 #m/s^2
ax=0 #m/s^2
ay=-g #m/s^2


lix=[]
liy=[]


file1=open("myfile01.txt",'w+')
file2=open("myfile02.txt",'w+')


def time_of_flight(thita) :



    global t_flight
    global ux
    global uy
    global a
    global thita0

    ux=u*np.cos(np.deg2rad(thita))
    uy=u*np.sin(np.deg2rad(thita))

    a=g
    b =-2*u*np.sin(np.deg2rad(thita))
    c = -2*h
    dis = (b**2) - (4 * a*c)

# find two results
    t1 = (-b-np.sqrt(dis))/(2 * a)
    t2 = (-b + np.sqrt(dis))/(2 * a)
#positive time
    if t1>0:
    	t_flight=t1
    elif t2>0:
    	t_flight=t2
    else:
    	t_flight=0

    file2.write(' * '+'time  of flight is '+str(t_flight)+'\n')


##############


def x_range(thita):
	global R
	R=u*(np.cos(np.deg2rad(thita)))*(t_flight)
	#print('Range is ',R)
	file2.write(' * '+ 'Range is '+str(R)+'\n')

###############


def final_Velocity(thita):
	global a

	vx=ux

	vy=uy+a*(t_flight)

	#print(vx,' i +',vy,' j ')

	file2.write(' * '+'final velocity when particle hit the ground is  '+str(vx)+'i +' + str(vy)+' j'+'\n')

##############

def max_Height(thita):
	#Height will be maxima at time
	global a
	global uy
	global ay

	time5=(uy)/(-ay)
	Height1=(uy)*(time5)+(0.5*(ay)*(time5)**2)

	Height2=Height1+h


	file2.write(' * '+ 'maximum y displacement of paricle  is '+str(Height1)+'\n')
	file2.write(' * '+ 'maximum Height from the ground (y=0) '+str(Height2)+'\n\n')


def Computation(thita) :

   #function calling

    time_of_flight(thita)

    x_range(thita)

    final_Velocity(thita)

    max_Height(thita)



    start =0
    stop = t_flight+(t_flight/100)
    step = t_flight/100



    float_range_array = np.arange(start, stop, step)



    for time in list(float_range_array):




    	sx=ux*(time)+0.5*ax*time**2
    	sy=h+uy*(time)+0.5*ay*time**2
    	file1.write('\n'+'at t='+str(time))



    	lix.append(sx)
    	liy.append(sy)




    	file1.write('\n'+'('+str(sx)+' , '+str(sy)+')\n')


for thita0 in [30,45,60] :


	 #global t_flight
	 file1.write('\n For angle :- '+str(thita0)+'\n')

	 file2.write('For angle :- '+str(thita0)+'\n')


	 if thita0==30:


	   Computation(thita0)

	   plt.plot(np.array(lix),np.array(liy),color='green', linewidth=2,label='30 Degrees')



	   lix.clear()
	   liy.clear()


	 elif thita0==45:
	   	Computation(thita0)
	   	plt.plot(np.array(lix),np.array(liy),color='blue', linewidth=2,label='45 Degrees')
	   	lix.clear()
	   	liy.clear()



	 elif thita0==60:
	   	Computation(thita0)
	   	plt.plot(np.array(lix),np.array(liy),color='black', linewidth=2,label='60 Degrees')
	   	lix.clear()
	   	liy.clear()


lix.clear()
liy.clear()


plt.legend()
plt.title('Projectile motion',fontsize=28,color="grey")

plt.xlabel('X axis',fontsize=18)
plt.ylabel(' Y axis',fontsize=18)
plt.grid()
plt.show()


file1.close()
file2.close()
