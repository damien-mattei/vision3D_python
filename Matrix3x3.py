#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Matrix3x3.py
The class Matrix3x3.
"""

from Vector3D import Vector3D
from Overload import Overload_by_class

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
         
