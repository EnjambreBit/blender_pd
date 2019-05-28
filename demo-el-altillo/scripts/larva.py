import bge
import math
import random
from bge import logic as gl

def main():
    controller = bge.logic.getCurrentController()
    larva = controller.owner
    keyboard = bge.logic.keyboard.events
    scene = gl.getCurrentScene()
    nube1 = scene.objectsInactive["cloud1"]
    inicio_nubes = scene.objects["inicio_nubes"]
    iposX = inicio_nubes.localPosition[0]
    iposY = inicio_nubes.localPosition[1]
    iposZ = inicio_nubes.localPosition[2]
    
    

    if keyboard[bge.events.TABKEY]==1:
        bge.types.KX_CharacterWrapper.jump(bge.constraints.getCharacter(larva)) 
        
    if keyboard[bge.events.CKEY]==1:
        bge.render.setBackgroundColor([.25,0,0,0])
        
    if keyboard[bge.events.NKEY]==1:
        nposX = iposX + (random.uniform(-40,40))
        nposY = iposY + (random.uniform(-40,40))
        
        inicio_nubes.localPosition =[nposX, nposY, iposZ]
        
        nube = scene.addObject(nube1, inicio_nubes)
        
        inicio_nubes.localPosition = [iposX, iposY, iposZ]
    
    if larva["direccion"] == False:
        larva.localScale[0] = (1.0)
    else:
        larva.localScale[0] = (-1.0)

main()