import psutil
import winsound
import time

BATTERY_LOWER_LIMIT = 45
BATTERY_UPPER_LIMIT = 65

mins = 0

while True:
	battery = psutil.sensors_battery()
	plugged = battery.power_plugged
	percent = battery.percent
	if plugged == False and percent <= BATTERY_LOWER_LIMIT:
		winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
		print("\nPLUG IN YOUR LAPTOP   |   " + str(percent) + '%' + ' '*10)
	elif plugged == True and percent >= BATTERY_UPPER_LIMIT:
		winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
		print("\nUNPLUG NOW   |   "  + str(percent) + '%' + ' '*10)
	else:
		if plugged == True:
			print ('\r' + str(mins) + ' minutes since plugged in.' + ' '*5),
		else:
			print ('\r' + str(mins) + ' minutes since unplugged. ' + ' '*5),
	time.sleep(60)
	mins += 1