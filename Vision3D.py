#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vision3D.py
La classe Vision3D de base avec son main pour l'execution.
"""
from __future__ import annotations

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

        #sc = Vector

        # vectors defining screen frame

        # vector u
        self.u = Vector3D()

        # vector v
        self.v = Vector3D()

        # vector w
        self.w = Vector3D()

        

    def __repr__(self):
        return 'Vision3D @ {} camera = {}  screen = {}'.format(hex(id(self)),self.c,self.s)

