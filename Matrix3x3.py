#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Matrix3x3.py
The class Matrix3x3.
"""

#from Point3D
import Point3D # in Python ,opposite of C++ ,import from Vector containing Point are not seen from Matrix
#from Vector3D
import Vector3D

from Overload import * #Overload_by_class


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

        self.m = [[0,0,0],
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
        
        self.m = [[v1.x,v1.y,v1.z],
                  [v2.x,v2.y,v2.z],
                  [v3.x,v3.y,v3.z]]

        if __debug__:
            print("# Matrix3x3 constructor #")
         

    # m  : multiplicand ,matrix,....
    def __mul__(self, m): #  self is at LEFT of multiplication operand : self * m = Matrix * m

        if __debug__:
            print("Matrix3x3.py : __mul__")

        m00 = self.m[0][0]
        m01 = self.m[0][1]
        m02 = self.m[0][2]

        m10 = self.m[1][0]
        m11 = self.m[1][1]
        m12 = self.m[1][2]

        m20 = self.m[2][0]
        m21 = self.m[2][1]
        m22 = self.m[2][2]
            
        # this creates operator overload
        # another solution would be to use decorator overloading
        if isinstance(m,Point3D) or isinstance(m,Vector3D): # matrix multiplication

            x = m.x
            y = m.y
            z = m.z

            object_type = type(m)
            
            return object_type(m00 * x + m01 * y + m02 * z,
                               m10 * x + m11 * y + m12 * z,
                               m20 * x + m21 * y + m22 * z)

        elif isinstance(m,tuple) and len(m) == 3: 

            (x,y,z) = m

            return (m00 * x + m01 * y + m02 * z,
                    m10 * x + m11 * y + m12 * z,
                    m20 * x + m21 * y + m22 * z)
            
        else: # number multiplication

            print("Matrix3x3 multiplication not yet implemented")
            
            # return Point3D(self.x * m,
            #                self.y * m,
            #                self.z * m)
        
            #return self * m # self is at LEFT of operand *
    
