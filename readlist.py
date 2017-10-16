# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 18:40:31 2017

@author: will
"""

with open("list.txt") as f:
    content = f.readlines()
conent = [x.strip() for x in content]

print("testing output")
