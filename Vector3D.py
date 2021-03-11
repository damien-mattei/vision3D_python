#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vector3D.py
Vector3D class.
"""

#from __future__ import annotations

import math


from Point3D import Point3D



##>>> overload.area(3)
##9
##>>> overload.area(4,5)
##20
#from overloading import overload

from Overload import Overload_by_class,volume


# >>> v1=Vector3D(1.1,2.2,3.3)
# Inside wrapped_function()
#   name = __init__
#   key = ('__init__', ('Vector3D', 'float', 'float', 'float'))

# Vector3D constructor #
#class Vector3D(object):
class Vector3D:
    '''Construct an object Vector3D.'''

    # v1=Vector3D(1.1,2.2,3.3)

    #v2=Vector3D() # does not work because before __init__ ?


    #v2=Vector3D()
    #Inside wrapped_function()
     #  name = __init__
    #   key = ('__init__', ('Vector3D',))
    # # Vector3D constructor #
    # >>> v2
    # Inside wrapped_function()
    #   name = __repr__
    #   key = ('__repr__', ('Vector3D',))
    # Vector3D @ 0x111d55e20 [0.0,0.0,0.0]
    @Overload_by_class('Vector3D')
    def __init__(self,x=0.0,y=0.0,z=0.0):

        self.x = x 
        self.y = y
        self.z = z

        if __debug__:
            print("# Vector3D constructor #")

            
    @Overload_by_class('Vector3D',float,float,float)
    def __init__(self,x=0.0,y=0.0,z=0.0):

        self.x = x 
        self.y = y
        self.z = z

        if __debug__:
            print("# Vector3D constructor #")
        
    #v=Vector3D(Point3D(1.0,1.0,1.0),Point3D(3.0,3.0,3.0))
    #     # Point3D constructor #
    # # Point3D constructor #
    # Inside wrapped_function()
    #   name = __init__
    #   key = ('__init__', ('Vector3D', 'Point3D', 'Point3D'))
    # # Vector3D constructor #
    # >>> v
    # Inside wrapped_function()
    #   name = __repr__
    #   key = ('__repr__', ('Vector3D',))
    # Vector3D @ 0x113aac910 [2.0,2.0,2.0]
    @Overload_by_class('Vector3D',Point3D,Point3D)
    def __init__(self,a=Point3D(),b=Point3D()):
        
        self.x = b.x - a.x
        self.y = b.y - a.y
        self.z = b.z - a.z

        if __debug__:
            print("# Vector3D constructor #")

    #v=Vector3D((1,2,3),(4,5,6))
    #   Overload.py : Inside wrapped_function()
    #   name = __init__
    #   key = ('__init__', ('Vector3D', 'tuple', 'tuple'))
    # # Vector3D constructor #
    # >>> v
    # Overload.py : Inside wrapped_function()
    #   name = __repr__
    #   key = ('__repr__', ('Vector3D',))
    # Vector3D @ 0x111100e20 [3,3,3]
    @Overload_by_class('Vector3D',tuple,tuple)
    def __init__(self,a,b):

        (ax,ay,az)=a
        (bx,by,bz)=b
        self.x = bx - ax
        self.y = by - ay
        self.z = bz - az

        if __debug__:
            print("# Vector3D constructor #")
            
    # v1
    # Vector3D @ 0x7f7ded7869d0 [1,2.2,3.3]

    @Overload_by_class('Vector3D')
    def __repr__(self):
        return 'Vector3D @ {} [{},{},{}]'.format(hex(id(self)),self.x,self.y,self.z)


    # print(v1)
    # [1,2.2,3.3]

    def __str__(self):
        return '[{},{},{}]'.format(self.x,self.y,self.z)


    #     >>> v1=Vector3D(1,2.2,3.3)
    #     # Vector3D constructor #
    # >>> v2=Vector3D(2,2.2,3.3)
    # # Vector3D constructor #
    # >>> v1bis=Vector3D(1,2.2,3.3)
    # # Vector3D constructor #
    # >>> v1 is v2
    # False
    # >>> v1 == v2
    # False
    # >>> v1 == v1bis
    # True
    # >>> v1 is v1bis
    # False
    
    #>>> v1=Vector3D(1,2.2,3.3)
    # Vector3D constructor #
    #>>> v1
    #Vector3D @ 0x104a058d0 [1,2.2,3.3]
    #>>> v2=v1
    #>>> v2
    #Vector3D @ 0x104a058d0 [1,2.2,3.3]
    #>>> v1 is v2
    #True
    #>>> v1 == v2
    #True
    def __eq__(self, other): 
        if not isinstance(other, Vector3D):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.x == other.x and self.y == other.y and self.z == other.z

    
    
    # >>> p1=Point3D(1,2.2,3.3)
    # # Point3D constructor #
    # >>> p2=Point3D(1,3.2,4.3)
    # # Point3D constructor #

    # v1=Vector3D.set_with_points(p1,p2)
    # >>> v1=Vector3D.set_with_points(p1,p2)
    # Vector3D constructor #
    # >>> v1
    # Vector3D @ 0x7f41e013bc10 [0,1.0,1.0]
    # >>> print(v1)
    # [0,1.0,1.0]
 
    @classmethod
    def set_with_points(cls,a,b):

        ax = a.x
        ay = a.y
        az = a.z

        bx = b.x
        by = b.y
        bz = b.z

        x = bx - ax
        y = by - ay
        z = bz - az

        return cls(x,y,z)
    
        
    # overload + operator
    # >>> v1+v2
    # Vector3D constructor #
    #Vector3D @ 0x7f7dec6d3390 [2,0.0,6.3]
    
    def __add__(self,v):
        
        return Vector3D(self.x + v.x,
                        self.y + v.y,
                        self.z + v.z)
    
    
    # overload * operator
    # >>> v1*3.2
    # Vector3D constructor #
    # Vector3D @ 0x7f4f019a0e50 [3.2,7.040000000000001,10.56]

    # dot product - produit scalaire
    # >>> v1=Vector3D(1,2.2,3.3)
    # # Vector3D constructor #
    # >>> v2=Vector3D(2,2.5,3.7)
    # # Vector3D constructor #
    # >>> v1*v2
    # Vector3D.py : __mul__
    # 19.71
    
    def __mul__(self,m): # self * m

        if __debug__:
            print("Vector3D.py : __mul__")

        # this creates operator overload
        if isinstance(m,Vector3D): # dot product - produit scalaire
            return self.x * m.x + self.y * m.y + self.z * m.z
        else:
            return Vector3D(self.x * m,
                            self.y * m,
                            self.z * m)
    

        
    
    # >>> 2.0*v1
    # Vector3D constructor #
    # Vector3D @ 0x7efdb8310e10 [2.0,4.4,6.6]
    # >>> 2*v1
    # Vector3D constructor #
    # Vector3D @ 0x7efdb8323910 [2,4.4,6.6]

    # m3d = [[1 , 2 , 3],[4 , 5, 6],[7, 8, 9]]
    # >>> m3d*v1
    # Vector3D.py : __rmul__
    # # Vector3D constructor #
    # Vector3D @ 0x7f08c9283710 [15.299999999999999,34.8,54.3]
    
    # m  : multiplicand ,matrix,....
    def __rmul__(self, m): #  self is at RIGHT of multiplication operand : m * self

        if __debug__:
            print("Vector3D.py : __rmul__")

        # this creates operator overload
        if isinstance(m,list): # matrix multiplication TODO: change list with a Matrix3X3 class

            x = self.x
            y = self.y
            z = self.z
            
            return Vector3D(m[0][0] * x + m[0][1] * y + m[0][2] * z,
                            m[1][0] * x + m[1][1] * y + m[1][2] * z,
                            m[2][0] * x + m[2][1] * y + m[2][2] * z)

        else: # number multiplication

            # return Vector3D(self.x * m,
            #                 self.y * m,
            #                 self.z * m)
        
            return self * m # self is at LEFT of operand *

        
    # overload / operator
    
    def __truediv__(self,d):
        
        x = self.x / d
        y = self.y / d
        z = self.z / d

        return Vector3D(x,y,z)
        

    # overload += operator

    # >>> v1=Vector3D(1,2.2,3.3)
    # # Vector3D constructor #
    # >>> v2=Vector3D(2,2.5,3.7)
    # # Vector3D constructor #
    # >>> v1+=v2
    # >>> v1
    # Vector3D @ 0x7fa71ff35490 [3,4.7,7.0]
    
    def __iadd__(self,v):
        
        self.x += v.x
        self.y += v.y
        self.z += v.z

        return self


    # cross product - produit vectoriel
    # operator syntax: v ^ v2
    # WARNING: this not XOR but CROSS PRODUCT
    def __xor__(self,v):

        x = self.x
        y = self.y
        z = self.z
        
        return Vector3D(y * v.z - z * v.y,
                        z * v.x - x * v.z,
		        x * v.y - y * v.x)

    # >>> v1.norm()
    # Vector3D.py : __mul__
    # 4.090232267243512
    def norm(self):

        return math.sqrt(self * self)



# code à enlever:

#@overload(int)
@Overload_by_class(int)
def area1(size):
    calc =  size * size
    print (calc)

@Overload_by_class(int)
def volume1(size):
    calc =  size * size *  size
    print (calc)

@Overload_by_class(int,int,int)
def volume1(length, breadth,depth):
    calc =  length * breadth *  depth
    print (calc)
