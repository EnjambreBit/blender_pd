#!/usr/bin/python3
# -*- coding: UTF-8 -*-

## sonidos-mutantes_always.py
## Basado en blenderOSC_always.py
## Adaptado por Iván Hoffmann - ihoffmann@enjambrebit.com.ar

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


def clamp(n, minn, maxn):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n

# Listen every frame
gl.data = gl.my_receiver.get_data()

# Imprime gl.data para debug
print("===========================")
print("gl.data")
print(gl.data)
print("===========================")

# Get x, y in data OSC message
if gl.data:
    if "/n" in gl.data:
#        gl.n1 = gl.data[2]
#        gl.n2 = gl.data[3]
#        gl.n3 = gl.data[4]
#        gl.n4 = gl.data[5]
#        gl.n5 = gl.data[6]
#        gl.n6 = gl.data[7]
#        gl.n7 = gl.data[8]
#        gl.n8 = gl.data[9]
#        gl.n9 = gl.data[10]
#        gl.n10 = gl.data[11]

# Redondeando valores a 2 decimales
        gl.n1 = round(gl.data[2], 2)
        gl.n2 = round(gl.data[3], 2)
        gl.n3 = round(gl.data[4], 2)
        gl.n4 = round(gl.data[5], 2)
        gl.n5 = round(gl.data[6], 2)
        gl.n6 = round(gl.data[7], 2)
        gl.n7 = round(gl.data[8], 2)
        gl.n8 = round(gl.data[9], 2)
        gl.n9 = round(gl.data[10], 2)
        gl.n10 = round(gl.data[11], 2)

# Obtenemos la escena actual
scene = gl.getCurrentScene()

# Obtenemos los objetos de la escena
luz1 = scene.objects["luz1"]
luz2 = scene.objects["luz2"]
luz3 = scene.objects["luz3"]
tunel1 = scene.objects["tunel1"]
tunel_ventanas1 = scene.objects["tunel_ventanas1"]
logo_enjambre = scene.objects["logo_enjambre"]

# "Escenarios"
domo1 = scene.objects["domo1"]

# Random colors from gl.data
gl.all = [gl.n1,gl.n2,gl.n3,gl.n4,gl.n5,gl.n6,gl.n7,gl.n8,gl.n9,gl.n10]
rand_red = random.choice(gl.all)
rand_green = random.choice(gl.all)
rand_blue = random.choice(gl.all)

# Limitamos variables de posicion para mantenerlas dentro del domo
ln1 = clamp(gl.n1, -8, 8)
ln6 = clamp(gl.n6, -8, 8)
ln10 = clamp(gl.n10, -8, 8)

# Animamos objetos
luz1.localPosition.z = ln1
luz2.localPosition.z = ln6
luz3.localPosition.z = ln10

tunel_ventanas1.color = [rand_red, 0.0, 0.0, 1.0]

#logo_enjambre.localScale = [rand_red, rand_green, rand_blue]
logo_enjambre.color = [rand_red, rand_green, rand_blue, 1.0]

print("---------")
print(tunel_ventanas1.color)
print("---------")


#for x in scene.objects:
#    print(x)

# Send
res = 30*random.random() - 15  # from 15 to 15gl.my_sender.simple_send_to("/blender/x", res, (gl.ip_out, gl.port_out))