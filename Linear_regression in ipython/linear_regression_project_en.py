
# coding: utf-8

# # 1 Matrix operations
# 
# ## 1.1 Create a 4*4 identity matrix

# In[1]:

#This project is designed to get familiar with python list and linear algebra
#You cannot use import any library yourself, especially numpy

A = [[1,2,3], 
     [2,3,3], 
     [1,2,5]]

B = [[1,2,3,5], 
     [2,3,3,5], 
     [1,2,5,1]]

#TODO create a 4*4 identity matrix 
I = None


# ## 1.2 get the width and height of a matrix. 

# In[ ]:

#TODO Get the height and weight of a matrix.
def shape(M):
    return 0,0


# ## 1.3 round all elements in M to certain decimal points

# In[ ]:

# TODO in-place operation, no return value
# TODO round all elements in M to decPts
def matxRound(M, decPts=4):
    pass


# ## 1.4 compute transpose of M

# In[ ]:

#TODO compute transpose of M
def transpose(M):
    return None


# ## 1.5 compute AB. return None if the dimensions don't match

# In[ ]:

#TODO compute matrix multiplication AB, return None if the dimensions don't match
def matxMultiply(A, B):
    return None


# ## 1.6 Test your implementation

# In[ ]:

#TODO test the shape function

#TODO test the round function

#TODO test the transpose funtion

#TODO test the matxMultiply function, when the dimensions don't match

#TODO test the matxMultiply function, when the dimensions do match


# # 2 Gaussian Jordan Elimination
# 
# ## 2.1 Compute augmented Matrix 
# 
# $ A = \begin{bmatrix}
#     a_{11}    & a_{12} & ... & a_{1n}\\
#     a_{21}    & a_{22} & ... & a_{2n}\\
#     a_{31}    & a_{22} & ... & a_{3n}\\
#     ...    & ... & ... & ...\\
#     a_{n1}    & a_{n2} & ... & a_{nn}\\
# \end{bmatrix} , b = \begin{bmatrix}
#     b_{1}  \\
#     b_{2}  \\
#     b_{3}  \\
#     ...    \\
#     b_{n}  \\
# \end{bmatrix}$
# 
# Return $ Ab = \begin{bmatrix}
#     a_{11}    & a_{12} & ... & a_{1n} & b_{1}\\
#     a_{21}    & a_{22} & ... & a_{2n} & b_{2}\\
#     a_{31}    & a_{22} & ... & a_{3n} & b_{3}\\
#     ...    & ... & ... & ...& ...\\
#     a_{n1}    & a_{n2} & ... & a_{nn} & b_{n} \end{bmatrix}$

# In[ ]:

#TODO construct the augment matrix of matrix A and column vector b, assuming A and b have same number of rows
def augmentMatrix(A, b):
    return None


# ## 2.2 Basic row operations
# - exchange two rows
# - scale a row
# - add a scaled row to another

# In[ ]:

# TODO r1 <---> r2
# TODO in-place operation, no return value
def swapRows(M, r1, r2):
    pass

# TODO r1 <--- r1 * scale
# TODO in-place operation, no return value
def scaleRow(M, r, scale):
    pass

# TODO r1 <--- r1 + r2*scale
# TODO in-place operation, no return value
def addScaledRow(M, r1, r2, scale):
    pass


# ## 2.3  Gauss-jordan method to solve Ax = b
# 
# ### Hint：
# 
# Step 1: Check if A and b have same number of rows
# Step 2: Construct augmented matrix Ab
# 
# Step 3: Column by column, transform Ab to reduced row echelon form [wiki link](https://en.wikipedia.org/wiki/Row_echelon_form#Reduced_row_echelon_form)
#     
#     for every column of Ab (except the last one)
#         column c is the current column
#         Find in column c, at diagnal and under diagnal (row c ~ N) the maximum absolute value
#         If the maximum absolute value is 0
#             then A is singular, return None （Prove this proposition in Question 2.4）
#         else
#             Apply row operation 1, swap the row of maximum with the row of diagnal element (row c)
#             Apply row operation 2, scale the diagonal element of column c to 1
#             Apply row operation 3 mutiple time, eliminate every other element in column c
#             
# Step 4: return the last column of Ab
# 
# ### Remark：
# We don't use the standard algorithm first transfering Ab to row echelon form and then to reduced row echelon form.  Instead, we arrives directly at reduced row echelon form. If you are familiar with the stardard way, try prove to yourself that they are equivalent. 

# In[ ]:

#TODO implement gaussian jordan method to solve Ax = b

""" Gauss-jordan method to solve x such that Ax = b.
        A: square matrix, list of lists
        b: column vector, list of lists
        decPts: degree of rounding, default value 4
        epsilon: threshold for zero, default value 1.0e-16
        
    return x such that Ax = b, list of lists 
    return None if A and b have same height
    return None if A is (almost) singular
"""

def gj_Solve(A, b, decPts=4, epsilon = 1.0e-16):
    return None


# ## 2.4 Prove the following proposition:
# 
# **If square matrix A can be divided into four parts: ** 
# 
# $ A = \begin{bmatrix}
#     I    & X \\
#     Z    & Y \\
# \end{bmatrix} $, where I is the identity matrix, Z is all zero and the first column of Y is all zero, 
# 
# **then A is singular.**
# 
# Hint: There are mutiple ways to prove this problem.  
# - consider the rank of Y and A
# - consider the determinate of Y and A 
# - consider certain column is the linear combination of other columns

# TODO Please use latex （refering to the latex in problem may help）
# 
# TODO Proof：

# ## 2.5 Test your gj_Solve() implementation

# In[ ]:

# construct A and b where A is singular
# construct A and b where A is not singular
# solve x for  Ax = b 
# compute Ax
# compare Ax and b

# TODO


# # 3 Linear Regression: 
# 
# ## 3.1 Compute the gradient of loss function with respect to parameters 
# ## (Choose one between two 3.1 questions)
# 
# We define loss funtion E as 
# $$
# E(m, b) = \sum_{i=1}^{n}{(y_i - mx_i - b)^2}
# $$
# 
# Proves that 
# $$
# \frac{\partial E}{\partial m} = \sum_{i=1}^{n}{-2x_i(y_i - mx_i - b)}
# $$
# 
# $$
# \frac{\partial E}{\partial b} = \sum_{i=1}^{n}{-2(y_i - mx_i - b)}
# $$
# 
# $$
# \begin{bmatrix}
#     \frac{\partial E}{\partial m} \\
#     \frac{\partial E}{\partial b} 
# \end{bmatrix} = 2X^TXh - 2X^TY
# $$
# 
# $$ 
# \text{, where }
# Y =  \begin{bmatrix}
#     y_1 \\
#     y_2 \\
#     ... \\
#     y_n
# \end{bmatrix}
# ,
# X =  \begin{bmatrix}
#     x_1 & 1 \\
#     x_2 & 1\\
#     ... & ...\\
#     x_n & 1 \\
# \end{bmatrix},
# h =  \begin{bmatrix}
#     m \\
#     b \\
# \end{bmatrix}
# $$

# TODO Please use latex （refering to the latex in problem may help）
# 
# TODO Proof：

# ## 3.1 Compute the gradient of loss function with respect to parameters 
# ## (Choose one between two 3.1 questions)
# 
# Proves that 
# $$
# E = Y^TY -2(Xh)^TY + (Xh)^TXh
# $$
# 
# $$
# \frac{\partial E}{\partial h} = 2X^TXh - 2X^TY
# $$
# 
# $$ 
# \text{,where }
# Y =  \begin{bmatrix}
#     y_1 \\
#     y_2 \\
#     ... \\
#     y_n
# \end{bmatrix}
# ,
# X =  \begin{bmatrix}
#     x_1 & 1 \\
#     x_2 & 1\\
#     ... & ...\\
#     x_n & 1 \\
# \end{bmatrix},
# h =  \begin{bmatrix}
#     m \\
#     b \\
# \end{bmatrix}
# $$

# TODO Please use latex （refering to the latex in problem may help）
# 
# TODO Proof：

# ## 3.2  Linear Regression
# ### Solve equation $X^TXh = X^TY $ to compute the best parameter for linear regression.

# In[ ]:

#TODO implement linear regression 
'''
points: list of (x,y) tuple
return m and b
'''
def linearRegression(points):
    return 0,0


# ## 3.3 Test your linear regression implementation

# In[ ]:

#TODO Construct the linear function

#TODO Construct points with gaussian noise
import random

#TODO Compute m and b and compare with ground truth


# ## 4.1 Unittests
# 
# Please make sure yout implementation passed all the unittests

# In[ ]:

import unittest
import numpy as np

from decimal import *

class LinearRegressionTestCase(unittest.TestCase):
    """Test for linear regression project"""

    def test_shape(self):

        for _ in range(10):
            r,c = np.random.randint(low=1,high=25,size=2)
            matrix = np.random.randint(low=-10,high=10,size=(r,c))
            self.assertEqual(shape(matrix.tolist()),(r,c))


    def test_matxRound(self):

        for decpts in range(10):
            r,c = np.random.randint(low=1,high=25,size=2)
            matrix = np.random.random((r,c))

            mat = matrix.tolist()
            dec_true = [[Decimal(str(round(num,decpts))) for num in row] for row in mat]

            matxRound(mat,decpts)
            dec_test = [[Decimal(str(num)) for num in row] for row in mat]

            res = Decimal('0')
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    res += dec_test[i][j].compare_total(dec_true[i][j])

            self.assertEqual(res,Decimal('0'))


    def test_transpose(self):
        for _ in range(10):
            r,c = np.random.randint(low=1,high=25,size=2)
            matrix = np.random.random((r,c))

            mat = matrix.tolist()
            t = np.array(transpose(mat))

            self.assertEqual(t.shape,(c,r))
            self.assertTrue((matrix.T == t).all())


    def test_matxMultiply(self):

        for _ in range(10):
            r,d,c = np.random.randint(low=1,high=25,size=3)
            mat1 = np.random.randint(low=-10,high=10,size=(r,d)) 
            mat2 = np.random.randint(low=-5,high=5,size=(d,c)) 
            dotProduct = np.dot(mat1,mat2)

            dp = np.array(matxMultiply(mat1,mat2))

            self.assertTrue((dotProduct == dp).all())


    def test_augmentMatrix(self):

        for _ in range(10):
            r,c = np.random.randint(low=1,high=25,size=2)
            A = np.random.randint(low=-10,high=10,size=(r,c))
            b = np.random.randint(low=-10,high=10,size=(r,1))

            Ab = np.array(augmentMatrix(A.tolist(),b.tolist()))
            ab = np.hstack((A,b))

            self.assertTrue((Ab == ab).all())

    def test_swapRows(self):
        for _ in range(10):
            r,c = np.random.randint(low=1,high=25,size=2)
            matrix = np.random.random((r,c))

            mat = matrix.tolist()

            r1, r2 = np.random.randint(0,r, size = 2)
            swapRows(mat,r1,r2)

            matrix[[r1,r2]] = matrix[[r2,r1]]

            self.assertTrue((matrix == np.array(mat)).all())

    def test_scaleRow(self):

        for _ in range(10):
            r,c = np.random.randint(low=1,high=25,size=2)
            matrix = np.random.random((r,c))

            mat = matrix.tolist()

            rr = np.random.randint(0,r)
            with self.assertRaises(ValueError):
                scaleRow(mat,rr,0)

            scale = np.random.randint(low=1,high=10)
            scaleRow(mat,rr,scale)
            matrix[rr] *= scale

            self.assertTrue((matrix == np.array(mat)).all())
    
    def test_addScaleRow(self):

        for _ in range(10):
            r,c = np.random.randint(low=1,high=25,size=2)
            matrix = np.random.random((r,c))

            mat = matrix.tolist()

            r1,r2 = np.random.randint(0,r,size=2)

            scale = np.random.randint(low=1,high=10)
            addScaledRow(mat,r1,r2,scale)
            matrix[r1] += scale * matrix[r2]

            self.assertTrue((matrix == np.array(mat)).all())


    def test_gj_Solve(self):

        for _ in range(10):
            r = np.random.randint(low=3,high=10)
            A = np.random.randint(low=-10,high=10,size=(r,r))
            b = np.arange(r).reshape((r,1))

            x = gj_Solve(A.tolist(),b.tolist())
            if np.linalg.matrix_rank(A) < r:
                self.assertEqual(x,None)
            else:
                Ax = np.dot(A,np.array(x))
                loss = np.mean((Ax - b)**2)
                # print Ax
                # print loss
                self.assertTrue(loss<0.1)


suite = unittest.TestLoader().loadTestsFromTestCase(LinearRegressionTestCase)
unittest.TextTestRunner(verbosity=3).run(suite)

