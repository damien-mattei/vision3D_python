#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vision3D.py
La classe Vision3D de base avec son main pour l'execution.
"""
#from __future__ import annotations

from Point3D import Point3D
#from Vector3DMultipleDispatchVersion import Vector3D
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

        # data
        self.univ = Universe()

        #  dico Points3D <-> Pixel
        self.dicoPointPixel = {}
            
        self.c = c
        self.s = s

        # pixel expressed in unit of frame reference 
        self.pixelInUnit = 1

        # pixels half-size of screen on Y
        self.winHalfSizeY = 192

        # pixels half-size of screen on X
        self.winHalfSizeX = 280

        # compute vector w

        # create SC vector
        sc=Vector3D(c,s)

        self.d = sc.norm() # compute norm of SC

        
        # vectors defining screen frame       

        # vector w
        # normalize w
        w = sc / self.d

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

    
    # >>> vis.projection((2.7,3.2,3.7))
    # Matrix3x3.py : __mul__
    # (-0.2963092430786103, -0.17107422125480973) 
    def projection(self,p):

        pPrim = self.m3x3 * p

        (x,y,z) = pPrim
        
        r = self.d / (self.d + z)

        return (  y * r,- x * r )

    
    def convert2Pixel(self,p):

        (x,y,z) = p

        return (int(x * self.pixelInUnit), int(y * self.pixelInUnit))


    def convert2AbsPixel(self,p):

        (x,y) = p

        return (x * self.winHalfSizeX, y * self.winHalfSizeY)

    
    def convert2ScreenCoord(self,p):

        (x,y) = p

        return ( x , 2 * winHalfSizeY - y )

    
    def projectPoint3DtoPixel(self,p):

        return convert2ScreenCoord(
                     convert2AbsPixel(
					      convert2Pixel(
							    projection(p))))


    #  associate Point3D and Pixels in dictionary (Point3D <-> Pixel)
    #     >>> vis.associatePt3Pix2InDico()
    # >>> vis.dicoPointPixel
    # {}
    def associatePt3Pix2InDico(self):

        # finding the vertex list
        vertexList = self.univ.tuple3list

        # iterate on the list to compute 3D to 2D projection and Pixels calculus
        for P3D in vertexList:

            pt2 = projectPoint3DtoPixel(P3D)
            dicoPointPixel[P3D] = pt2
