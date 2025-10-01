"""
Msc Python Project (2021)
Name: Prathamesh Deshmukh
Que 1 Matrix Multiplication

Description:
This script performs matrix multiplication on two matrices provided by the user.
It first prompts the user to enter the dimensions (rows and columns) and then
the individual elements for each matrix. The script validates if the matrices
are compatible for multiplication (i.e., columns of the first matrix equal
rows of the second). The multiplication is implemented from scratch using a
manual, triple-nested loop algorithm. The NumPy library is used only to confirm
the dimensions of the input and resulting matrices, not for the calculation itself.

Dependencies:
- numpy

Usage:
Run the script from the command line. Follow the prompts to enter the
dimensions and elements for both matrices. The resulting matrix or an
error message will be printed to the console.
"""

import numpy as np


#for matrix 1

R1 = int(input("Enter the number of rows of  matrix 1:"))
C1 = int(input("Enter the number of columns: of  matrix 1:"))


matrix1= [ ]
print("Enter Element Row wise:")

for i in range(R1):
    a1 =[ ]
    for j in range(C1):
         a1.append(int(input()))
    matrix1.append(a1)


X=np.array(matrix1)

print("The first matrix you have enter is :")
for i in range(R1):
    for j in range(C1):
        print(matrix1[i][j], end = " ")
    print()
X=np.array(matrix1)
print("Matrix 1 dimmension is ",X.shape)

 #for matrix 2

R2 = int(input("Enter the number of rows of second matrix:"))
C2 = int(input("Enter the number of columns of second matrix:"))


matrix2 = [ ]
print("Enter the Element row wise:")

for i in range(R2):
    a2 =[ ]
    for j in range(C2):
         a2.append(int(input()))
    matrix2.append(a2)

print("The Second matrix you have enter is :")
for i in range(R2):
    for j in range(C2):
        print(matrix2[i][j], end = " ")
    print()

Y=np.array(matrix2)
print("Matrix 2 dimmension is ",Y.shape)


A=matrix1
B=matrix2

#matrix3 defn

def Matrix_multiplication():
    list_null1=[]
    list_null2=[]
    matrix3=[]



    for ind1 in range(C2):
    		list_null1.append(0)
    for ind2 in range(R1):
    	list_null2=list_null1[:]
    	matrix3.append(list_null2)

    for i in range(len(A)):

    # iterating by coloum by B
        for j in range(len(B[0])):

        # iterating by rows of B
            for k in range(len(B)):
                matrix3[i][j] += A[i][k] * B[k][j]


    print("The  matrix multiplication is :")
    for i in range(R1):
        for j in range(C2):
            print(matrix3[i][j], end = " ")
        print()


    Z=np.array(matrix3)
    print("Matrix multiplication dimmension is ",Z.shape)


if (R2==C1) :
	Matrix_multiplication()

else:
	print("\n Sorry Matrix multiplication not Possible \n ")
	print("matrix Dimmension  is  not Compatible for multiplication ! \n ")
	print("\n As Column of 1st matrix are ",C1,"which are not equal to the row of 2nd Matrix which are \n ",R2)
