from System import Int16
from ctypes import windll, Structure, c_ulong, byref

if starting:
		vJoy[0].x = 0
		vJoy[0].y = 0
		autocpeed = 30 #update rate (5-75 seems best)
		joynum = 0 #blend in your joystick/gamepad. Change the number if you multiple controllers to get the one you want
		system.setThreadTiming(TimingTypes.HighresSystemTimer)
		system.threadExecutionInterval = autocpeed
		kbmousesense = 1500 # mouse reponsiveness with keyboard press
		mousesense = 500 # general mouse reponsiveness 
		joystick[joynum].setRange(Int16.MinValue, Int16.MaxValue,)


		
#mousewheel throttle, mwheel down is 50 percent throttle, mwheel up is full and 0 throttle is any key of your choosing,
#by default it is numberpad slash

if mouse.wheelUp:
	vJoy[0].z = Int16.MaxValue
      
if mouse.wheelDown:
	vJoy[0].z = 0

if keyboard.getKeyDown(Key.NumberPadSlash):
	vJoy[0].z = Int16.MinValue

# remove '#' to enable middle mouse button as 0 throttle and delete or hastag 'vJoy[0].setButton(2, mouse.middleButton)'
#so there are no conflicts

#if mouse.middleButton:
#	vJoy[0].z = Int16.MinValue


#xbox controller mode clashes with the game so ignore this for now
#vJoy[0].x = (xbox360[0].leftStickX * 17000) + (mouse.deltaX*mousesense)
#vJoy[0].y = (xbox360[0].leftStickY * -17000) + (mouse.deltaY*mousesense)


#right button roll like in the original games where mouse becomes an analogue roll temporarily
if mouse.rightButton:
	vJoy[0].rz = mouse.deltaX*mousesense #mouse axis is now roll while right button down
	vJoy[0].y = mouse.deltaY*mousesense
else:
	vJoy[0].x = (joystick[joynum].x / 1.7) + (mouse.deltaX*mousesense)
	vJoy[0].y = (joystick[joynum].y / 1.7) + (mouse.deltaY*mousesense)
	vJoy[0].rz = 0



vJoy[0].setButton(0, mouse.leftButton)
vJoy[0].setButton(1, mouse.rightButton)
vJoy[0].setButton(2, mouse.middleButton)

   
if keyboard.getKeyDown(Key.UpArrow):
	vJoy[0].y = -Int16.MaxValue + (mouse.deltaY*kbmousesense)
	
if keyboard.getKeyDown(Key.DownArrow):
	vJoy[0].y = Int16.MaxValue + (mouse.deltaY*kbmousesense)

if keyboard.getKeyDown(Key.LeftArrow):
	vJoy[0].x = -Int16.MaxValue + (mouse.deltaX*kbmousesense)
	
if keyboard.getKeyDown(Key.RightArrow):
	vJoy[0].x = Int16.MaxValue + (mouse.deltaX*kbmousesense)

diagnostics.watch(xbox360[0].leftStickY)
diagnostics.watch(xbox360[0].leftStickX)
diagnostics.watch(vJoy[0].x)
diagnostics.watch(vJoy[0].y)
diagnostics.watch(mouse.deltaY)
diagnostics.watch(mouse.deltaX)
diagnostics.watch(joystick[joynum].x)
diagnostics.watch(joystick[joynum].y)
