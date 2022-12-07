#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 13:29:48 2022

@author: david
"""

from ..grid import Cell

def test_Fill_Empty():
    
    c = Cell(2, 2, 4, 4)
    
    
    c.fill()
    
    assert c.occupied == True
    