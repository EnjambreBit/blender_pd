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
import math
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
#print("===========================")
#print("gl.data")
#print(gl.data)
#print("===========================")

# Get x, y in data OSC message
if gl.data:
    if "/n" in gl.data:
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
        gl.n11 = round(gl.data[12], 2)
        gl.n12 = round(gl.data[13], 2)
        gl.n13 = round(gl.data[14], 2)
        gl.n14 = round(gl.data[15], 2)
        gl.n15 = round(gl.data[16], 2)
        gl.n16 = round(gl.data[17], 2)
        gl.n17 = round(gl.data[18], 2)
        gl.n18 = round(gl.data[19], 2)

# Obtenemos la escena actual
scene = gl.getCurrentScene()
#for x in scene.objects:
#    print("objectos")
#    print(x)
#    print("___________")

# Random colors from gl.data
gl.all = [gl.n1,gl.n2,gl.n3,gl.n4,gl.n5,gl.n6,gl.n7,gl.n8,gl.n9,gl.n10,gl.n11,gl.n12,gl.n13,gl.n14,gl.n15]
rand_red = random.choice(gl.all)
rand_green = random.choice(gl.all)
rand_blue = random.choice(gl.all)

sub_bass = [gl.n1,gl.n2,gl.n3] # 20, 30, 50 Hz
bass = [gl.n3,gl.n4,gl.n5] # 50, 100, 200 Hz
low_mid = [gl.n5,gl.n6,gl.n7] # 200, 300, 500 Hz
mid = [gl.n7,gl.n8,gl.n9] # 500, 1000, 2000 Hz
upper_mid = [gl.n9,gl.n10,gl.n11] # 2, 3, 4 kHz
presence = [gl.n11,gl.n12,gl.n13] # 4, 5, 6 kHz
brillance = [gl.n13,gl.n14,gl.n15,gl.n16,gl.n17,gl.n18] # 6, 8, 10, 12, 14, 15 kHz


# Limitamos variables para intensidad de luces
li1 = clamp(gl.n1, 0, 1.0)
li2 = clamp(gl.n2, 0, 1.0)
li3 = clamp(gl.n3, 0, 1.0)
li4 = clamp(gl.n4, 0, 1.25)
li5 = clamp(gl.n5, 0, 1.25)
li6 = clamp(gl.n6, 0, 1.25)
li7 = clamp(gl.n7, 0, 1.5)
li8 = clamp(gl.n8, 0, 1.5)
li9 = clamp(gl.n9, 0, 1.5)
li10 = clamp(gl.n10, 0, 1.75)
li11 = clamp(gl.n11, 0, 1.75)
li12 = clamp(gl.n12, 0, 1.75)
li13 = clamp(gl.n13, 0, 1.75)
li14 = clamp(gl.n14, 0, 2)
li15 = clamp(gl.n15, 0, 2)
li16 = clamp(gl.n16, 0, 2)
li17 = clamp(gl.n17, 0, 2)
li18 = clamp(gl.n18, 0, 2)

liAll = [li1,li2,li3,li4,li5,li6,li7,li8,li9,li10,li11,li12,li13,li14,li15,li16,li17,li18]


# Obtenemos los objetos de la escena

# Acto 0 - La espera
pl1 = scene.objects["pl1"]
ico1 = scene.objects["ico1"]
pl2 = scene.objects["pl2"]
ico2 = scene.objects["ico2"]
pl3 = scene.objects["pl3"]
ico3 = scene.objects["ico3"]
pl4 = scene.objects["pl4"]
ico4 = scene.objects["ico4"]
pl5 = scene.objects["pl5"]
ico5 = scene.objects["ico5"]

# Animacion Icoesferas Mutantes
ico1.localPosition = [gl.n1-38.42, gl.n2-29.62, 0]
ico2.localPosition = [gl.n5-12.25, gl.n6-40.19, 0]
ico3.localPosition = [gl.n9-19.95, gl.n10-17.79, 0]
ico4.localPosition = [gl.n14+8.30, gl.n16-32.11, 0]

pl5.energy = float(random.choice(liAll*10))

#ico1.localScale = [gl.n5, gl.n15, gl.n5] ## Si el origen esta en el centro, se agranda enorme y garpa mucho
#ico1.localScale = [clamp(gl.n5, 2.5, 5), clamp(gl.n5, 2.5, 5), clamp(gl.n5, 2.5, 5)]

# Acto 1 - Ciudad Mutante
e1_l1 = scene.objects["e1_l1"]
e1_l2 = scene.objects["e1_l2"]
e1_l3 = scene.objects["e1_l3"]
e1_l4 = scene.objects["e1_l4"]
e1_l5 = scene.objects["e1_l5"]
e1_l6 = scene.objects["e1_l6"]
e1_l7 = scene.objects["e1_l7"]
e1_l8 = scene.objects["e1_l8"]
e1_l9 = scene.objects["e1_l9"]
e1_l10 = scene.objects["e1_l10"]
e1_l11 = scene.objects["e1_l11"]
e1_l12 = scene.objects["e1_l12"]
e1_l13 = scene.objects["e1_l13"]
e1_l14 = scene.objects["e1_l14"]
e1_l15 = scene.objects["e1_l15"]

#Animacion Luces

#e1_l1.energy = random.choice(gl.all)

# sub_bass lamps
e1_l4.energy = float(li1)
e1_l5.energy = float(li2)
e1_l8.energy = float(li3)

# bass lamps
e1_l14.energy = float(li4)
e1_l10.energy = float(li5)

# low_mid lamps
e1_l6.energy = float(li6)
e1_l10.energy = float(li7)

# mid lamps
e1_l15.energy = float(random.choice(mid))

##upper_mid lamps
e1_l9.energy = float(li9)
e1_l12.energy = float(li10)

## presence lamps
e1_l1.energy = float(li11)
e1_l2.energy = float(li12)
e1_l3.energy = float(li13)


# brillance lamps
e1_l7.energy = float(li16)
e1_l13.energy = float(li17)
e1_l11.energy = float(li18)

# Send
res = 30*random.random() - 15  # from 15 to 15gl.my_sender.simple_send_to("/blender/x", res, (gl.ip_out, gl.port_out))