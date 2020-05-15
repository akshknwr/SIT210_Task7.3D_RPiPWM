import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

ECHO=11
Trig=7
LED =33
GPIO.setup(LED,GPIO.OUT)
brightness =0 #initialise the brightness with 0
myLED=GPIO.PWM(33,100)
myLED.start(0)


def updateDistance():
	GPIO.setup(Trig,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)
	GPIO.output(Trig,GPIO.LOW)
	
	time.sleep(0.2)
	
	GPIO.output(Trig,GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(Trig,GPIO.LOW)
	while GPIO.input(ECHO)==0:
		pulse_start = time.time()
	while GPIO.input(ECHO)==1:
		pulse_end= time.time()
	pulse_duration= pulse_end - pulse_start
	distance = round(pulse_duration * 17150, 2)
	print("distance: ",distance,"cm")
	return distance
	
def adjustLEDBrightness(distance):

	global brightness 
	print("brightness ",brightness)
	global myLED
	pauseTime=0.010
	if (distance <= 5) :
		brightness = 100 
	elif (distance > 5 and distance < 10):
		brightness =80
	elif (distance >10 and distance < 20):
		brightness =60
	elif (distance >20 and distance <50 ):
		brightness = 40
	elif (distance > 50 and distance <100):
		brightness=20
	elif (distance >100):
		brightness =0
	
	myLED.ChangeDutyCycle(brightness)
	time.sleep(0.10)
	
	

try:
  while 1:
    distance = updateDistance()
    adjustLEDBrightness(distance)
	

	
	
    
except KeyboardInterrupt:
    print("stopped")
    GPIO.cleanup()
