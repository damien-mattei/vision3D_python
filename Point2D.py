#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Point2D.py
La classe Point2D.
"""

class Point2D:
    '''Construit un objet Point2D.'''

    # p1=Point2D(1,2.2)

    def __init__(self,x,y):
        self.x = x
        self.y = y

        

    # >>> p1
    #(1,2.2)
    def __repr__(self):
        x=self.x ; y=self.y
        return '({},{})'.format(x,y)

    # p1.display()
    # Point2D @ 0x7f258b9ebed0 (1,2.2)
    def display(self):
        print('Point2D @ {} ({},{})'.format(hex(id(self)),self.x,self.y))

        
        

