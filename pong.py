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
import time

currentlyRunning = True

pygame.init()
mainScreen = pygame.display.set_mode((1280, 1024), pygame.FULLSCREEN | pygame.HWSURFACE)
pygame.display.set_caption("PiPong")
pixelSizeX = 20
pixelSizeY = 16
pixelSize = [pixelSizeX, pixelSizeY]
BACKGROUNDCOLOR = (104, 255, 142)
WHITE = (255, 255, 255)
pongStart = False
pongPlay = False

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
	elif character == "a":
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) + pixelRasterize(2, True), pixelRasterize(carY, False) + pixelRasterize(.5, False), pixelRasterize(1, True), pixelRasterize(6, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(2, True), pixelRasterize(carY, False) + pixelRasterize(1.5, False), pixelRasterize(1, True), pixelRasterize(4, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) + pixelRasterize(3, True), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) - pixelRasterize(2, True), pixelRasterize(5, True), pixelRasterize(1, False)])
	elif character == "B":
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(2, True), pixelRasterize(carY, False), pixelRasterize(1, True), pixelRasterize(7, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False), pixelRasterize(3, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) - pixelRasterize(3, False), pixelRasterize(3, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) + pixelRasterize(3, False), pixelRasterize(3, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) + pixelRasterize(2, True), pixelRasterize(carY, False) - pixelRasterize(1.5, False), pixelRasterize(1, True), pixelRasterize(2, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) + pixelRasterize(2, True), pixelRasterize(carY, False) + pixelRasterize(1.5, False), pixelRasterize(1, True), pixelRasterize(2, False)])
	elif character == "b":
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(2, True), pixelRasterize(carY, False), pixelRasterize(1, True), pixelRasterize(7, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) + pixelRasterize(3, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) + pixelRasterize(2, True), pixelRasterize(carY, False) + pixelRasterize(1, False), pixelRasterize(1, True), pixelRasterize(3, False)])
	elif character == "C":
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(2, True), pixelRasterize(carY, False), pixelRasterize(1, True), pixelRasterize(7, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) - pixelRasterize(3, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) + pixelRasterize(3, False), pixelRasterize(5, True), pixelRasterize(1, False)])
	elif character == "c":
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) - pixelRasterize(1, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(2, True), pixelRasterize(carY, False) + pixelRasterize(1, False), pixelRasterize(1, True), pixelRasterize(5, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) + pixelRasterize(3, False), pixelRasterize(5, True), pixelRasterize(1, False)])
	elif character == "D":
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(2, True), pixelRasterize(carY, False), pixelRasterize(1, True), pixelRasterize(7, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(1, True), pixelRasterize(carY, False) - pixelRasterize(3, False), pixelRasterize(3, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(1, True), pixelRasterize(carY, False) + pixelRasterize(3, False), pixelRasterize(3, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) + pixelRasterize(2, True), pixelRasterize(carY, False), pixelRasterize(1, True), pixelRasterize(3, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) + pixelRasterize(1, True), pixelRasterize(carY, False) - pixelRasterize(2, False), pixelRasterize(1, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) + pixelRasterize(1, True), pixelRasterize(carY, False) + pixelRasterize(2, False), pixelRasterize(1, True), pixelRasterize(1, False)])
	elif character == "d":
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) + pixelRasterize(2, True), pixelRasterize(carY, False), pixelRasterize(1, True), pixelRasterize(5, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(2, True), pixelRasterize(carY, False) + pixelRasterize(1, False), pixelRasterize(1, True), pixelRasterize(3, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) + pixelRasterize(3, False), pixelRasterize(5, True), pixelRasterize(1, False)])
	elif character == "E":
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) - pixelRasterize(3, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) + pixelRasterize(3, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(2, True), pixelRasterize(carY, False), pixelRasterize(1, True), pixelRasterize(7, False)])
	elif character == "e":
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) - pixelRasterize(1, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) + pixelRasterize(1, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) + pixelRasterize(3, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) + pixelRasterize(2, True), pixelRasterize(carY, False), pixelRasterize(1, True), pixelRasterize(3, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(2, True), pixelRasterize(carY, False) + pixelRasterize(1, False), pixelRasterize(1, True), pixelRasterize(5, False)])
	elif character == "F":
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) - pixelRasterize(3, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(2, True), pixelRasterize(carY, False), pixelRasterize(1, True), pixelRasterize(7, False)])
	elif character == "f":
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) - pixelRasterize(1, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) + pixelRasterize(1, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(2, True), pixelRasterize(carY, False) + pixelRasterize(1, False), pixelRasterize(1, True), pixelRasterize(5, False)])
	elif character == "G":
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(2, True), pixelRasterize(carY, False), pixelRasterize(1, True), pixelRasterize(7, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) + pixelRasterize(1, True), pixelRasterize(carY, False), pixelRasterize(3, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) + pixelRasterize(2, True), pixelRasterize(carY, False) + pixelRasterize(1, False), pixelRasterize(1, True), pixelRasterize(3, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) - pixelRasterize(3, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) + pixelRasterize(3, False), pixelRasterize(5, True), pixelRasterize(1, False)])
	elif character == "g":
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) - pixelRasterize(1, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) + pixelRasterize(1, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True), pixelRasterize(carY, False) + pixelRasterize(3, False), pixelRasterize(5, True), pixelRasterize(1, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) - pixelRasterize(2, True), pixelRasterize(carY, False), pixelRasterize(1, True), pixelRasterize(3, False)])
		mainScreen.fill(color, rect=[pixelRasterize(carX, True) + pixelRasterize(2, True), pixelRasterize(carY, False) + pixelRasterize(1, False), pixelRasterize(1, True), pixelRasterize(5, False)])

while currentlyRunning:
	pygame.mouse.set_visible(False)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			currentlyRunning = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				if pongPlay == False:
					pongStart = True
			if event.key == pygame.K_W:
				pMoveOne = 1
			elif event.key == pygame.K_S:
				pMoveOne = 2
			else:
				pMoveOne = 3
			if event.key == pygame.K_UP:
				pMoveTwo = 1
			elif event.key == pygame.K_DOWN:
				pMoveTwo = 2
			else:
				pMoveTwo = 3
	mainScreen.fill(BACKGROUNDCOLOR)
	if pongStart == True:
		ponger = random.randint(1, 64)
		pOne = 32
		pTwo = 32
		pOneP = 0
		pTwoP = 0
		pBall = 32
		pProgress = 0
		pMove = False
		pongStart = False
		pongPlay = True
	if pongPlay == True:
		if pongMoveOne == 1:
			pOne -= 1
		elif pongMoveOne == 2:
			pOne += 1
		if pongMoveTwo == 1:
			pTwo -= 1
		elif pongMoveTwo == 2:
			pTwo += 1
		if pMove == False:
			pProgress += 1
			if pBall != ponger:
				if pBall < ponger:
					pBall += 1
				else:
					pBall -= 1
		elif pMove == True:
			pProgress -= 1
			if pBall != ponger:
				if pBall < ponger:
					pBall += 1
				else:
					pBall -= 1
		if pProgress == -28 and pBall in range(pOne - 2, pOne + 2):
			ponger = random.randint(1, 64)
			if pMove == False:
				pMove = True
			elif pMove == True:
				pMove == False
		elif pProgress == 28 and pBall in range(pTwo -2, pTwo + 2):
			ponger = random.randint(1, 64)
			if pMove == False:
				pMove = True
			elif pMove == True:
				pMove == False
		if pProgress == -32:
			pProgress == 0
			pTwoP += 1
		elif pProgress ==  32:
			pProgress == 0
			pOneP += 1
		if pOneP == 5:
			characterRender("A", (255,255,255), 16, 32)
			time.sleep(10)
			pongPlay = False
		if pTwoP == 5:
			characterRender("A", (255,255,255), 48, 32)
			time.sleep(10)
			pongPlay = False
		
		mainScreen.fill(WHITE, rect=[pixelRasterize(3, True), pixelRasterize(pOne, False), pixelRasterize(1, True), pixelRasterize(5, True)])
		mainScreen.fill(WHITE, rect=[pixelRasterize(61, True), pixelRasterize(pTwo, False), pixelRasterize(1, True), pixelRasterize(5, True)])
		mainScreen.fill(WHITE, rect=[pixelRasterize(pProgress + 32, True), pixelRasterize(pBall, False), pixelRasterize(1, True), pixelRasterize(1, False)])
	pygame.display.update()
	time.sleep(1 / 60)
pygame.quit()
sys.exit()
