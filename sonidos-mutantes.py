#!/usr/bin/python3
# -*- coding: UTF-8 -*-

## sonidos-mutantes.py
## Basado en test.py de Labomedia

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

import subprocess

subprocess.Popen('pd-extended ./enjambre-sonidos-mutantes.pd', shell=True)

subprocess.Popen('blender ./sonidos-mutantes_v01.blend', shell=True)
