#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Matrix3x3.py
The class Matrix3x3.
"""

from Point3D import Point3D # in Python ,opposite of C++ ,import from Vector containing Point are not seen from Matrix
from Vector3D import Vector3D

from OverloadByClass import * #Overload_by_class


# >>> m1=Matrix3x3()
# Overload.py : Inside wrapped_function()
#   name = __init__
#   key = ('__init__', ('Matrix3x3',))
# # Matrix3x3 constructor #
# >>> m1
# <Matrix3x3.Matrix3x3 object at 0x10f5543d0>
# >>> p1=Point3D(1,2.2,3.3)
# # Point3D constructor #
# >>> p1
# Point3D @ 0x10f5de750 (1,2.2,3.3)
# >>> res=m1*p1
# Matrix3x3.py : __mul__
# # Point3D constructor #
# >>> res
# Point3D @ 0x108fcb810 (0.0,0.0,0.0)

class Matrix3x3:
    '''Construct an object Matrix3x3.'''

    
    @Overload_by_class('Matrix3x3')
    def __init__(self):

        self.M = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]

        if __debug__:
            print("# Matrix3x3 constructor #")


    @Overload_by_class('Matrix3x3',Vector3D,Vector3D,Vector3D)
    def __init__(self,v1,v2,v3):

        print("Matrix3x3.py : __init__('Matrix3x3',Vector3D,Vector3D,Vector3D)")
        
        if __debug__:
            print("Matrix3x3.py : __init__('Matrix3x3',Vector3D,Vector3D,Vector3D) : v1.x=")
            print(v1.x)
            print("Matrix3x3.py : __init__('Matrix3x3',Vector3D,Vector3D,Vector3D) : v2.x=")
            print(v2.x)
            print("Matrix3x3.py : __init__('Matrix3x3',Vector3D,Vector3D,Vector3D) : v2.y=")
            print(v2.y)
            print("Matrix3x3.py : __init__('Matrix3x3',Vector3D,Vector3D,Vector3D) : v2.z=")
            print(v2.z)
        
        self.M = [[v1.x,v1.y,v1.z],
                  [v2.x,v2.y,v2.z],
                  [v3.x,v3.y,v3.z]]

        if __debug__:
            print("# Matrix3x3 constructor #")

            
    @Overload_by_class('Matrix3x3',
                       float,float,float,
                       float,float,float,
                       float,float,float)
    def __init__(self,
                 M00,M01,M02,
                 M10,M11,M12,
                 M20,M21,M22):

        print("Matrix3x3.py : __init__('Matrix3x3',float,float,float,float,float,float,float,float,float)")

        self.M[0][0] = M00
        self.M[0][1] = M01
        self.M[0][2] = M02
        
        self.M[1][0] = M10
        self.M[1][1] = M11
        self.M[1][2] = M12
        
        self.M[2][0] = M20
        self.M[2][1] = M21
        self.M[2][2] = M22


    # >>> Matrix3x3.checkSquare3x3Matrix(vis.m3x3.M)
    # True
    def checkSquare3x3Matrix(M):

        return len(M) == 3 and len(M[0]) == 3 and len(M[1]) == 3 and len(M[2]) == 3

    
    @Overload_by_class('Matrix3x3',list)
    def __init__(self,R):

        if checkSquare3x3Matrix(R):

            self.M = R

        else:

            raise ValueError("Matrix3x3.py : __init__('Matrix3x3',list) : R has not a size of 3x3.')")

        
          
    # >>> vis=Vision3D((1,2,3),(4,5,6))
    # >>> vis.m3x3
    # Matrix3D @ 0x7f97ec959690 
    # [[0.0,-0.7071067811865476,0.7071067811865476]
    #  [0.8164965809277261,-0.4082482904638631,-0.4082482904638631]
    #  [0.5773502691896258,0.5773502691896258,0.5773502691896258]]
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

    # [[0.0,-0.7071067811865476,0.7071067811865476]
    #  [0.8164965809277261,-0.4082482904638631,-0.4082482904638631]
    #  [0.5773502691896258,0.5773502691896258,0.5773502691896258]]
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

    
    # R  : multiplicand ,vector,point,matrix,....
    # DEPRECATED
    def backup__mul__(self, R): #  self is at LEFT of multiplication operand : self * R = Matrix * R, R is at Right

        if __debug__:
            print("Matrix3x3.py : __mul__")

        M00 = self.M[0][0]
        M01 = self.M[0][1]
        M02 = self.M[0][2]

        M10 = self.M[1][0]
        M11 = self.M[1][1]
        M12 = self.M[1][2]

        M20 = self.M[2][0]
        M21 = self.M[2][1]
        M22 = self.M[2][2]
            
        # this creates operator overload
        # another solution would be to use decorator overloading
        if isinstance(R,Point3D) or isinstance(R,Vector3D): # matrix multiplication

            x = R.x
            y = R.y
            z = R.z

            object_type = type(R)
            
            return object_type(M00 * x + M01 * y + M02 * z,
                               M10 * x + M11 * y + M12 * z,
                               M20 * x + M21 * y + M22 * z)

        elif isinstance(R,tuple) and len(R) == 3: 

            (x,y,z) = R

            return (M00 * x + M01 * y + M02 * z,
                    M10 * x + M11 * y + M12 * z,
                    M20 * x + M21 * y + M22 * z)
            
        else: # Multiplication

            print("Matrix3x3 multiplication not yet implemented")
            
            

    
    # R  : multiplicand (Vector3D)
    @Overload_by_class('Matrix3x3',Vector3D)
    def __mul__(self, R): #  self is at LEFT of multiplication operand : self * R = Matrix * R, R is at Right

        if __debug__:
            print("Matrix3x3.py : __mul__('Matrix3x3',Vector3D)")

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
    @Overload_by_class('Matrix3x3',Point3D)
    def __mul__(self, R): #  self is at LEFT of multiplication operand : self * R = Matrix * R, R is at Right

        if __debug__:
            print("Matrix3x3.py : __mul__('Matrix3x3',Point3D)")

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
    @Overload_by_class('Matrix3x3',tuple)
    def __mul__(self, R): #  self is at LEFT of multiplication operand : self * R = Matrix * R, R is at Right

        if __debug__:
            print("Matrix3x3.py : __mul__('Matrix3x3',tuple)")

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

            raise ValueError("Matrix3x3.py : __mul__('Matrix3x3',tuple) : tuple R has not a size of 3.')")

        (x,y,z) = R

        return (M00 * x + M01 * y + M02 * z,
                M10 * x + M11 * y + M12 * z,
                M20 * x + M21 * y + M22 * z)
            

    
    # R  : multiplicand
    # square 3x3 matrix multiplication
    # Warning: to be numerically verified ! test TO-DO !
    @Overload_by_class('Matrix3x3','Matrix3x3')
    def __mul__(self, R): #  self is at LEFT of multiplication operand : self * R = Matrix * R, R is at Right

        if __debug__:
            print("Matrix3x3.py : __mul__('Matrix3x3','Matrix3x3')")

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

            ((R00,R01,R02),
             (R10,R11,R12),
             (R20,R21,R22)) = R.M
            
            return Matrix3x3(M00 * R00 + M01 * R10 + M02 * R20,M00 * R01 + M01 * R11 + M02 * R21,M00 * R02 + M01 * R12 + M02 * R22,
                             M10 * R00 + M11 * R10 + M12 * R20,M10 * R01 + M11 * R11 + M12 * R21,M10 * R02 + M11 * R12 + M12 * R22,
                             M20 * R00 + M21 * R10 + M22 * R20,M20 * R01 + M21 * R11 + M22 * R21,M20 * R02 + M21 * R12 + M22 * R22)
            

        else:

            raise ValueError("Matrix3x3.py : __init__('Matrix3x3',list) : R has not a size of 3x3.')")


        
