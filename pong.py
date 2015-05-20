#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
#  pong.py
#  
#  Copyright 2015, Nathan Guerrero and Giovanni Galvan @ Chopper Studios
#  PiPong - A recreation of the classic game designed for the Raspberry Pi with special controllers.  
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# We need to import things for them to work.
import pygame
import sys
import random
import RPi.GPIO as GPIO
import time

pygame.init()
pygame.display.set_mode([1280, 1024], pygame.FULLSCREEN | pygame.HWSURFACE)
pixelSizeX = 20
pixelSizeY = 16
pixelSize = [pixelSizeX, pixelSizeY]
