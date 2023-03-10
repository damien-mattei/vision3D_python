#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Matrix3x3.py
The class Matrix3x3.
"""

from Point3D import Point3D # in Python ,opposite of C++ ,import from Vector containing Point are not seen from Matrix

#from Vector3DMultipleDispatchVersion import Vector3D
from Vector3D import Vector3D

from multimethod import multimethod # install : pip install multimethod==1.9.1

from typing import Union,Callable

from collections.abc import Iterable


Numeric = Union[float, int]


class MatError(Exception):     # juste pour la lisibilité des exceptions
    pass


# this is "like" a type definition to avoid error of undefined type during definition of the final Class
# ,it is an "Abstract" class that will be overwritten by the final one but used
# to pre-define the type Matrix3x3 and use it in the latter definition of Matrix3x3 itself.
# class Matrix3x3:
#     pass


# >>> m1=Matrix3x3()

# >>> m3=Matrix3x3(1,2,3.7,4,5,6,7,8,9)
# Matrix3x3.py : __init__(Matrix3x3,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric)
# # Matrix3x3 constructor #
# >>> m3*2.2
# Matrix3x3.py : __mul__(Matrix3x3,Numeric)
# Matrix3x3.py : __rmul__(Matrix3x3,Numeric)
# Matrix3x3.py : __init__(Matrix3x3,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric)
# # Matrix3x3 constructor #
# Matrix3D @ 0x7f63fbcb3190 
# [[2.2,4.4,8.14]
#  [8.8,11.0,13.200000000000001]
#  [15.400000000000002,17.6,19.8]]
# >>> m3*2
# Matrix3x3.py : __mul__(Matrix3x3,Numeric)
# Matrix3x3.py : __rmul__(Matrix3x3,Numeric)
# Matrix3x3.py : __init__(Matrix3x3,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric)
# # Matrix3x3 constructor #
# Matrix3D @ 0x7f63fb046fd0 
# [[2,4,7.4]
#  [8,10,12]
#  [14,16,18]]
class Matrix3x3():
    '''Construct an object Matrix3x3.'''

    
    @multimethod
    def __init__(self):

        self.M = [[0.0,0.0,0.0],
                  [0.0,0.0,0.0],
                  [0.0,0.0,0.0]]

        if __debug__:
            print("# Matrix3x3 constructor #")


    @multimethod
    def __init__(self,f : Callable):

        if __debug__:
            print("# Matrix constructor Matrix (function) #")

        self.M = [[f(i,j) for j in range(3)] for i in range(3)]

    @multimethod
    def __init__(self,v1 : Vector3D,v2 : Vector3D,v3 : Vector3D):

        print("Matrix3x3.py : __init__(Matrix3x3,Vector3D,Vector3D,Vector3D)")
        
        if __debug__:
            print("Matrix3x3.py : __init__(Matrix3x3,Vector3D,Vector3D,Vector3D) : v1.x=")
            print(v1.x)
            print("Matrix3x3.py : __init__(Matrix3x3,Vector3D,Vector3D,Vector3D) : v2.x=")
            print(v2.x)
            print("Matrix3x3.py : __init__(Matrix3x3,Vector3D,Vector3D,Vector3D) : v2.y=")
            print(v2.y)
            print("Matrix3x3.py : __init__(Matrix3x3,Vector3D,Vector3D,Vector3D) : v2.z=")
            print(v2.z)
        
        self.M = [[v1.x,v1.y,v1.z],
                  [v2.x,v2.y,v2.z],
                  [v3.x,v3.y,v3.z]]

        if __debug__:
            print("# Matrix3x3 constructor #")



    # >>> m3=Matrix3x3(1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0)  
    @multimethod
    def __init__(self,
                 M00 : Numeric, M01 : Numeric, M02 : Numeric,
                 M10 : Numeric, M11 : Numeric, M12 : Numeric,
                 M20 : Numeric, M21 : Numeric, M22 : Numeric):

        print("Matrix3x3.py : __init__(Matrix3x3,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric)")

        self.__init__()

        self.M[0][0] = M00
        self.M[0][1] = M01
        self.M[0][2] = M02
        
        self.M[1][0] = M10
        self.M[1][1] = M11
        self.M[1][2] = M12
        
        self.M[2][0] = M20
        self.M[2][1] = M21
        self.M[2][2] = M22


   
    
    @multimethod
    def __init__(self,R : list):

        if checkSquare3x3Matrix(R):

            self.M = R

        else:

            raise ValueError("Matrix3x3.py : __init__(Matrix3x3,list) : R has not a size of 3x3.')")

        
    def dim(self):
        '''Retourne le format de la matrice courante.'''
        n = len(self.M)
        if n == 0:
            raise MatError('Matrice vide !')
        return (n,len(self.M[0]))

    
    # >>> vis=Vision3D((1,2,3),(4,5,6))
    # >>> vis.m3x3
    
    def __repr__(self):

        M00 = self.M[0][0]
        M01 = self.M[0][1]
        M02 = self.M[0][2]

        M10 = self.M[1][0]
        M11 = self.M[1][1]
        M12 = self.M[1][2]

        M20 = self.M[2][0]
        M21 = self.M[2][1]
        M22 = self.M[2][2]
            
        return 'Matrix3D @ {} \n[[{},{},{}]\n [{},{},{}]\n [{},{},{}]]'.format(hex(id(self)),
                                                                               M00,M01,M02,
                                                                               M10,M11,M12,
                                                                               M20,M21,M22)


    # >>> print(vis.m3x3)

    
    def __str__(self):

        M00 = self.M[0][0]
        M01 = self.M[0][1]
        M02 = self.M[0][2]

        M10 = self.M[1][0]
        M11 = self.M[1][1]
        M12 = self.M[1][2]

        M20 = self.M[2][0]
        M21 = self.M[2][1]
        M22 = self.M[2][2]
            
        return '\n[[{},{},{}]\n [{},{},{}]\n [{},{},{}]]'.format(M00,M01,M02,
                                                                 M10,M11,M12,
                                                                 M20,M21,M22)


    # >>> m3=Matrix3x3(1,2,3.7,4,5,6,7,8,9)
    # Matrix3x3.py : __init__(Matrix3x3,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric)
    # # Matrix3x3 constructor #
    # >>> m3[1]
    # [4, 5, 6]
    # >>> m3[1][2]
    # 6
    # >>> m3
    # Matrix3D @ 0x7fa2467be750 
    # [[1,2,3.7]
    #  [4,5,6]
    #  [7,8,9]]
    def __getitem__(self,i):        # pour pouvoir écrire m[i] pour la ligne i
        return self.M[i]            # et m[i][j] pour l'élément en ligne i et colonne j

    def lig(self,i):                # m.lig(i) <==> m[i]
        '''Retourne la ligne i >= 0 de la matrice sous forme de liste plate.'''
        return self.M[i]

    # >>> m3
    # Matrix3D @ 0x7fa2467be750 
    # [[1,2,3.7]
    #  [4,5,6]
    #  [7,8,9]]
    # >>> 
    # ======= RESTART: /home/mattei/Dropbox/git/vision3D_python/Vision3D.py =======
    # >>> m3=Matrix3x3(1,2,3.7,4,5,6,7,8,9)
    # Matrix3x3.py : __init__(Matrix3x3,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric)
    # # Matrix3x3 constructor #
    # >>> m3.col(2)
    # [3.7, 6, 9]
    def col(self,j):
        '''Retourne la colonne j >= 0 de la matrice sous forme de liste plate.'''
        (n,_) = self.dim()
        return [self.M[i][j] for i in range(n)]

    
    # >>> m3=Matrix3x3(1,2,3.7,4,5,6,7,8,9)
    # Matrix3x3.py : __init__(Matrix3x3,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric)
    # # Matrix3x3 constructor #
    # >>> m2=m3*2
    # Matrix3x3.py : __mul__(Matrix3x3,Numeric)
    # Matrix3x3.py : __rmul__(Matrix3x3,Numeric)
    # Matrix3x3.py : __init__(Matrix3x3,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric)
    # # Matrix3x3 constructor #
    # >>> m2+m3
    # # Matrix constructor Matrix (function) #
    # Matrix3D @ 0x7f056ee18fd0 
    # [[3,6,11.100000000000001]
    #  [12,15,18]
    #  [21,24,27]]
    def __add__(self,m2):
        '''Retourne la somme de la matrice courante et d'une matrice m2
        de même format.'''
        (n,p) = self.dim()
        if m2.dim() != (n,p):
            raise MatError('mat_sum : Mauvais formats de matrices !')
        L = self.M ; L2 = m2.M
        return Matrix3x3(lambda i,j : L[i][j] + L2[i][j])

    
    
    # R  : multiplicand (Vector3D)
    @multimethod
    def __mul__(self, R : Vector3D): #  self is at LEFT of multiplication operand : self * R = Matrix * R, R is at Right

        if __debug__:
            print("Matrix3x3.py : __mul__(Matrix3x3,Vector3D)")

        M00 = self.M[0][0]
        M01 = self.M[0][1]
        M02 = self.M[0][2]

        M10 = self.M[1][0]
        M11 = self.M[1][1]
        M12 = self.M[1][2]

        M20 = self.M[2][0]
        M21 = self.M[2][1]
        M22 = self.M[2][2]
            
        x = R.x
        y = R.y
        z = R.z

        object_type = type(R)
            
        return object_type(M00 * x + M01 * y + M02 * z,
                           M10 * x + M11 * y + M12 * z,
                           M20 * x + M21 * y + M22 * z)


    # R  : multiplicand (Point3D)
    @multimethod
    def __mul__(self, R : Point3D): #  self is at LEFT of multiplication operand : self * R = Matrix * R, R is at Right

        if __debug__:
            print("Matrix3x3.py : __mul__(Matrix3x3,Point3D)")

        M00 = self.M[0][0]
        M01 = self.M[0][1]
        M02 = self.M[0][2]

        M10 = self.M[1][0]
        M11 = self.M[1][1]
        M12 = self.M[1][2]

        M20 = self.M[2][0]
        M21 = self.M[2][1]
        M22 = self.M[2][2]
            
        x = R.x
        y = R.y
        z = R.z

        object_type = type(R)
            
        return object_type(M00 * x + M01 * y + M02 * z,
                           M10 * x + M11 * y + M12 * z,
                           M20 * x + M21 * y + M22 * z)


    # R  : multiplicand
    # m2=Matrix3x3(3.0,2.0,3.0,4.0,4.0,6.0,7.0,8.0,9.0)
    # Matrix3x3.py : __init__(Matrix3x3,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric)
    # # Matrix3x3 constructor #
    # m2*(-1,-2,-3)
    # Matrix3x3.py : __mul__(Matrix3x3,tuple)
    # (-16.0, -30.0, -50.0)
    # m2*[-1,-2,-3]
    # Matrix3x3.py : __mul__(Matrix3x3,tuple)
    # (-16.0, -30.0, -50.0)
    @multimethod
    def __mul__(self, R : Iterable): # tuple): #  self is at LEFT of multiplication operand : self * R = Matrix * R, R is at Right

        if __debug__:
            print("Matrix3x3.py : __mul__(Matrix3x3,Iterable)")

        M00 = self.M[0][0]
        M01 = self.M[0][1]
        M02 = self.M[0][2]

        M10 = self.M[1][0]
        M11 = self.M[1][1]
        M12 = self.M[1][2]

        M20 = self.M[2][0]
        M21 = self.M[2][1]
        M22 = self.M[2][2]


        if len(R) != 3:

            raise ValueError("Matrix3x3.py : __mul__(Matrix3x3,Iterable) : Iterable R has not a size of 3.')")

        (x,y,z) = R

        return (M00 * x + M01 * y + M02 * z,
                M10 * x + M11 * y + M12 * z,
                M20 * x + M21 * y + M22 * z)
            

    
    # R  : multiplicand
    # square 3x3 matrix multiplication
    # >>> m2=m3*2
    # Matrix3x3.py : __mul__(Matrix3x3,Numeric)
    # Matrix3x3.py : __rmul__(Matrix3x3,Numeric)
    # Matrix3x3.py : __init__(Matrix3x3,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric)
    # # Matrix3x3 constructor #
    # >>> m2*m3
    # Matrix3x3.py : __mul__(Matrix3x3,Matrix3x3)
    # Matrix3x3.py : __init__(Matrix3x3,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric,Numeric)
    # # Matrix3x3 constructor #
    # Matrix3D @ 0x7f63f9b47210 
    # [[69.80000000000001,83.2,98.0]
    #  [132,162,197.6]
    #  [204,252,309.8]]
    @multimethod
    def __mul__(self, R : object): # "Matrix3x3"):  #  self is at LEFT of multiplication operand : self * R = Matrix * R, R is at Right
        # object instead of "Matrix3x3"

        if __debug__:
            print("Matrix3x3.py : __mul__(Matrix3x3,Matrix3x3)")

        # M00 = self.M[0][0]
        # M01 = self.M[0][1]
        # M02 = self.M[0][2]

        # M10 = self.M[1][0]
        # M11 = self.M[1][1]
        # M12 = self.M[1][2]

        # M20 = self.M[2][0]
        # M21 = self.M[2][1]
        # M22 = self.M[2][2]


        ((M00,M01,M02),
         (M10,M11,M12),
         (M20,M21,M22)) = self.M
        

        if checkSquare3x3Matrix(R.M):
        #if R.checkSquare3x3Matrix():

            ((R00,R01,R02),
             (R10,R11,R12),
             (R20,R21,R22)) = R.M
            
            return Matrix3x3(M00 * R00 + M01 * R10 + M02 * R20,M00 * R01 + M01 * R11 + M02 * R21,M00 * R02 + M01 * R12 + M02 * R22,
                             M10 * R00 + M11 * R10 + M12 * R20,M10 * R01 + M11 * R11 + M12 * R21,M10 * R02 + M11 * R12 + M12 * R22,
                             M20 * R00 + M21 * R10 + M22 * R20,M20 * R01 + M21 * R11 + M22 * R21,M20 * R02 + M21 * R12 + M22 * R22)
            

        else:

            raise ValueError("Matrix3x3.py : __init__(Matrix3x3,list) : R has not a size of 3x3.')")



    # R  : multiplicand
    # square 3x3 matrix multiplication by number
    #     >>> m3=Matrix3x3(1,2,3,4,5,6,7,8,9)
    
    @multimethod
    def __rmul__(self, m : Numeric): #  self is at RIGHT of multiplication operand : m * self

        if __debug__:
            print("Matrix3x3.py : __rmul__(Matrix3x3,Numeric)")

        ((M00,M01,M02),
         (M10,M11,M12),
         (M20,M21,M22)) = self.M
        
        return Matrix3x3(m*M00,m*M01,m*M02,
                         m*M10,m*M11,m*M12,
                         m*M20,m*M21,m*M22)
            



    # >>> m3=Matrix3x3(1,2,3,4,5,6,7,8,9)
    
    def __neg__(self):

        if __debug__:
            print("Matrix3x3.py : __neg__")

        return -1 * self


    # R  : multiplicand

    # >>> m3*2
    

    @multimethod
    def __mul__(self, R : Numeric): #  self is at LEFT of multiplication operand : self * R = Matrix * R, R is at Right

        if __debug__:
            print("Matrix3x3.py : __mul__(Matrix3x3,Numeric)")

        return R * self # matrix multiplication by a number is commutative self * R =  R * self 


    # now it also works with mixed types (int and float in the matrix):
    
    # >>> m3=Matrix3x3(1,2,3.7,4,5,6,7,8,9)
   




    
# >>> m3.__class__.__bases__
# (<class 'Matrix3x3.Matrix3x3Abstract'>,)
   
# >>> Matrix3x3.checkSquare3x3Matrix(vis.m3x3.M)
# True
def checkSquare3x3Matrix(M): # strange why this function does not need a self to be called later in class ?!
    
    return len(M) == 3 and len(M[0]) == 3 and len(M[1]) == 3 and len(M[2]) == 3

