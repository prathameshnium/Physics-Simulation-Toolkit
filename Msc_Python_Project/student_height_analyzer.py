"""
Msc Python Project (2021)
Name: Prathamesh Deshmukh
Que 2 Dictionary of Ten Students

Description:
This script collects the names and heights of ten students and performs a
basic analysis of the data. It interactively prompts the user to enter a
name and height (in feet and inches) for each student. The information is
stored in a dictionary, with the student's name as the key and their total
height in inches as the value.

After collecting all the data, the script processes it to:
1. Find the student with the maximum height.
2. Calculate the average height of all students.

The results are then printed to the console in a human-readable format
(e.g., "5 feet 10 Inches").

Dependencies:
None (uses only built-in Python libraries).

Usage:
Run the script from the command line. Follow the prompts to enter the name,
feet, and inches for each of the ten students. The final analysis will be
displayed after the tenth student's data is entered.
"""

dict1={}
t=0


def input_feet_inch():
	global value
	print("Input height")

	h_ft = int(input("Feet: "))
	h_inch = int(input("Inches: "))
	h_inch += h_ft * 12
	value=h_inch


def inch_to_feet_inch(a):
	feet1=int(a/12)
	inch1=int(a%12)
	return str(feet1)+' feet '+str(inch1)+' Inches '


while t<10 :
          key=input('Enter the Name :')
          #value=input("enter the Height for given")
          input_feet_inch()


          dict1[key]=value
          t=t+1



p= list(dict1.values())


for i in dict1:
    if dict1[i]==max(p):


        print("* Student with maximum height is ",i," and his height is : ",inch_to_feet_inch(max(p)))



z=0
for i in range(0, len(p)):
    p[i] = int(p[i])



#sum
for j in range(0, len(p)):
    z=z+ p[j]

#avg
h1=int(z)/len(p)
print("* Average Height is : ",inch_to_feet_inch(h1))
