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
####################################################n#########################



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

gl.n1 = 0
gl.n2 = 0
gl.n3 = 0
gl.n4 = 0
gl.n5 = 0
gl.n6 = 0
gl.n7 = 0
gl.n8 = 0
gl.n9 = 0
gl.n10 = 0
gl.n11 = 0
gl.n12 = 0
gl.n13 = 0
gl.n14 = 0
gl.n15 = 0
gl.n16 = 0
gl.n17 = 0
gl.n18 = 0
gl.ax = 0
gl.ay = 0
gl.az = 0

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

    if "/accelerometer" in gl.data:
        gl.ax = round(gl.data[2], 2)
        gl.ay = round(gl.data[3], 2)
        gl.az = round(gl.data[4], 2)



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
li1 = clamp(gl.n1, 0, 3.0)
li2 = clamp(gl.n2, 0, 3.0)
li3 = clamp(gl.n3, 0, 3.0)
li4 = clamp(gl.n4, 0, 3.25)
li5 = clamp(gl.n5, 0, 3.25)
li6 = clamp(gl.n6, 0, 3.25)
li7 = clamp(gl.n7, 0, 4.5)
li8 = clamp(gl.n8, 0, 4.5)
li9 = clamp(gl.n9, 0, 4.5)
li10 = clamp(gl.n10, 0, 5.75)
li11 = clamp(gl.n11, 0, 5.75)
li12 = clamp(gl.n12, 0, 5.75)
li13 = clamp(gl.n13, 0, 5.75)
li14 = clamp(gl.n14, 0, 6)
li15 = clamp(gl.n15, 0, 6)
li16 = clamp(gl.n16, 0, 6)
li17 = clamp(gl.n17, 0, 6)
li18 = clamp(gl.n18, 0, 6)

liAll = [li1,li2,li3,li4,li5,li6,li7,li8,li9,li10,li11,li12,li13,li14,li15,li16,li17,li18]


# Obtenemos los objetos de la escena


#controller = gl.getCurrentController()
#owner = controller.owner
owner = scene.objects["cam_main"]
#owner.localPosition = [gl.x/5, gl.y/5, gl.z/5]

#ow_rot_xyz = owner.localOrientation.to_euler()
#ow_rot_xyz[0] = math.radians(gl.x)
#ow_rot_xyz[1] = math.radians(gl.y)
#ow_rot_xyz[2] = math.radians(gl.z)
#owner.localOrientation = ow_rot_xyz.to_matrix()

######################### La Espera ##########################

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
pl6 = scene.objects["pl6"]
ico6 = scene.objects["ico6"]
pl7 = scene.objects["pl7"]
ico7 = scene.objects["ico7"]
pl8 = scene.objects["pl8"]
ico8 = scene.objects["ico8"]
pl9 = scene.objects["pl9"]
ico9 = scene.objects["ico9"]
pl10 = scene.objects["pl10"]
ico10 = scene.objects["ico10"]

print(ow_rot_xyz[2])

# Animacion Icoesferas Mutantes
ico1.localPosition = [gl.n1-38.42, gl.n2-29.62, gl.az*10]
ico2.localPosition = [gl.n3-12.25, gl.n4-40.19, 0]
ico3.localPosition = [gl.n5-19.95, gl.n6-17.79, 0]
ico4.localPosition = [gl.n7+8.30, gl.n8-32.11, 0]
ico6.localPosition = [gl.n9-19.10, gl.n10-28.19, 0]
ico7.localPosition = [gl.n11-4.10, gl.n12-27.20, 0]
ico8.localPosition = [gl.n13+20.75, gl.n14-20.71, 0]
ico9.localPosition = [gl.n15+7.47, gl.n16-52.05, 0]
ico10.localPosition = [gl.n17-33.24, gl.n18-10.63, 0]

pl5.energy = float(random.choice(liAll*10))

#ico1.localScale = [gl.n5, gl.n15, gl.n5] ## Si el origen esta en el centro, se agranda enorme y garpa mucho
#ico1.localScale = [clamp(gl.n5, 2.5, 5), clamp(gl.n5, 2.5, 5), clamp(gl.n5, 2.5, 5)]


######################### Ciudad Mutante ##########################
# Luces edificios
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

# Icoesferas mini
sm_ico1 = scene.objects["sm_ico1"]
sm_ico2 = scene.objects["sm_ico2"]

#Animacion Luces
sm_gl9 = clamp(gl.n9, -1, 1)
sm_gl10 = clamp(gl.n10, -1.3, 1.3)

sm_gl16 = clamp(gl.n16, -0.5, 0.5)
sm_gl17 = clamp(gl.n17, -0.5, 0.5)
sm_gl18 = clamp(gl.n18, -0.5, 0.5)


sm_ico1.localPosition = [sm_gl9+1.99, sm_gl10+0.26, 0.176]
sm_ico2.localPosition = [sm_gl16-0.355, sm_gl17+1.393, sm_gl18+0.538]

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

######################### La CUEVA ##########################
# Objetos
ico_tunel1 = scene.objects["ico_tunel1"]
ico_tunel2 = scene.objects["ico_tunel2"]
ico_tunel3 = scene.objects["ico_tunel3"]
ico_tunel4 = scene.objects["ico_tunel4"]
ico_tunel5 = scene.objects["ico_tunel5"]
ico_tunel6 = scene.objects["ico_tunel6"]
ico_tunel7 = scene.objects["ico_tunel7"]
ico_tunel8 = scene.objects["ico_tunel8"]
ico_tunel9 = scene.objects["ico_tunel9"]
ico_tunel10 = scene.objects["ico_tunel10"]
ico_tunel11 = scene.objects["ico_tunel11"]
ico_tunel12 = scene.objects["ico_tunel12"]

# variables
it1 = clamp(gl.n1, -3, 3)
it2 = clamp(gl.n3, -5, 5)
it3 = clamp(gl.n5, -6.5, 6.5)
it4 = clamp(gl.n7, -8, 8)
it5 = clamp(gl.n9, -9.5, 9.5)
it6 = clamp(gl.n11, -11, 11)
it7 = clamp(gl.n12, -12.5, 12.5)
it8 = clamp(gl.n10, -14, 14)
it9 = clamp(gl.n8, -15.5, 15.5)
it10 = clamp(gl.n6, -17, 17)
it11 = clamp(gl.n4, -18.5, 18.5)
it12 = clamp(gl.n2, -20, 20)


# Animaciones La Cueva
ico_tunel1.localPosition = [it1-3.00, 44.08, -3.39]
ico_tunel2.localPosition = [it2-3.00, 49.33, -5.46]
ico_tunel3.localPosition = [it3-3.00, 58.36, -9.01]
ico_tunel4.localPosition = [it4-3.00, 67.37, -12.45]
ico_tunel5.localPosition = [it5-3.00, 76.45, -16.02]
ico_tunel6.localPosition = [it6-3.00, 85.48, -19.57]
ico_tunel7.localPosition = [it7-3.00, 94.54, -23.05]
ico_tunel8.localPosition = [it8-3.00, 103.62, -26.62]
ico_tunel9.localPosition = [it9-3.00, 112.65, -30.17]
ico_tunel10.localPosition = [it10-3.00, 121.66, -33.62]
ico_tunel11.localPosition = [it11-3.00, 130.74, -37.18]
ico_tunel12.localPosition = [it12-3.00, 139.77, -40.73]


# Send
res = 30*random.random() - 15  # from 15 to 15gl.my_sender.simple_send_to("/blender/x", res, (gl.ip_out, gl.port_out))