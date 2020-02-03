import ctypes 

sonic = ctypes.CDLL("/usr/local/lib/libsonic.so")   

sonic.measure.restype = ctypes.c_double

try:
	sonic.initalize()
	while True:
		results = []
		for i in range(3):
			returnValue = sonic.measure(ctypes.c_uint(i))
			if returnValue == 0:
				i -= 1
			else:
				results.append(round(returnValue, 2))
		
		print(results)
		results = []

except KeyboardInterrupt:
	print("\nCTRL-C pressed. Cleaning up and exiting.")

