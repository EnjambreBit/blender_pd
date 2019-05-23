import bge
from bge import logic as gl

def main():
    controller = bge.logic.getCurrentController()
    larva = controller.owner
    
    if larva["direccion"] == False:
        larva.localScale[0] = (1.0)
    else:
        larva.localScale[0] = (-1.0)

main()