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
