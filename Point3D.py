#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Point3D.py
La classe Point3D.
"""

class Point3D:
    '''Construit un objet Point3D.'''

    # p1=Point3D(1,2.2,3.3)

    def __init__(self,x=0,y=0,z=0):
        
        self.x = x
        self.y = y
        self.z = z

        if __debug__:
            print("# Point3D constructor #")

            
    # p1
    # Point3D @ 0x7fbe64853850 (1,2.2,3.3)

    def __repr__(self):
        return 'Point3D @ {} ({},{},{})'.format(hex(id(self)),self.x,self.y,self.z)

    # print(p1)
    # (1,2.2,3.3)

    def __str__(self):
        return '({},{},{})'.format(self.x,self.y,self.z)
   
        
