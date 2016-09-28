import bge


def main():

    cont = bge.logic.getCurrentController()
    light = cont.owner
    
    light.energy = light ["energy"]
    
#    if light ["lamp1"] == True:
#        light ["energy"] = 1.00
#    else:
#        light ["energy"] = 0.00

main()
