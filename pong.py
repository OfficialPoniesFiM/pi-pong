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

currentlyRunning = True

pygame.init()
mainScreen = pygame.display.set_mode((1280, 1024), pygame.FULLSCREEN | pygame.HWSURFACE)
pygame.display.set_caption("PiPong")
pixelSizeX = 20
pixelSizeY = 16
pixelSize = [pixelSizeX, pixelSizeY]
BACKGROUNDCOLOR = (104, 255, 142)

def pixelRasterize(pixelMultiplier, xy):
	if xy == True:
		return pixelMultiplier * (1280 / 20)
	else:
		return pixelMultiplier * (1024 / 16)
	

while currentlyRunning:
	pygame.mouse.set_visible(False)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			currentlyRunning = False
	mainScreen.fill(BACKGROUNDCOLOR)
	pygame.display.update()
	time.sleep(1 / 60)
pygame.quit()
sys.exit()
