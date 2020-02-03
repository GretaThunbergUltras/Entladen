import cv2
import numpy as np
import brickpi3
from time import sleep
import ctypes

BP = brickpi3.BrickPi3()

palletCascade = cv2.CascadeCassifier('cascade_gruppe10.xml')

sonic = ctypes.CDLL("/usr/local/lib/libsonic.so")
sonic.measure.restype = ctypes.c_double
sonic.initalize()
while True:
	results = []
	returnValue = sonic.measure(ctypes.c_uint(0))
	if returnValue == 0:
		i = i-1
	else:
		results.append(round(returnValue, 2))
		print(results)
		results = []

