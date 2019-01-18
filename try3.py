from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *
import numpy as np


class Cordinates():
		replayBtn = (340,390)
		dinoLimity = (480,466)
		#x= 100 y=415


def restartGame():
		pyautogui.click(Cordinates.replayBtn)#Açãode Click


def pressSpace():
		pyautogui.keyDown('space')
		# time.sleep(0.05)
		print('Jump')
		pyautogui.keyUp('space')

def imageGrab():
	box = (Cordinates.dinoLimity[0]+10,Cordinates.dinoLimity[1], Cordinates. dinoLimity[0]+100,Cordinates.dinoLimity[1]+30)
	 
	image = ImageGrab.grab(box)
	grayImage = ImageOps.grayscale(image)
	a = array(grayImage.getcolors())

	if a.sum()!= 2947:
		print(a.sum())

	return a.sum()

def getImageAt(x1,y1, x2,y2):
	
	img = ImageGrab.grab(bbox=(x1,y1,x2,y2)) #bbox specifies specific region (bbox= x,y,width,height *starts top-left)
	grayImg = ImageOps.grayscale(img)
	arrayImg = np.array(grayImg)
	#print(arrayImg.sum())
	return arrayImg.sum()
restartGame()
x1 = 460
y1 = 445
x11 = x1+40
y11 = y1+40
while True:
	imgg = imageGrab()
	
	if(imgg> 2947+3000):
		pressSpace()
		#time.sleep(0.1)
	ll = getImageAt(x1, y1, x11, y11)
		
	if (ll == 190892):
		time.sleep(3)
		print('---------------------------------------------')
		restartGame()
	print(imgg, ll)

