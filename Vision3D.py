#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vision3D.py
La classe Vision3D de base avec son main pour l'execution.
"""
#from __future__ import annotations

from Point3D import Point3D
from Vector3D import Vector3D
from Universe import Universe




# >>> vis=Vision3D((1,2,3),(4,5,6))
# # Vision3D constructor #
# # Vector3D constructor #
# # Vector3D constructor #
# # Vector3D constructor #
# >>> vis
# Vision3D @ 0x10de39dd0 camera = (1, 2, 3)  screen = (4, 5, 6)
class Vision3D:
    '''Construit un objet Vision3D.'''

    # c position of eye or camera ,s position of center of screen
    def __init__(self,c=(0,0,0),s=(0,0,0)):

        if __debug__:
            print("# Vision3D constructor #")
            
        self.c = c
        self.s = s

        # compute vector w

        # create SC vector
        sc=Vector3D(c,s)

        d = sc.norm() # compute norm of SC

        
        # vectors defining screen frame       

        # vector w
        # normalize w
        w = Vector3D(sc / d)

        # vector u
        # WARNING seems python does not see as in C++ that u.y is perheaps not initialized
        # arbitrary taking negative solution for orientation
        u = Vector3D(0,- ( w.x / sqrt(w.x * w.x + w.y * w.y)), - w.y * u.y / w.x)

        # vector v
        v = Vector3D(w ^ u)

        # change of basis matrix

        # cf. C++ version for comments
        # da1 = v.y * w.z - v.z * w.y
        # da2 = v.z * w.x - v.x * w.z
        # da3 = v.x * w.y - v.y * w.x
        
        da = Vector3D(v ^ w)
        db = Vector3D(w ^ u)
        dc = Vector3D(u ^ v)
        
    def __repr__(self):
        return 'Vision3D @ {} camera = {}  screen = {}'.format(hex(id(self)),self.c,self.s)

