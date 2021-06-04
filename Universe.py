#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Universe.py
The Universe class.
"""

#from Point3D
import Point3D


# >>> u=Universe()
# # Universe constructor #
# >>> u
# <Universe.Universe object at 0x7fd66c551e90>


# >> p1=u.createTuple3(1.0,2.2,3.3)
# >>> p1
# (1.0, 2.2, 3.3)
# >>> p2=u.createTuple3(2.0,2.2,3.3)
# >>> p1 is p2
# False
# >>> p1bis=u.createTuple3(1.0,2.2,3.3)
# >>> p1 is p1bis
# True


class Universe:
    '''Construct an object Universe.'''


    def __init__(self):
  
        self.tuple3list = []

        # DEPRECATED
        self.point3Dlist = []

        #if __debug__:
        print("# Universe constructor #")
        
    # create a point by checking if it already exist in the universe
    # DEPRECATED
    #    >>> u.createPoint3D(1,2,3)
    # # Point3D constructor #
    # Point3D @ 0x7f6874ec7cd0 (1,2,3)
    # >>> u.createPoint3D(2,2,3)
    # # Point3D constructor #
    # Point3D @ 0x7f6874e7a590 (2,2,3)
    # >>> p2=u.createPoint3D(1,2,3)
    # # Point3D constructor #
    # >>> p2
    # Point3D @ 0x7f6874ec7cd0 (1,2,3)
    def createPoint3D(self,x,y,z):

        p3d = Point3D(x,y,z)

        search = next((p for p in self.point3Dlist if p == p3d), None)

        if search is None:
            
            self.point3Dlist.append(p3d)
            return p3d

        else:
            return search
        

    # Point 3D will be tuple 3
    def createTuple3(self,x,y,z):

        p3d = (x,y,z)

        search = next((p for p in self.tuple3list if p == p3d), None)

        if search is None:
            
            self.tuple3list.append(p3d)
            return p3d

        else:
            return search

        
        
