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
#    if "/t7" in gl.data:
#        gl.z = gl.data[2]
#        print("gl.z como llega: ")
#        print(gl.z)
    if "/f0" in gl.data:
        gl.f0 = gl.data[2]*10
    if "/f1" in gl.data:
        gl.f1 = gl.data[2]*10
    if "/f2" in gl.data:
        gl.f2 = gl.data[2]*10
    if "/f3" in gl.data:
        gl.f3 = gl.data[2]*10
    if "/f4" in gl.data:
        gl.f4 = gl.data[2]*10

# Move the Cube
controller = gl.getCurrentController()
owner = controller.owner
#owner.localPosition = [0.3*gl.x, 0.3*gl.y, 2*gl.z]

scene = gl.getCurrentScene()
cubo = scene.objects["Cube"]
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

o0.localPosition.z = gl.f0
o1.localPosition.z = gl.f1
o2.localPosition.z = gl.f2
o3.localPosition.z = gl.f3
o4.localPosition.z = gl.f4

#gl.z = gl.z*20

#t7.localPosition.z = gl.z
#t6.localPosition.z = gl.z*2
#t5.localPosition.z = gl.z*3
#t4.localPosition.z = gl.z*5
#t3.localPosition.z = gl.z*8
#t2.localPosition.z = gl.z*13
#t1.localPosition.z = gl.z*21

#cam = scene.active_camera
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