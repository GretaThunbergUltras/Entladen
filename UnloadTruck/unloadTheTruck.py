import cv2
import numpy as np
import brickpi3
from time import sleep
import ctypes
from botlib.bot import Bot
#from botlib.bot import Forklift

bot = None


class unloadTheTruck:
	#make bot None
	
	#forklift = None
	
	#make an Obj to use the BrickPi
	BP = brickpi3.BrickPi3()
	#loads the trained cascade
	palletCascade = cv2.CascadeClassifier('cascade_gruppe10.xml')

	#portC = move back and forwards range 0 - -5000
	#portA = move the fork up and down range 0 - -2500
	#portB = driving motor range -100 - 100
	#portD = steering
	#def pickUpFork():
	#	BP.set_motor_position(BP.PORT_C, -5000)
	#	BP.set_motor_position(BP.PORT_A, -2500)

	#def setForkOnHeight(height):
	#	BP.set_motor_position(BP.PORT_C, 0)
	#	BP.set_motor_position(BP.PORT_A, height)

	#def layDownFork():
	#	BP.set_motor_position(BP.PORT_C, 0)
	#	BP.set_motor_position(BP.PORT_A, 0)

	def nothing():
		pass

	#def initializeForklift():
		#global forklift
		#forklift = Forklift()
	
	def initializeRob():
		global bot
		bot = Bot()
		bot.calibrate()
		
	def follow_line(self):
            from threading import Thread

        linetracker = self._bot.linetracker()

        def follow():
            for improve in linetracker:
                if improve != None:
                    self._bot.drive_steer(improve)
                    # TODO: is this needed
                    sleep(0.1)

        thread = Thread(group=None, target=follow, daemon=True)
        thread.start()

	def umdrehen():
		'''
		Roboter macht eine Dreipunktwende nach rechts hinten.
		Funktion ist NICHT kollisionsfrei.
		Basiert darauf dass alle Motoren zum Fahren unter allen Situationen gleich schnell laufen und
		einen gleichen gleichen Wendekreis haben.
		'''
		bot.drive_steer(1)
		sleep(1)
		bot.drive_power(-30)
		sleep(3.52)
		bot.drive_power(0)
		sleep(1)
		bot.drive_steer(0)
		sleep(1)
		bot.drive_steer(-1)
		bot.drive_power(30)
		sleep(3.52)
		bot.drive_power(0)
		bot.drive_steer(0)
		sleep(1)
		bot.drive_power(20)
		sleep(1)
		bot.drive_power(0)

	def getDistance(k):
		#if you uncomment the commented lines you get a average distance
		sonic = ctypes.CDLL("/usr/local/lib/libsonic.so")
		sonic.measure.restype = ctypes.c_double
		#count and sum for more accuracy if needed(if speed is needed)
		#counter = 0
		#sum = 0
		sonic.initalize()
		#for average put 10 or 100 in
		for i in range(1):
			results = 0
			returnValue = sonic.measure(ctypes.c_uint(k))
			if returnValue == 0:
				i -= 1
			else:
				results = (round(returnValue, 2))
				mittelwert = results
				#sum = sum + results
				#counter = counter + 1
			print(results)
			#results = 0
		#mittelwert = sum//counter
		round(mittelwert, 1)
		return mittelwert

	def getHeightOfPallet():
		print('JO')

	def palletAndTruckROI(x1, y1, x2, img):
		#tried to make a ROI getting a better usage of the picture and less trash
		roi = img[(x1,y1), (x2,0)]
		blankImageSize = img.size()
		blankImage = np.zeros(([blankImageSize]), dtype = np.uint8)
		blankImage[(x1,y1), (x2, 0)] = roi
		return roi
	#set up the bot and calibrate
	initializeRob()
	#start driving (distance doesnt matter)
	#self.follow_line()
	BP.set_motor_power(BP.PORT_B, 40)
	#inital distance check while driving
	distance = getDistance(0)
	#drive fast till your distance is lower than 80cm
	while distance > 80:
		print('driving fast')
		distance = getDistance(0)
	#drive slower till you reach 40 cm
	BP.set_motor_power(BP.PORT_B, 25)
	distance = getDistance(0)
	while distance > 40:
		print('driving slow')
		distance = getDistance(0)
	#stop the engine
	print('stop')
	BP.set_motor_power(BP.PORT_B, 0)
	#save distance while standing
	distanceToTruck = getDistance(0)
	#start the vid
	cap = cv2.VideoCapture(0)
	print('vid')
	while 1:
		#get the img
		ret, img = cap.read()
		#make a gray version of img
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		#try to detect the pallet
		print('try to detect pallet')
		pallet = palletCascade.detectMultiScale(gray, 1.1, 3)
		#draw the lines on the img
		for (x, y, w, h) in pallet:
			print("Pallet detected")
			print("X: {:d}, Y: {:d}, W: {:d}, H: {:d}".format(x, y, w, h))
			cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

		if len(pallet) != 0:
			print("There is something detected")
			#make roi with 
			x1 = x-5
			x2 = x+w+5
			y1 = y-5
			img2 = img[y1:640, x1:x2]
			cv2.imshow('PalletAndTruck', img2)
			#make canny
			canny = cv2.Canny(img2, 100,200)
			#make lineDetection
			
			#get results of this linedetection (find the floor and the upper edge of the pallet)
			
			#calculate the height and set it in to the fork function
			bot._forklift.set_rotation_forward()
			bot._forklift.set_custom_height(13.5)
			sleep(3)
			break
		else:
			#try it again
			BP.set_motor_power(BP.PORT_B, 20)
			sleep(0.5)
			BP.set_motor_power(BP.PORT_B, 0)
			sleep(1)
			continue

		#this will be erased later
		k = cv2.waitKey(30) & 0xff
		if k == 27:
			break
	#drive slowly till you get in closer distance to the Truck
	print('detected and fork is setted up, now drive slowly')
	BP.set_motor_power(BP.PORT_B, 20)
	distance = getDistance(0)
	while distance > 10:
		print('last 10cm')
		distance = getDistance(0)
	BP.set_motor_power(BP.PORT_B, 13)
	#hier die zeit anpassen
	sleep(8)
	#distance = getDistance(0)
	#brauchen wir nicht umbedingt
	#while distance > 4:
		#distance = getDistance(0)
	#print('last 4cm')
	BP.set_motor_power(BP.PORT_B, 0)
	
	#pick up the pallet
	bot._forklift.set_rotation_backward()

	#drive backwards till you reach enough distance
	BP.set_motor_power(BP.PORT_B, -50)
	distance = getDistance(2)
	#drive till you got enough distance to the Truck
	while distance < 80:
		distance = getDistance(2)
	BP.set_motor_power(BP.PORT_B, 0)
	#make a 180 degree turn around
	umdrehen()

	cap.release()
	cv2.destroyAllWindows()
