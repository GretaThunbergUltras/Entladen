import cv2
import numpy as np
import brickpi3
from time import sleep
import ctypes

BP = brickpi3.BrickPi3()

palletCascade = cv2.CascadeClassifier('cascade_gruppe10.xml')
	def getHeightOfPallet():
		#calc
		#pixellength calculated to a cm amount
		#cm amount minus way from the upper side of the pallet to the lower side of the pallet
		print('jo')

	def calcTheTimeToDrive():
		#get the distance to pallet with octo and calc how long you have to drive to reach it
		#calc
		print('Jo')

	def palletAndTruckROI():
		#cut everthing then the truck and the pallet
		roi = img[(x1, y1), (x2, 0)]
		blankImageSize = img.size()
		blankImage = np.zeros(([blankImageSize]), dtype = np.uint8)
		blankImage[(x1,y1), (x2,0)] = roi

#drive till there is something in range of 30cm in front of the car
while ultrasonic(i) =< 30:

	BP.set_motor_power(BP.PORT_B, 25)
	sleep(0.5)

#brake
BP.set_motor_power(BP.PORT_B, 0)

#get the right distance when standing
distanceToTruck = distanceFromOctosonarInTheFront()

#open up the cam
cap = cv2.VideoCapture(0)

while True:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	pallet = palletCascade.detectMultiScale(gray, 3, 5)
	if cv2.CascadeClassifier.empty() == True:
		while True:
			print('Cant load Cascade')

	for(x1,y1,x2,y2) in pallet:
		#draw rectangle aroud detected pallet
		cv2.rectangle(img, (x1,y1), (x1+x2, y1+y2), (0,255,0), 5)
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img, 'Pallet', (x2+10, y2+10), font, 1, (0,255,0), 3, cv2.LINE_AA
		imshow('Obj Det', img)

	# pallet is found
	if len(pallet) != 0:
		#cascade can be release somehow
	#perhaps first do canny then get the roi with the next good lines to the detected objects
		palletAndTruckROI
		# do canny detection to get some clean pics 
		canny = cv2.canny(blankImage, 100, 200)
		cv2.contours
		#here we have to get the pixel value of the upper line of the Truck so we can get the length from the ground to the pallet height
		getHeightOfPallet()
		#getForkToTheRightHeight
		driveTheWayToPallet()
		#set up the motor for the right time
		#release everything not needed
		cap.release()
		break

	# if no pallet  is found
	else:
		#drive a bit forward and try again to recognize it
		#octosonarDontCrash
		BP.set_motor_power(BP.PORT_B, 20)
		time.sleep(0.5sec)
		continue

while distanceInFront() =! distance to the truck if you stand right in front of it:
	#drive slowly till the truck is surely in front of you
	BP.set_motor_powe(BP.PORT_B, 20)
	time.sleep(1)

#set fork to carry mode
#drive backwards and check to not crash till distance is ok
while checkOctorsonar in the front != 20cm:
	BP.set_motor_power(BP.PORT_B,-50)
	#for a predefinded time
	time.sleep(5)

#do a 180 degree turn from other group
