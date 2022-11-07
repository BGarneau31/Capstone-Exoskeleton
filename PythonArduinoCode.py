import time
import serial

# arduino = serial.Serial(port='port', baudrate=000, timeout=.1)  # update port and baudrate
# time.sleep(1)
#
#
# class PythonArduino(arduino):
#     def __init__(self):
#         self.arduino = arduino
#         self.data = None
#
#     def receive_data(self):
#         while True:
#             self.position_data = arduino.readline()[:-2]  # end bit get rid of new line arduino characters
#             if self.data:

#                 return self.data
#
#     def send_command(self, python_command):
#         data_from_python = python_command
#         arduino.write(data_from_python)  # arduino takes this data to update the motor to correct position


# python_arduino_connect = PythonArduino()
# python_arduino_connect.receive_data()
# python_arduino_connect.send_data()  # this will be imported into main and called in GUI with specifics when needed


class TestFakeArduino:

    def __init__(self):
        self.code = None

    def receive_data(self):
        # read arduino data
        # return data
        return 1, 2, 3

    def send_data(self, python_data):
        # send arduino data command
        data_from_python = python_data
        print(data_from_python)
