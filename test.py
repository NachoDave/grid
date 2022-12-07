#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 16:25:33 2022

@author: david
"""

from grid import Cell
#ßhelp(Cell)

def test_bulk():
    c = Cell(2, 2, 4, 4)
    assert c.neighbours() == 4
    
    assert c.left() == (1, 2)
    assert c.right()  == (3, 2)
    assert c.up() == (2, 3)
    assert c.down() == (2, 1)