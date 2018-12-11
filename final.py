import RPi.GPIO as GPIO
import time
import Adafruit_CharLCD as LCD
import os

# pin setup for lcd
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2



lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
#GPIO.setmode(GPIO.BOARD)
PIN_TRIGGER_1 = 20
PIN_ECHO_1 = 21
PIN_TRIGGER_2 = 5
PIN_ECHO_2 = 6


def reset():
	sensor1 = False
	sensor2 = False


in_counter = 0
out_counter = 0
sensor1 = False
sensor2 = False
d = 20


while True:
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(PIN_TRIGGER_1, GPIO.OUT)
	GPIO.setup(PIN_ECHO_1, GPIO.IN)
	GPIO.setup(PIN_TRIGGER_2, GPIO.OUT)
	GPIO.setup(PIN_ECHO_2, GPIO.IN)

	GPIO.output(PIN_TRIGGER_1, GPIO.LOW)
	time.sleep(0.2)
	GPIO.output(PIN_TRIGGER_1, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(PIN_TRIGGER_1, GPIO.LOW)

	while GPIO.input(PIN_ECHO_1)==0:
		 pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO_1)==1:
		 pulse_end_time = time.time()

	pulse_duration = pulse_end_time - pulse_start_time
	distance = round(pulse_duration * 17150, 2)
	lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,lcd_columns, lcd_rows, lcd_backlight)

	# when sensor 1 is hit
	if distance < d:
		#print("hit!")
		#print(distance)
		if sensor2 == True:
			out_counter = out_counter + 1
			sensor1 = False
			sensor2 = False
		else:
			sensor1 = True
		#lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
		#lcd.clear()
		#lcd.message('distance: '+str(distance))
	#time.sleep(0.2)


        GPIO.output(PIN_TRIGGER_2, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(PIN_TRIGGER_2, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER_2, GPIO.LOW)

        while GPIO.input(PIN_ECHO_2)==0:
                 pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO_2)==1:
                 pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
     	
	# when sensor 2 is hit
        if distance < d:
                #print("hit!")
                #print(distance)

		if sensor1 == True:
			in_counter = in_counter + 1
			sensor1 = False
			sensor2 = False
		else:
			sensor2 = True
                #lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
                # lcd.clear()
                #lcd.message('distance: '+str(distance))
		time.sleep(0.1)
	
	os.system('clear')
        in_out = 'in: '+ str(in_counter)+' , out: '+str(out_counter)
	sensor_state = str(sensor2)+' '+str(sensor1)
	print in_out
	print sensor_state
	lcd.message(in_out+'\n')
	passenger = in_counter - out_counter
	total = 'total: '+str(passenger)
	lcd.message(total)

	GPIO.cleanup()
	
