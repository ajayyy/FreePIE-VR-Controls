import math
from collections import namedtuple

Quaternion = namedtuple('Quaternion', 'w x y z')
Euler = namedtuple('Euler', 'x y z')

#right hand rule
def R_matrix_pitch(theta):
    R_matrix_X = [[1,0,0,0],[0,math.cos(theta),-math.sin(theta),0],[0,math.sin(theta),math.cos(theta),0],[0,0,0,0]]
    return R_matrix_X

def R_matrix_yaw(theta):
    R_matrix_Y = [[math.cos(theta),0,math.sin(theta),0],[0,1,0,0],[-math.sin(theta),0,math.cos(theta),0],[0,0,0,0]]
    return R_matrix_Y

def R_matrix_roll(theta):
    R_matrix_Z = [[ math.cos(theta),-math.sin(theta),0,0 ] , [math.sin(theta) , math.cos(theta),0,0], [0,0,1,0],[0,0,0,0 ]]
    return R_matrix_Z

#alternate transform generation, apply yaw pitch roll in that order sequentially:
def AltTransformMatrix_yawpitchroll(yaw,pitch,roll):
    firstOperation = matrixMultiply(R_matrix_yaw(yaw), R_matrix_pitch( pitch )) #rotate yaw
    secondOperation = matrixMultiply(firstOperation, R_matrix_roll( roll ))
    return secondOperation

def matrixMultiply(m1,m2):
    prodM = []
    for i in range(len(m1)): #for each row of m1
        row = m1[i]
        newRow = []
        for j in range(len(m2[0])): #for each column of m2
            y = 0
            for x in range(len(row)):
                rowEl = row[x]
                colEl = m2[x][j]
                y += rowEl*colEl
                #if (y < 0.000005 and y > 0): #rounding 0 to make easier to read print out
                #    y = 0.0
                #if (y == 1):
                #    y = 1.0
            newRow.append(y)
        prodM.append(newRow)
    return prodM

def quaternion_to_euler(q):
    sqw = q.w * q.w
    sqx = q.x * q.x
    sqy = q.y * q.y
    sqz = q.z * q.z

    normal = math.sqrt(sqw + sqx + sqy + sqz)
    pole_result = (q.x * q.z) + (q.y * q.w)

    if (pole_result > (0.5 * normal)): # singularity at north pole
        ry = math.pi/2 #heading/yaw?
        rz = 0 #attitude/roll?
        rx = 2 * math.atan2(q.x, q.w) #bank/pitch?
        return Euler(rx, ry, rz)
    if (pole_result < (-0.5 * normal)): # singularity at south pole
        ry = -math.pi/2
        rz = 0
        rx = -2 * math.atan2(q.x, q.w)
        return Euler(rx, ry, rz)

    r11 = 2*(q.x*q.y + q.w*q.z)
    r12 = sqw + sqx - sqy - sqz
    r21 = -2*(q.x*q.z - q.w*q.y)
    r31 = 2*(q.y*q.z + q.w*q.x)
    r32 = sqw - sqx - sqy + sqz

    rx = math.atan2( r31, r32 )
    ry = math.asin ( r21 )
    rz = math.atan2( r11, r12 )

    return Euler(rx, ry, rz)

recenter = keyboard.getPressed(Key.PageDown)
toggle = keyboard.getPressed(Key.PageUp)


if starting:
   enabled = False
   multiply = 17
   #oculusVR.center()
   #oculusVR.update += update
   
if toggle:
  	enabled = not enabled

if recenter:
	pass
   	#oculusVR.center()
   	
global pressed
def vive_controller():
	i=0
	
	global posxhmd
	global posyhmd
	global poszhmd
	global orrxhmd
	global orryhmd
	global orrzhmd
	global posx0
	global posy0
	global posz0
	global orrpitch0
	global orryaw0
	global orrroll0
	global posx1
	global posy1
	global posz1
	global orrpitch1
	global orryaw1
	global orrroll1
	global pressed
	global R_matrix_calibrationCenter
	global T_matrix_calibrationCenter	
	db = 0.3 #deadband for joysticks
	
	global IMURrx
	global IMURry
	global IMURrz
	global IMURrw
	
	#save calibration values in this
	global LHandpitch1
	global LHandyaw1
	global LHandroll1
	global RHandpitch1
	global RHandyaw1
	global RHandroll1
	
	joyLi = 0 #index of joysticks[] device object list (see Core plugins Joystick)
	joyRi = 1
	
	Lone = wiimote[joyLi].buttons.button_down(WiimoteButtons.DPadUp) or wiimote[joyLi].buttons.button_down(WiimoteButtons.DPadDown) or wiimote[joyLi].buttons.button_down(WiimoteButtons.DPadLeft) or wiimote[joyLi].buttons.button_down(WiimoteButtons.DPadRight)
	Ltrigger = wiimote[joyLi].buttons.button_down(WiimoteButtons.B)
	Lfour = wiimote[joyLi].buttons.button_down(WiimoteButtons.One)
	Lstart = wiimote[joyLi].buttons.button_down(WiimoteButtons.Home)
	Lbumper = wiimote[joyLi].buttons.button_down(WiimoteButtons.A)
	
	Rone = wiimote[joyRi].buttons.button_down(WiimoteButtons.DPadUp) or wiimote[joyRi].buttons.button_down(WiimoteButtons.DPadDown) or wiimote[joyRi].buttons.button_down(WiimoteButtons.DPadLeft) or wiimote[joyRi].buttons.button_down(WiimoteButtons.DPadRight)
	Rtrigger = wiimote[joyRi].buttons.button_down(WiimoteButtons.B)
	Rfour = wiimote[joyRi].buttons.button_down(WiimoteButtons.One)
	Rstart = wiimote[joyRi].buttons.button_down(WiimoteButtons.Home)
	Rbumper = wiimote[joyRi].buttons.button_down(WiimoteButtons.A)
	
	diagnostics.watch(wiimote[joyLi].buttons.button_down(WiimoteButtons.B))
	diagnostics.watch(wiimote[joyRi].buttons.button_down(WiimoteButtons.B))
	diagnostics.watch(leap.rightroll)

	diagnostics.watch(wiimote[joyLi].buttons.button_down(WiimoteButtons.A))
	diagnostics.watch(wiimote[joyRi].buttons.button_down(WiimoteButtons.DPadUp))
	diagnostics.watch(wiimote[joyLi].buttons.button_down(WiimoteButtons.DPadDown))
	
	if pressed == 0:
		if ((wiimote[joyLi].buttons.button_down(WiimoteButtons.Minus)) ):
			#hydra[0].isDocked = True
			#hydra[1].isDocked = True
			
			hydra[1].pitch = 0
			hydra[1].yaw = 0
			hydra[1].roll = 0
			hydra[1].x = -65 #driver fails/doesn't calibrate if the controllers share 0,0,0 when .start changes to True
			hydra[1].y = -45
			hydra[1].z = -200
			hydra[1].side = 'L'
			
			hydra[0].pitch = 0
			hydra[0].yaw = 0
			hydra[0].roll = 0
			hydra[0].x = 65
			hydra[0].y = -45
			hydra[0].z = -200
			hydra[0].side = 'R'
		
			hydra[0].start = True
			hydra[1].start = True
			
			hydra[0].isDocked = False
			hydra[1].isDocked = False			
			#oculusVR.center
			
			#calibration orientation and position
			T_matrix_calibrationCenter = [ [1,0,0, freeTrack.x], [0,1,0,freeTrack.y], [0,0,1,freeTrack.z], [0,0,0,1] ]
			R_matrix_calibrationCenter = AltTransformMatrix_yawpitchroll(freeTrack.yaw, freeTrack.pitch, freeTrack.roll)
			
			orrpitch1 = freeTrack.pitch
			orryaw1 = freeTrack.yaw
			orrroll1 = freeTrack.roll
			
			#calibrate left hand
			#IMURlx = joystick[joyLi].x/float(1024)
			#IMURly = joystick[joyLi].y/float(1024)
			#IMURlz = joystick[joyLi].xRotation/float(1024)
			#IMURlw = joystick[joyLi].yRotation/float(1024)
			
			#calibrate right hand
			#IMURrx = joystick[joyRi].x/float(1024)
			#IMURry = joystick[joyRi].y/float(1024)
			#IMURrz = joystick[joyRi].xRotation/float(1024)
			#IMURrw = joystick[joyRi].yRotation/float(1024)
		
			#eulersL = quaternion_to_euler(Quaternion(IMURlw, IMURlx, IMURly, IMURlz))
			#eulersR = quaternion_to_euler(Quaternion(IMURrw, IMURrx, IMURry, IMURrz))
			
			#LHandpitch1 = eulersL.z +math.pi
			#LHandyaw1 = -eulersL.x 
			#LHandroll1 = -eulersL.y +math.pi
			
			LHandpitch1 = wiimote[joyLi].ahrs.pitch
			LHandyaw1 = -wiimote[joyLi].ahrs.yaw
			LHandroll1 = -wiimote[joyLi].ahrs.roll
			
			RHandpitch1 = wiimote[joyRi].ahrs.pitch
			RHandyaw1 = -wiimote[joyRi].ahrs.yaw
			RHandroll1 = -wiimote[joyRi].ahrs.roll
			
		def log_motionplus():
			diagnostics.watch(wiimote[joyLi].ahrs.yaw)
   			diagnostics.watch(wiimote[joyLi].ahrs.pitch)
   			diagnostics.watch(wiimote[joyLi].ahrs.roll)
   			diagnostics.watch(wiimote[joyRi].ahrs.yaw)
   			diagnostics.watch(wiimote[joyRi].ahrs.pitch)
   			diagnostics.watch(wiimote[joyRi].ahrs.roll)

		if starting:
			system.setThreadTiming(TimingTypes.HighresSystemTimer)
   			system.threadExecutionInterval = 2
   			
   			wiimote[joyLi].motionplus.update += log_motionplus
   			wiimote[joyRi].motionplus.update += log_motionplus
   			
   			wiimote[joyLi].enable(WiimoteCapabilities.MotionPlus)
   			wiimote[joyRi].enable(WiimoteCapabilities.MotionPlus)
   			
   			diagnostics.watch(wiimote[joyLi].ahrs.yaw)
   			diagnostics.watch(wiimote[joyLi].ahrs.pitch)
   			diagnostics.watch(wiimote[joyLi].ahrs.roll)
   			diagnostics.watch(wiimote[joyRi].ahrs.yaw)
   			diagnostics.watch(wiimote[joyRi].ahrs.pitch)
   			diagnostics.watch(wiimote[joyRi].ahrs.roll)
   			
			pressed = 1 
			
		#elif (wiimote[joyLi].buttons.button_down(WiimoteButtons.Plus)):
			#hydra[1].start = True
			#pressed = 1
		elif (wiimote[joyRi].buttons.button_down(WiimoteButtons.Minus)):
			hydra[0].start = True
			pressed = 1
	#elif (wiimote[i].buttons.button_down(WiimoteButtons.Plus) or wiimote[i].buttons.button_down(WiimoteButtons.Minus)):
		#pressed = 1
	else:
		hydra[0].start = False
		hydra[1].start = False
		pressed = 0
	
	
	
	#---------- SET HAND POSITIONS: HMD pos + Leap hand pos using 4x4 matrix transformations
	
	if pressed == 0: #tracking (not recentering)
		#shiftForward = 0#0.20 #15cm
		
		#debug using the other controller:
		#hydra[0].x = 0
		#hydra[0].y = 0 
		#hydra[0].z = 0
		#hydra[0].pitch = orrpitch1
		#hydra[0].yaw = orryaw1
		#hydra[0].roll = orrroll1

		hydra[0].one = Lone
		hydra[0].trigger = Ltrigger
		hydra[0].four = Lfour
		hydra[0].start = Lstart
		hydra[0].bumper = Lbumper
		hydra[0].joybutton = wiimote[joyLi].buttons.button_down(WiimoteButtons.Plus)
		if wiimote[joyRi].buttons.button_down(WiimoteButtons.DPadRight):
			hydra[0].joyx = 1
		elif wiimote[joyRi].buttons.button_down(WiimoteButtons.DPadLeft):
			hydra[0].joyx = -1
		if wiimote[joyRi].buttons.button_down(WiimoteButtons.DPadUp):
			hydra[0].joyy = 1
		elif wiimote[joyRi].buttons.button_down(WiimoteButtons.DPadDown):
			hydra[0].joyy = -1
		#hydra[0].joyx = joystick[joyLi].z/float(1024)
		#hydra[0].joyy = -joystick[joyLi].zRotation/float(1024)
		
		hydra[1].one = Rone
		hydra[1].trigger = Rtrigger
		hydra[1].four = Rfour
		hydra[1].start = Rstart
		hydra[1].bumper = Rbumper
		hydra[1].joybutton = wiimote[joyRi].buttons.button_down(WiimoteButtons.Plus)
		if wiimote[joyLi].buttons.button_down(WiimoteButtons.DPadRight):
			hydra[1].joyx = 1
		elif wiimote[joyLi].buttons.button_down(WiimoteButtons.DPadLeft):
			hydra[1].joyx = 0
		if wiimote[joyLi].buttons.button_down(WiimoteButtons.DPadUp):
			hydra[1].joyy = 1
		elif wiimote[joyLi].buttons.button_down(WiimoteButtons.DPadDown):
			hydra[1].joyy = 0

		#hydra[0].joyx = -joystick[joyRi].z/float(1024)
		#hydra[0].joyy = joystick[joyRi].zRotation/float(1024)
		
		#hydra controls
		
		deltaX = freeTrack.x - T_matrix_calibrationCenter[0][3]
		deltaY = freeTrack.y - T_matrix_calibrationCenter[1][3]
		deltaZ = freeTrack.z - T_matrix_calibrationCenter[2][3]
		T_matrix_current = [ [1,0,0, deltaX], [0,1,0,deltaY], [0,0,1,deltaZ], [0,0,0,1] ]#curent T of hmd, relative to calibration point
		
		deltaYaw = freeTrack.yaw - orryaw1
		deltaPitch = freeTrack.pitch -orrpitch1
		deltaRoll = freeTrack.roll - orrroll1
		R_matrix_current = AltTransformMatrix_yawpitchroll(deltaYaw, deltaPitch, deltaRoll) #curent R of hmd, relative to calibration point
		
		#create transformation of Leap sensor data to HMD position (e.g. used to calculate the Leap's coordinate system in space, relative to calibration point)
		distanceBetweenEyesToLeapSensor = [0,0,-0.08] #8cm
		T_matrix_leap = [ [1,0,0,0], [0,1,0,0], [0,0,1,distanceBetweenEyesToLeapSensor[2]],[0,0,0,1] ]# translate to leap sensor along z (forward)
		R_matrix_leap = matrixMultiply(R_matrix_pitch(-math.pi/2),R_matrix_roll(math.pi))# generate rotation matrix of the eye-center to the mounted leap on the Oculus DK2
		
		#continue the transformation matrix by translating to the IB's origin
		distanceFromLeapToIB = [.1175,-.0825,-.0735] # see Interaction Box: https://developer.leapmotion.com/documentation/csharp/devguide/Leap_Coordinate_Mapping.html
		T_matrix_interactionbox = T_matrix_leap
		T_matrix_interactionbox[0][3] += distanceFromLeapToIB[0]
		T_matrix_interactionbox[1][3] += distanceFromLeapToIB[1]
		T_matrix_interactionbox[2][3] += distanceFromLeapToIB[2]
		
		#compose final transformation matrix of HMD to Leap data, (will be used to calculate IB-Leap data relative to HMD coordinate system)
		Tr_matrix_Leap = matrixMultiply(T_matrix_interactionbox, R_matrix_leap)
		
		#FORMAT LEAP SENSOR DATA--------------:
		
		#scale leap's IB normallized units
		scaleLeapToIB = [.835,.835,.747] #see dimensions of Interaction Box: https://developer.leapmotion.com/documentation/csharp/devguide/Leap_Coordinate_Mapping.html
		scaleOffset = [-0.5,0,0.5]
		
		enableLeapTracking = 1 #change to 1 or 0

		
		LeapDataR = [ [1,0,0,(leap.rightxpos+scaleOffset[0])*scaleLeapToIB[0]*enableLeapTracking], [0,1,0,(-leap.rightypos+scaleOffset[1])*scaleLeapToIB[1]*enableLeapTracking], [0,0,1,(-leap.rightzpos+scaleOffset[2])*scaleLeapToIB[2]*enableLeapTracking],[0,0,0,1] ]
		LeapDataL = [ [1,0,0,(leap.leftxpos+scaleOffset[0])*scaleLeapToIB[0]*enableLeapTracking], [0,1,0,(-leap.leftypos+scaleOffset[1])*scaleLeapToIB[1]*enableLeapTracking], [0,0,1,(-leap.leftzpos+scaleOffset[2])*scaleLeapToIB[2]*enableLeapTracking],[0,0,0,1] ]

		diagnostics.watch(LeapDataL[0][3])
		diagnostics.watch(LeapDataL[1][3])
		diagnostics.watch(LeapDataL[2][3])

		diagnostics.watch(LeapDataR[0][3])
		diagnostics.watch(LeapDataR[1][3])
		diagnostics.watch(LeapDataR[2][3])
		
		
		#check to see if 0, 1, or 2 hands are visible
		leftHandVisible = True
		rightHandVisible = True
		#if (LeapDataL[0][3] == LeapDataL[1][3] and LeapDataL[1][3] == LeapDataL[2][3] and LeapDataL[2][3] == 0):
		#	leftHandVisible = False
		#if (LeapDataR[0][3] == LeapDataR[1][3] and LeapDataR[1][3] == LeapDataR[2][3] and LeapDataR[2][3] == 0):
		#	rightHandVisible = False
		
		#if no leap, place controller/hand at eye-center for L and R hands
		if (LeapDataR[0][3] == LeapDataR[1][3] and LeapDataR[1][3] == LeapDataR[2][3] and LeapDataR[2][3] == 0):
			showHandR = .200
			rightHandVisible = False
		else:
			showHandR = -.200 #subtract the calibration distance, this is poorly understood behavior by the driver, see calibration step
		

		if (LeapDataL[0][3] == LeapDataL[1][3] and LeapDataL[1][3] == LeapDataL[2][3] and LeapDataL[2][3] == 0):
			showHandL = .200
			leftHandVisible = False
		else:
			showHandL = -.200 #subtract the calibration distance, this is poorly understood behavior by the driver, see calibration step
		
		LeapDataL[1][3] +=(showHandL)
		LeapDataR[1][3] +=(showHandR)
		
		Tr_matrix_HMD_LeapDataL = matrixMultiply(Tr_matrix_Leap,LeapDataL) #Leap data from perspective of current frame's HMD delta pos/rot
		Tr_matrix_HMD_LeapDataR = matrixMultiply(Tr_matrix_Leap,LeapDataR) #Leap data from perspective of current frame's HMD delta pos/rot
		T_matrix_HMD_LeapDataL = [ [1,0,0, Tr_matrix_HMD_LeapDataL[0][3] ], [0,1,0,Tr_matrix_HMD_LeapDataL[1][3] ], [0,0,1,Tr_matrix_HMD_LeapDataL[2][3] ] , [0,0,0,1] ] #this position is relative to the HMD position
		T_matrix_HMD_LeapDataR = [ [1,0,0, Tr_matrix_HMD_LeapDataR[0][3] ], [0,1,0,Tr_matrix_HMD_LeapDataR[1][3] ], [0,0,1,Tr_matrix_HMD_LeapDataR[2][3] ] , [0,0,0,1] ] #this position is relative to the HMD position
		
		#remove delta rotate to match calibration point's coordinate system (i.e. emulated hydra base station's coordinate space)
		Tr_matrix_deltaCalibration_LeapDataL = matrixMultiply(R_matrix_current,T_matrix_HMD_LeapDataL)
		Tr_matrix_deltaCalibration_LeapDataR = matrixMultiply(R_matrix_current,T_matrix_HMD_LeapDataR)
		
		#translate the amount user moved from calibration point
		T_matrix_Calibrated_LeapDataL_x = Tr_matrix_deltaCalibration_LeapDataL[0][3]+T_matrix_current[0][3]
		T_matrix_Calibrated_LeapDataL_y = Tr_matrix_deltaCalibration_LeapDataL[1][3]+T_matrix_current[1][3]
		T_matrix_Calibrated_LeapDataL_z = Tr_matrix_deltaCalibration_LeapDataL[2][3]+T_matrix_current[2][3]
		#...for R hand:
		T_matrix_Calibrated_LeapDataR_x = Tr_matrix_deltaCalibration_LeapDataR[0][3]+T_matrix_current[0][3]
		T_matrix_Calibrated_LeapDataR_y = Tr_matrix_deltaCalibration_LeapDataR[1][3]+T_matrix_current[1][3]
		T_matrix_Calibrated_LeapDataR_z = Tr_matrix_deltaCalibration_LeapDataR[2][3]+T_matrix_current[2][3]
		
		METER_TO_MM = 1200 #scales from meters
		
		#if hand visible update, else use previous value
		if(leftHandVisible):
			hydra[1].x = (T_matrix_Calibrated_LeapDataL_x*METER_TO_MM) 
			hydra[1].y = (T_matrix_Calibrated_LeapDataL_y*METER_TO_MM) 
			hydra[1].z = (T_matrix_Calibrated_LeapDataL_z*METER_TO_MM)
			
		if(rightHandVisible):
			hydra[0].x = (T_matrix_Calibrated_LeapDataR_x*METER_TO_MM) 
			hydra[0].y = (T_matrix_Calibrated_LeapDataR_y*METER_TO_MM) 
			hydra[0].z = (T_matrix_Calibrated_LeapDataR_z*METER_TO_MM) 
	
		#---------- SET HAND ROTATION FROM Arduino HID DEVICES, CONVERT FROM SHORT TO FLOAT
		#IMURlx = joystick[joyLi].x/float(1024)
		#IMURly = joystick[joyLi].y/float(1024)
		#IMURlz = joystick[joyLi].xRotation/float(1024)
		#IMURlw = joystick[joyLi].yRotation/float(1024)
		
		#IMURrx = joystick[joyRi].x/float(1024)
		#IMURry = joystick[joyRi].y/float(1024)
		#IMURrz = joystick[joyRi].xRotation/float(1024)
		#IMURrw = joystick[joyRi].yRotation/float(1024)
		
		#eulersL = quaternion_to_euler(Quaternion(IMURlw, IMURlx, IMURly, IMURlz))
		#eulersR = quaternion_to_euler(Quaternion(IMURrw, IMURrx, IMURry, IMURrz))
		
		#hydra[1].yaw  = -( eulersL.z-LHandpitch1)
		#hydra[1].roll = (eulersL.x-LHandyaw1)
		#hydra[1].pitch = (eulersL.y-LHandroll1)
		
		#hydra[0].yaw  = -( eulersR.z-RHandpitch1)
		#hydra[0].roll = (eulersR.x-RHandyaw1)
		#hydra[0].pitch = (eulersR.y-RHandroll1)
		
		
		hydra[0].yaw = wiimote[joyRi].ahrs.yaw
		hydra[0].pitch = -wiimote[joyRi].ahrs.pitch
		hydra[0].roll = wiimote[joyRi].ahrs.roll

		hydra[1].yaw = wiimote[joyLi].ahrs.yaw
		hydra[1].pitch = -wiimote[joyLi].ahrs.pitch
		hydra[1].roll = wiimote[joyLi].ahrs.roll
		
	diagnostics.watch(leap.rightpitch)
	diagnostics.watch(leap.rightyaw)
	diagnostics.watch(leap.rightroll)

	diagnostics.watch(leap.leftpitch)
	diagnostics.watch(leap.leftyaw)
	diagnostics.watch(leap.leftroll)
	
	#----------
	#diagnostics.watch(joystick[joyLi].getDown(1))
	#diagnostics.watch(joystick[joyRi].getDown(1))
	
	#freeTrack.x = posxhmd
	#freeTrack.y = posyhmd
	#freeTrack.z = poszhmd
	#freeTrack.yaw = orrxhmd
	#freeTrack.pitch = orryhmd
	#freeTrack.roll = orrzhmd

	diagnostics.watch(Rone)
	diagnostics.watch(Rtrigger)
	#diagnostics.watch(Rfour)
	diagnostics.watch(Rstart)
	diagnostics.watch(Rbumper)
	
	diagnostics.watch(Lone)
	diagnostics.watch(Ltrigger)
	#diagnostics.watch(Lfour)
	diagnostics.watch(Lstart)
	diagnostics.watch(Lbumper)

	#diagnostics.watch(xbox360[i].a)
	#diagnostics.watch(xbox360[i].b)
	#diagnostics.watch(xbox360[i].x)
	#diagnostics.watch(xbox360[i].y)
	#diagnostics.watch(xbox360[i].start)
	#diagnostics.watch(xbox360[i].back)
	#diagnostics.watch(xbox360[i].leftStickX)
	#diagnostics.watch(xbox360[i].leftStickY)
	#diagnostics.watch(xbox360[i].rightStickX)
	#diagnostics.watch(xbox360[i].rightStickY)
	#diagnostics.watch(xbox360[i].leftShoulder)
	#diagnostics.watch(xbox360[i].rightShoulder)
	#diagnostics.watch(xbox360[i].leftTrigger)
	#diagnostics.watch(xbox360[i].rightTrigger)
	#diagnostics.watch(posx0)
	#diagnostics.watch(posy0)
	#diagnostics.watch(posz0)
	#diagnostics.watch(orrpitch0)
	#diagnostics.watch(orryaw0)
	#diagnostics.watch(orrroll0)
	#diagnostics.watch(posx1)
	#diagnostics.watch(posy1)
	#diagnostics.watch(posz1)
	#diagnostics.watch(orrpitch1)
	#diagnostics.watch(orryaw1)
	#diagnostics.watch(orrroll1)
	#diagnostics.watch(posxhmd)
	#diagnostics.watch(posyhmd)
	#diagnostics.watch(poszhmd)
	#diagnostics.watch(orrxhmd)
	#diagnostics.watch(orryhmd)
	#diagnostics.watch(orrzhmd)
	#diagnostics.watch(IMURlx)
	#diagnostics.watch(IMURly)
	#diagnostics.watch(IMURlz)
	#diagnostics.watch(IMURlw)
	#diagnostics.watch(oculusVR.x)
	#diagnostics.watch(oculusVR.y)
	#diagnostics.watch(oculusVR.z)
	#diagnostics.watch(oculusVR.pitch)
	#diagnostics.watch(oculusVR.yaw)
	#diagnostics.watch(oculusVR.roll)
	#diagnostics.watch(RightHandPos_x)  
	#diagnostics.watch(RightHandPos_y)
	#diagnostics.watch(RightHandPos_z)
	

def hydra_init():
	hydra[0].pitch = 0
	hydra[0].yaw = 0
	hydra[0].roll = 0
	hydra[0].x = 0
	hydra[0].y = 0
	hydra[0].z = 0

	hydra[1].pitch = 0
	hydra[1].yaw = 0
	hydra[1].roll = 0
	hydra[1].x = 0
	hydra[1].y = 0
	hydra[1].z = 0

def vive_init():
	global posxhmd
	global posyhmd
	global poszhmd
	posxhmd = 0
	posyhmd = 0
	poszhmd = 0
	global orrxhmd
	global orryhmd
	global orrzhmd
	orrxhmd = 0
	orryhmd = 0
	orrzhmd = 0
	global posx0
	global posy0
	global posz0
	posx0 = 0
	posy0 = 0
	posz0 = 0
	global orrpitch0
	global orryaw0
	global orrroll0
	orrpitch0 = 0
	orryaw0 = 0
	orrroll0 = 0
	global posx1
	global posy1
	global posz1
	posx1 = 0
	posy1 = 0
	posz1 = 0
	global orrpitch1
	global orryaw1
	global orrroll1
	orrpitch1 = 0
	orryaw1 = 0
	orrroll1 = 0

	global R_matrix_calibrationCenter
	R_matrix_calibrationCenter = [ [1,0,0, 0], [0,1,0,0], [0,0,1, 0], [0,0,0,1] ]
	global T_matrix_calibrationCenter
	T_matrix_calibrationCenter = [ [1,0,0, 0], [0,1,0,0], [0,0,1, 0], [0,0,0,1] ]
	
	global RHandpitch1
	RHandpitch1 = 0
	global RHandyaw1
	RHandyaw1 = 0
	global RHandroll1
	RHandroll1 = 0
	
	global LHandpitch1
	LHandpitch1 = 0
	global LHandyaw1
	LHandyaw1 = 0
	global LHandroll1
	LHandroll1 = 0
	
global s
global pressed
if starting:
	pressed = 0
	vive_init()
	s = 1
	hydra_init()
	

if s == 1:
	vive_controller()
