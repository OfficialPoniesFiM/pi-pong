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

def characterRender(character, color, carX, carY):
	if character == "A":
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) - pixelRasterize(3, False), pixelRasterize(5, True), pixelRasterize(1, True)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(2, True), pixelRasterize(carY, False), pixelRasterize(1, True), pixelRasterize(7, True)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) + pixelRasterize(2, True), pixelRasterize(carY, False), pixelRasterize(1, True), pixelRasterize(7, True)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False), pixelRasterize(5, True), pixelRasterize(1, False)])
	else if character == "a":
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) + pixelRasterize(2, True), pixelRasterize(carY, False) + pixelRasterize(.5, False), pixelRasterize(1, True), pixelRasterize(6, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(2, True), pixelRasterize(carY, False) + pixelRasterize(1.5, False), pixelRasterize(1, True), pixelRasterize(4, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) + pixelRasterize(3, True), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) - pixelRasterize(2, True), pixelRasterize(5, True), pixelRasterize(1, False)])
	else if character == "B":
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(2, True), pixelRasterize(carY, False), pixelRasterize(1, True), pixelRasterize(7, False])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False), pixelRasterize(3, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) - pixelRasterize(3, False), pixelRasterize(3, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) + pixelRasterize(3, False), pixelRasterize(3, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) + pixelRasterize(2, True), pixelRasterize(carY, False) - pixelRasterize(1.5, False), pixelRasterize(1, True), pixelRasterize(2, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) + pixelRasterize(2, True), pixelRasterize(carY, False) + pixelRasterize(1.5, False), pixelRasterize(1, True), pixelRasterize(2, False)])
	else if character == "b":
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(2, True), pixelRasterize(carY, False), pixelRasterize(1, True), pixelRasterize(7, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) + pixelRasterize(3, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) + pixelRasterize(2, True), pixelRasterize(carY, False) + pixelRasterize(1, False), pixelRasterize(1, True), pixelRasterize(3, False)])
	else if character == "C":
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(2, True), pixelRasterize(carY, False), pixelRasterize(1, True), pixelRasterize(7, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) - pixelRasterize(3, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) + pixelRasterize(3, False), pixelRasterize(5, True), pixelRasterize(1, False)])
	else if character == "c":
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) - pixelRasterize(1, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(2, True), pixelRasterize(carY, False) + pixelRasterize(1, False), pixelRasterize(1, True), pixelRasterize(5, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) + pixelRasterize(3, False), pixelRasterize(5, True), pixelRasterize(1, False)])
	else if character == "D":
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(2, True), pixelRasterize(carY, False), pixelRasterize(1, True), pixelRasterize(7, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(1, True), pixelRasterize(carY, False) - pixelRasterize(3, False), pixelRasterize(3, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(1, True), pixelRasterize(carY, False) + pixelRasterize(3, False), pixelRasterize(3, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) + pixelRasterize(2, True), pixelRasterize(carY, False), pixelRasterize(1, True), pixelRasterize(3, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) + pixelRasterize(1, True), pixelRasterize(carY, False) - pixelRasterize(2, False), pixelRasterize(1, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) + pixelRasterize(1, True), pixelRasterize(carY, False) + pixelRasterize(2, False), pixelRasterize(1, True), pixelRasterize(1, False)])
	else if character == "d":
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) + pixelRasterize(2, True), pixelRasterize(carY, False), pixelRasterize(1, True), pixelRasterize(5, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(2, True), pixelRasterize(carY, False) + pixelRasterize(1, False), pixelRasterize(1, True), pixelRasterize(3, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) + pixelRasterize(3, False), pixelRasterize(5, True), pixelRasterize(1, False)])

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
