# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:06:00 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

x,y,z=mc.player.getTilePos()
for i in range(20):
    r = random.randrange(1,7)
    if r == 1:
        mc.setBlocks(x,y,z,x,y,z+4,86)
        z = z+4
    if r == 2:
        mc.setBlocks(x,y,z,x,y,z-4,46)
        z = z-4  
    if r == 3:    
        mc.setBlocks(x,y,z,x+4,y,z,20)
        x = x+4 
    if r == 4:
        mc.setBlocks(x,y,z,x-4,y,z,7)
        x= x-4 
    if r == 5:
        mc.setBlocks(x,y,z,x,y+4,z,7)
        y=y+4        
    if r == 6:
        mc.setBlocks(x,y,z,x,y-4,z,20)
        y=y-4
        