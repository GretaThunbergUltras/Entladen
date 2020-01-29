def getForkToPickUpHeightForLKW(self, height=None):
        # rotate forward
        self._rotate_motor.to_init_position()	
		
        # move fork on the right height
		if height != None:
			#height = height / (maxHeight/2)-1
			pos = self.height_motor.position_from_factor(height)
		else:
			pos = self._height_motor.position_from_factor(-1.0)
			
		self._height_motor.change_position(pos)