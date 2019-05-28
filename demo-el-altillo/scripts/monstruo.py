import bge
import math
import random
from bge import logic as gl

def main():
    controller = bge.logic.getCurrentController()
    monstruo = controller.owner
    keyboard = bge.logic.keyboard.events
    scene = gl.getCurrentScene()
    
    

    if keyboard[bge.events.TABKEY]==1:
        bge.types.KX_CharacterWrapper.jump(bge.constraints.getCharacter(monstruo)) 
    
    if monstruo["direccion"] == False:
        monstruo.localScale[0] = (1.0)
    else:
        monstruo.localScale[0] = (-1.0)

main()