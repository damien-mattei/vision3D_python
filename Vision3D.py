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
from Matrix3x3 import Matrix3x3


import math



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

        self.univ = Universe()
            
        self.c = c
        self.s = s

        # compute vector w

        # create SC vector
        sc=Vector3D(c,s)

        d = sc.norm() # compute norm of SC

        
        # vectors defining screen frame       

        # vector w
        # normalize w
        w = sc / d

        # vector u
       
        # arbitrary taking negative solution for orientation
        u = Vector3D()
        u.x = 0
        u.y = - ( w.x / math.sqrt(w.x * w.x + w.y * w.y))
        u.z = - w.y * u.y / w.x

        # vector v
        v = w ^ u

        # change of basis matrix

        # cf. C++ version for comments
        # da1 = v.y * w.z - v.z * w.y
        # da2 = v.z * w.x - v.x * w.z
        # da3 = v.x * w.y - v.y * w.x
        
        da = v ^ w
        db = w ^ u
        dc = u ^ v

        # dot products - produits scalaires
        dau = u * da
        dbv = v * db
        dcw = w * dc

        daqu = da / dau
        dbqv = db / dbv
        dcqw = dc / dcw

        self.m3x3 = Matrix3x3(daqu,dbqv,dcqw)
        
    def __repr__(self):
        return 'Vision3D @ {} camera = {}  screen = {}'.format(hex(id(self)),self.c,self.s)

    def __str__(self):
        return 'Vision3D camera = {}  screen = {}'.format(self.c,self.s)
