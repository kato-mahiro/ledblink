from gpiozero import LED
import time

led=LED(17)

try:
	while True:
		print("LED ON!")
		led.on()
		time.sleep(1)

		print("LED OFF!")
		led.off()
		time.sleep(1)

except KeyboardInterrupt:
	print("end")
finally:
	led.close()
