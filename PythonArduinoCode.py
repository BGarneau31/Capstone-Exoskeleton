import time

import serial

arduino = serial.Serial(port='port', baudrate=000, timeout=.1)  # update port and baudrate
time.sleep(1)


class PythonArduino(arduino):
    def __init__(self):
        self.arduino = arduino
        self.data = None

    def receive_data(self):
        while True:
            self.data = arduino.readline()[:-2]  # end bit get rid of new line arduino characters
            if self.data:
                return self.data


python_arduino_connect = PythonArduino()
python_arduino_connect.receive_data()

# # Now we can write a simple script that sends data from Python to the Arduino, and then prints out what it gets back.
# import serial, time
# arduino = serial.Serial('COM1', 115200, timeout=.1)
# time.sleep(1) #give the connection a second to settle
# arduino.write("Hello from Python!")
# while True:
# 	data = arduino.readline()
# 	if data:
# 		print data.rstrip('\n') #strip out the new lines for now
# 		# (better to do .read() in the long run for this reason
