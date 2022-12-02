import time
import serial


# arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)  # update port and baudrate
# time.sleep(1)
#
# class PythonArduino:
#
#     def __init__(self):
#         self.position_data = None
#
#     def receive_data(self):
#         # read arduino data
#         # return data as string to print to console to show tech that motor is finished with command and in position
#
#         self.position_data = arduino.readline()[:-2]  # end bit get rid of new line arduino characters
#         return self.position_data
#
#     def send_data(self, python_data):
#         # send arduino data command
#         data_from_python = python_data
#         arduino.write(data_from_python.encode())
#         print(data_from_python)


# Fake data for testing GUI without arduino connection:

class PythonArduino:

    def __init__(self):
        self.position_data = None

    def receive_data(self):
        return 1

    def send_data(self, python_data):
        # send arduino data command
        data_from_python = python_data
        print(data_from_python)
