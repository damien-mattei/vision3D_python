#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Universe.py
The Universe class.
"""



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
        self.point3DList = []

        #if __debug__:
        print("# Universe constructor #")
        
    # create a point by checking if it already exist in the universe
    # DEPRECATED
    def createPoint3D(x,y,z):

        p3d = Point3D(x,y,z)

        return p3d


    def createTuple3(self,x,y,z):

        p3d = (x,y,z)

        search = next((p for p in self.tuple3list if p == p3d), None)

        if search is None:
            
            self.tuple3list.append(p3d)
            return p3d

        else:
            return search

        
        
