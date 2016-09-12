#!/usr/bin/python3
# -*- coding: UTF-8 -*-

## blenderOSC_always.py

#############################################################################
# Copyright (C) Labomedia July 2014
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franproplin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#############################################################################

# Adaptado por Iván Hoffmann

'''
This script run at all frame.
'''

import random
import bge
from bge import logic as gl

# Listen every frame
gl.data = gl.my_receiver.get_data()

# Get x, y in data OSC message
if gl.data:
    if "/t7" in gl.data:
        gl.z = gl.data[2]
    if "/f0" in gl.data:
        gl.f0 = gl.data[2]
    if "/f1" in gl.data:
        gl.f1 = gl.data[2]
    if "/f2" in gl.data:
        gl.f2 = gl.data[2]
    if "/f3" in gl.data:
        gl.f3 = gl.data[2]
    if "/f4" in gl.data:
        gl.f4 = gl.data[2]
        
    # Variables de la camara
    if "/camx" in gl.data:
        gl.camx = gl.data[2]
    if "/camy" in gl.data:
        gl.camy = gl.data[2]
    if "/camz" in gl.data:
        gl.camz = gl.data[2]
    if "/cam" in gl.data:
        gl.cam = gl.data[2]
    if "/cam_noise" in gl.data:
        gl.cam_noise = gl.data[2]

# 
controller = gl.getCurrentController()
#owner = controller.owner
#owner.localPosition = [0.3*gl.x, 0.3*gl.y, 2*gl.z]

# Obtenemos los objetos de la escena
scene = gl.getCurrentScene()
#cubo = scene.objects["Cube"]
#t1 = scene.objects["t1"]
#t2 = scene.objects["t2"]
#t3 = scene.objects["t3"]
#t4 = scene.objects["t4"]
#t5 = scene.objects["t5"]
#t6 = scene.objects["t6"]
#t7 = scene.objects["t7"]

o0 = scene.objects["o0"]
o1 = scene.objects["o1"]
o2 = scene.objects["o2"]
o3 = scene.objects["o3"]
o4 = scene.objects["o4"]

luz = scene.objects["luz"]
luz2 = scene.objects["luz2"]
luz3 = scene.objects["luz3"]

t_sonidos = scene.objects["t_sonidos"]

cam_noise_empty = scene.objects["cam_noise_empty"]


# Animamos objetos
o0.localPosition.z = gl.f0
o1.localPosition.z = gl.f1
o2.localPosition.z = gl.f2
o3.localPosition.z = gl.f3
o4.localPosition.z = gl.f4

luz.energy = gl.z*100
luz.energy = gl.f2*100
luz.energy = gl.f3*100


t_sonidos.localPosition.z = gl.f0

print("-------")
print("luz.energy")
print(luz.energy)
print("-------")

if luz.energy <= 1.0:
    luz.energy = 1.0

print("-------")
print("luz.energy")
print(luz.energy)
print("-------")
#gl.z = gl.z*20

#t7.localPosition.z = gl.z
#t6.localPosition.z = gl.z*2
#t5.localPosition.z = gl.z*3
#t4.localPosition.z = gl.z*5
#t3.localPosition.z = gl.z*8
#t2.localPosition.z = gl.z*13
#t1.localPosition.z = gl.z*21

print("gl.cam: ")
print(gl.cam)

camara = "cam"+str(gl.cam)
print(camara)

scene.active_camera = camara
cam = scene.active_camera
#cam.localPosition.x = gl.camx
#cam.localPosition.y = gl.camy
#cam.localPosition.z = gl.camz

cam_posx = cam.localPosition.x
cam_posy = cam.localPosition.y
cam_posz = cam.localPosition.z

print("cam_position")
print(cam.localPosition)

cam.localPosition = [+gl.camx, +gl.camy, +gl.camz]
cam_noise_empty.localPosition = [gl.cam_noise, gl.cam_noise, gl.cam_noise]

#for x in scene.objects:
#    print(x)

#t7.color = [gl.z, 0.0, 0.0, 1.0]
#t6.color = [gl.z, gl.z, 0.0, 1.0]
#t5.color = [gl.z, gl.z, gl.z, 1.0]
#t4.color = [0.0, gl.z, 0.0, 1.0]
#t3.color = [0.0, gl.z, gl.z, 1.0]
#t2.color = [gl.z, 0.0, gl.z, 1.0]
#t2.color = [0.0, 0.0, gl.z, 1.0]


# Send
res = 30*random.random() - 15  # from 15 to 15gl.my_sender.simple_send_to("/blender/x", res, (gl.ip_out, gl.port_out))