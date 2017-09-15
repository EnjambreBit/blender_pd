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

import math
import random
import bge
from bge import logic as gl

# Listen every frame
gl.data = gl.my_receiver.get_data()
print("===========================")
print("gl.data")
print(gl.data)
print("===========================")

# Get x, y in data OSC message
if gl.data:
    if "/accelerometer" in gl.data:
        gl.x = gl.data[2]
        gl.y = gl.data[3]
        gl.z = gl.data[4]

    if "/multi/2" in gl.data:
        gl.mt2_x = round(gl.data[2], 2)
        gl.mt2_y = round(gl.data[3], 2)
        
    if "/multi/5" in gl.data:
        gl.mt5_x = round(gl.data[2], 2)
        gl.mt5_y = round(gl.data[3], 2)

controller = gl.getCurrentController()
owner = controller.owner
#owner.localPosition = [gl.x/5, gl.y/5, gl.z/5]

#ow_rot_xyz = owner.localOrientation.to_euler()
#ow_rot_xyz[0] = math.radians(gl.x)
#ow_rot_xyz[1] = math.radians(gl.y)
#ow_rot_xyz[2] = math.radians(gl.z)
#owner.localOrientation = ow_rot_xyz.to_matrix()

# Obtenemos los objetos de la escena
scene = gl.getCurrentScene()
#cubo = scene.objects["Cube"]

newX = (gl.mt5_x * 5)
newY = -(gl.mt5_y * 5)
newZ = (gl.mt2_x * 2)

print(newX)

owner.localPosition = [newX, newY, newZ]


# Send
#res = 30*random.random() - 15  # from 15 to 15gl.my_sender.simple_send_to("/blender/x", res, (gl.ip_out, gl.port_out))