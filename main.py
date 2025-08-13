# -*- coding: utf_8 -*-
import direct.directbase.DirectStart
from modules.location import gameLocation

from pandac.PandaModules import Vec4

from modules.control import mouseControl

loc = gameLocation()
loc.loadTerrain('res/textures/heightfield.png')

loc.setTexture('res/textures/grass.png',20,20)
loc.setLights(Vec4(0.6,0.6,0.6,1), Vec4(1,1,1,1))
mc=mouseControl()
run()