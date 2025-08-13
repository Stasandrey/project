# -*- coding: utf_8 -*-

from pandac.PandaModules import GeoMipTerrain, Filename

from pandac.PandaModules import Texture,TextureStage
from pandac.PandaModules import AmbientLight, PointLight

from modules.control import cameraHandler

from pandac.PandaModules import BitMask32

class gameLocation():
    def __init__(self):
        self.terrain=GeoMipTerrain("Terrain")
        taskMgr.add(self.update, 'location_update')
        camera = cameraHandler()

    def loadTerrain(self, hfFile):
        self.terrain.setHeightfield(Filename(hfFile))
        self.terrain.setBlockSize(32)
        self.terrain.setFactor(64)
        self.terrain.setMinLevel(2)
        self.terrain.getRoot().reparentTo(render)
        self.terrain.getRoot().setSz(30)
        self.terrain.generate()
        self.terrain.setFocalPoint(base.camera)

        gnodes = self.terrain.getRoot().findAllMatches("+GeomNode")
        for gnode in gnodes:
            gnode.node().setIntoCollideMask(BitMask32.bit(1))



    def update(self, task):
        self.terrain.update()
        # self.terrain.getRoot().setRenderModeWireframe()
        return task.cont

    def setTexture(self, texFile, sx, sy):
        self.terrain.getRoot().setTexture(loader.loadTexture(texFile))
        self.terrain.getRoot().setTexScale(TextureStage.getDefault(), sx, sy)
        self.terrain.getRoot().getTexture().setMinfilter(Texture.FTLinearMipmapLinear)

    def setLights(self, ambient_l, camera_l):
        self.ambientLight = render.attachNewNode(AmbientLight("ambientLight"))
        self.pointLight = camera.attachNewNode(PointLight("PointLight"))
        self.ambientLight.node().setColor(ambient_l)
        self.pointLight.node().setColor(camera_l)
        render.setLight(self.ambientLight)
        render.setLight(self.pointLight)
