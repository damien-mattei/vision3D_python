#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vector3D.py
Vector3D class.
"""

#from __future__ import annotations

import math


from Point3D import Point3D


from multimethod import multimethod

#from Overload_by_class import Overload_by_class

from typing import Union

Numeric = Union[float, int]


# >>> v1=Vector3D(1.1,2.2,3.3)

# Vector3D constructor #
#class Vector3D(object):
class Vector3D:
    '''Construct an object Vector3D.'''


    # >> v2=Vector3D()
    # # Vector3D of float constructor #
    # >>> v2
    # Vector3D @ 0x7fee25c54790 [0.0,0.0,0.0]
    # >>> v1=Vector3D(1.1,2.2,3.3)
    # # Vector3D of Numeric constructor #
    # >>> v1
    # Vector3D @ 0x7fee25c47cd0 [1.1,2.2,3.3]
   

    @multimethod
    def __init__(self):


        if __debug__:
            print("# Vector3D of float constructor #")
            
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

        


    @multimethod
    def __init__(self,x : Numeric,y : Numeric,z : Numeric):

        if __debug__:
            print("# Vector3D of Numeric constructor #")

        self.x = x
        self.y = y
        self.z = z

       
            
    # create vector AB with points A and B
    
    #v=Vector3D(Point3D(1.0,1.0,1.0),Point3D(3.0,3.0,3.0))

    # Point3D constructor #
    # Point3D constructor #
    # Vector3D (Point3D,Point3D)constructor #
    #>>> v
    #Vector3D @ 0x7fee274d4fd0 [2.0,2.0,2.0]
    @multimethod
    def __init__(self,a : Point3D,b : Point3D):

        if __debug__:
            print("# Vector3D (Point3D,Point3D)constructor #")
      
        self.x = b.x - a.x
        self.y = b.y - a.y
        self.z = b.z - a.z

        

            
    #v=Vector3D((1,2,3),(4,5,6))

    # Vector3D (tuple,tuple) constructor #
    #>>> v
    #Vector3D @ 0x7fee2655ced0 [3,3,3]
    @multimethod
    def __init__(self,a : tuple,b : tuple):

        if __debug__:
            print("# Vector3D (tuple,tuple) constructor #")

        (ax,ay,az)=a
        (bx,by,bz)=b
        self.x = bx - ax
        self.y = by - ay
        self.z = bz - az

        
            
    # v1
    # Vector3D @ 0x7f7ded7869d0 [1,2.2,3.3]
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

    
    
 
    # >>> p1=Point3D(1.0,2.2,3.3)
    # # Point3D constructor #
    # >>> p2=Point3D(1.0,3.2,4.3)
    # # Point3D constructor #
    # >>> v1=Vector3D.set_with_points_backup(p1,p2)
    # OverloadByClass.py : Inside wrapped_function()
    # OverloadByClass : wrapped_function :  name = __init__
    # OverloadByClass : wrapped_function :  key = ('__init__', ('Vector3D', 'float', 'float', 'float'))
    # # Vector3D constructor #
    # >>> v1
    # Vector3D @ 0x7feed23f6b50 [0.0,1.0,1.0]
    # DEPRECATED
    @classmethod
    def set_with_points_backup(cls,a,b):

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
    

    # >>> p1=Point3D()
    # # Point3D constructor #
    # >>> p2=Point3D()
    # # Point3D constructor #
    # >>> v2=Vector3D(10.0,2.0,3.0)
    # OverloadByClass.py : Inside wrapped_function()
    # OverloadByClass : wrapped_function :  name = __init__
    # OverloadByClass : wrapped_function :  key = ('__init__', ('Vector3D', 'float', 'float', 'float'))
    # # Vector3D constructor #
    # >>> v=Vector3D(1.0,2.0,3.0)
    # OverloadByClass.py : Inside wrapped_function()
    # OverloadByClass : wrapped_function :  name = __init__
    # OverloadByClass : wrapped_function :  key = ('__init__', ('Vector3D', 'float', 'float', 'float'))
    # # Vector3D constructor #
    # >>> v.set_with_points(p1,p2)
    # >>> v
    # Vector3D @ 0x7f328e743450 [0.0,0.0,0.0]
    # >>> v=Vector3D(1.0,2.0,3.0)
    # OverloadByClass.py : Inside wrapped_function()
    # OverloadByClass : wrapped_function :  name = __init__
    # OverloadByClass : wrapped_function :  key = ('__init__', ('Vector3D', 'float', 'float', 'float'))
    # # Vector3D constructor #
    # >>> v
    # Vector3D @ 0x7f328e743b50 [1.0,2.0,3.0]
    # >>> v.set_with_points(p1,p2)
    # >>> v
    # Vector3D @ 0x7f328e743b50 [0.0,0.0,0.0]
    def set_with_points(self,a,b):

        ax = a.x
        ay = a.y
        az = a.z

        bx = b.x
        by = b.y
        bz = b.z

        self.x = bx - ax
        self.y = by - ay
        self.z = bz - az
        
    
    # overload + operator
    # >>> v1+v2
    # Vector3D constructor #
    #Vector3D @ 0x7f7dec6d3390 [2,0.0,6.3]
    
    def __add__(self,v):
        
        return Vector3D(self.x + v.x,
                        self.y + v.y,
                        self.z + v.z)


    
    # multiplications
    
    # >>> v1=Vector3D(1.1,2.2,3.3)
    # OverloadByClass.py : Inside wrapped_function()
    # OverloadByClass : wrapped_function :  name = __init__
    # OverloadByClass : wrapped_function :  key = ('__init__', ('Vector3D', 'float', 'float', 'float'))
    # # Vector3D constructor #
    # >>> v1*3.0
    # OverloadByClass.py : Inside wrapped_function()
    # OverloadByClass : wrapped_function :  name = __mul__
    # OverloadByClass : wrapped_function :  key = ('__mul__', ('Vector3D', 'float'))
    # Vector3D.py : __mul__ ('Vector3D', float)
    # OverloadByClass.py : Inside wrapped_function()
    # OverloadByClass : wrapped_function :  name = __init__
    # OverloadByClass : wrapped_function :  key = ('__init__', ('Vector3D', 'float', 'float', 'float'))
    # # Vector3D constructor #
    # Vector3D @ 0x7f2159337d50 [3.3000000000000003,6.6000000000000005,9.899999999999999]
    @multimethod
    def __mul__(self,m : Numeric): # self * m

        if __debug__:
            print("Vector3D.py : __mul__ (Vector3D, Numeric)")

        # number multiplication
        return Vector3D(self.x * m,
                        self.y * m,
                        self.z * m)

    # dot product - produit scalaire
    # >>> v1=Vector3D(1.1,2.2,3.3)
    # # Vector3D of Numeric constructor #
    # >>> v2=Vector3D(2.1,2.7,-3.3)
    # # Vector3D of Numeric constructor #
    # >>> v1*v2
    # Vector3D.py : __mul__(Vector3D, 'Vector3D')
    # -2.639999999999997
    @multimethod
    def __mul__(self,m : object): #"Vector3D"): # self * m

        if __debug__:
            print("Vector3D.py : __mul__(Vector3D, 'Vector3D')")

        # dot product - produit scalaire
        return self.x * m.x + self.y * m.y + self.z * m.z


    


        
    # right multiplication (non commutative)

    # >>> v1=Vector3D(1.1,2.2,3.3)
    # # Vector3D of Numeric constructor #
    # >>> m3d = [[1 , 2 , 3],[4 , 5, 6],[7, 8, 9]]
    # >>> m3d*v1
    # Vector3D.py : __rmul__(Vector3D , list)
    # # Vector3D of Numeric constructor #
    # Vector3D @ 0x7fee25c47cd0 [15.399999999999999,35.199999999999996,55.0]
    
    # m  : multiplicand ,list matrix,....
    
    @multimethod
    def __rmul__(self, m : list): #  self is at RIGHT of multiplication operand : m * self

        if __debug__:
            print("Vector3D.py : __rmul__(Vector3D , list)")

        x = self.x
        y = self.y
        z = self.z
            
        return Vector3D(m[0][0] * x + m[0][1] * y + m[0][2] * z,
                        m[1][0] * x + m[1][1] * y + m[1][2] * z,
                        m[2][0] * x + m[2][1] * y + m[2][2] * z)


    # >>> v1=Vector3D(1.1,2.2,3.3)
    # OverloadByClass.py : Inside wrapped_function()
    # OverloadByClass : wrapped_function :  name = __init__
    # OverloadByClass : wrapped_function :  key = ('__init__', ('Vector3D', 'float', 'float', 'float'))
    # Vector3D constructor #
    # >>> 2.0*v1
    # OverloadByClass.py : Inside wrapped_function()
    # OverloadByClass : wrapped_function :  name = __rmul__
    # OverloadByClass : wrapped_function :  key = ('__rmul__', ('Vector3D', 'float'))
    # Vector3D.py : __rmul__('Vector3D',float)
    # OverloadByClass.py : Inside wrapped_function()
    # OverloadByClass : wrapped_function :  name = __mul__
    # OverloadByClass : wrapped_function :  key = ('__mul__', ('Vector3D', 'float'))
    # Vector3D.py : __mul__ ('Vector3D', float)
    # OverloadByClass.py : Inside wrapped_function()
    # OverloadByClass : wrapped_function :  name = __init__
    # OverloadByClass : wrapped_function :  key = ('__init__', ('Vector3D', 'float', 'float', 'float'))
    # Vector3D constructor #
    # Vector3D @ 0x7f80060e0d10 [2.2,4.4,6.6]
    @multimethod
    def __rmul__(self, m : Numeric): #  self is at RIGHT of multiplication operand : m * self

        if __debug__:
            print("Vector3D.py : __rmul__(Vector3D,Numeric)")

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
    # WARNING: this is not XOR but CROSS PRODUCT
    # WARNING: cross product is not associative:
    # v1 ^ v2 ^ v3 = (v1 ^ v2) ^ v3 ≠ v1 ^ (v2 ^ v3)
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



