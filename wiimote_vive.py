diagnostics.watch(leap.rightpitch)
diagnostics.watch(leap.rightyaw)
diagnostics.watch(leap.rightroll)
diagnostics.watch(leap.rightxpos)
diagnostics.watch(leap.rightypos)
diagnostics.watch(leap.rightzpos)

diagnostics.watch(leap.leftpitch)
diagnostics.watch(leap.leftyaw)
diagnostics.watch(leap.leftroll)
diagnostics.watch(leap.leftxpos)
diagnostics.watch(leap.leftypos)
diagnostics.watch(leap.leftzpos)

diagnostics.watch(leap.typekeytapgesture)


hydra[1].yaw = leap.rightyaw
hydra[1].pitch = leap.rightpitch
hydra[1].roll = -leap.rightroll
hydra[1].x = filters.mapRange(leap.rightxpos, 0, 1, -1000,1000)
hydra[1].y = filters.mapRange(leap.rightypos, 0, 1, -1000,1000)
hydra[1].z = filters.mapRange(leap.rightzpos, 0, 1, -1000,1000)



hydra[0].yaw = wiimote[0].ahrs.yaw
hydra[0].pitch = wiimote[0].ahrs.pitch
hydra[0].roll = -wiimote[0].ahrs.roll
hydra[0].x = filters.mapRange(leap.leftxpos, 0, 1, -1000,1000)
hydra[0].y = filters.mapRange(leap.leftypos, 0, 1, -1000,1000)
hydra[0].z = filters.mapRange(leap.leftzpos, 0, 1, -1000,1000)

hydra[0].trigger = wiimote[0].buttons.button_down(WiimoteButtons.B)
hydra[1].trigger = leap.typekeytapgesture

Lone = wiimote[1].buttons.button_down(WiimoteButtons.DPadUp) or wiimote[1].buttons.button_down(WiimoteButtons.DPadDown) or wiimote[1].buttons.button_down(WiimoteButtons.DPadLeft) or wiimote[1].buttons.button_down(WiimoteButtons.DPadRight)
Lfour = wiimote[1].buttons.button_down(WiimoteButtons.Plus)
Lstart = wiimote[1].buttons.button_down(WiimoteButtons.Home)
Lbumper = wiimote[1].buttons.button_down(WiimoteButtons.A)

hydra[1].one = Lone
hydra[1].four = Lfour
hydra[1].start = Lstart
hydra[1].bumper = Lbumper
hydra[1].joybutton = Lone
if wiimote[1].buttons.button_down(WiimoteButtons.DPadRight):
	hydra[1].joyx = 1
elif wiimote[1].buttons.button_down(WiimoteButtons.DPadLeft):
	hydra[1].joyx = 0
if wiimote[1].buttons.button_down(WiimoteButtons.DPadUp):
	hydra[1].joyy = 1
elif wiimote[1].buttons.button_down(WiimoteButtons.DPadDown):
	hydra[1].joyy = 0
	
Rone = wiimote[0].buttons.button_down(WiimoteButtons.DPadUp) or wiimote[0].buttons.button_down(WiimoteButtons.DPadDown) or wiimote[0].buttons.button_down(WiimoteButtons.DPadLeft) or wiimote[0].buttons.button_down(WiimoteButtons.DPadRight)
Rfour = wiimote[0].buttons.button_down(WiimoteButtons.Plus)
Rstart = wiimote[0].buttons.button_down(WiimoteButtons.Home)
Rbumper = wiimote[0].buttons.button_down(WiimoteButtons.A)

hydra[0].one = Rone
hydra[0].four = Rfour
hydra[0].start = Rstart
hydra[0].bumper = Rbumper
hydra[0].joybutton = Rone
if wiimote[0].buttons.button_down(WiimoteButtons.DPadRight):
	hydra[0].joyx = 1
elif wiimote[0].buttons.button_down(WiimoteButtons.DPadLeft):
	hydra[0].joyx = 0
if wiimote[0].buttons.button_down(WiimoteButtons.DPadUp):
	hydra[0].joyy = 1
elif wiimote[0].buttons.button_down(WiimoteButtons.DPadDown):
	hydra[0].joyy = 0