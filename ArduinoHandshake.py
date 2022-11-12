import time
import serial
import serial.tools.list_ports


# need to put this whole script into class
class ArduinoCode:
    pass


HANDSHAKE = 0
MOTOR_CENTER = 1
MOTOR_LEFT = 2
MOTOR_RIGHT = 3


def find_arduino(port=None):
    """Get the name of the port that is connected to Arduino."""
    if port is None:
        ports = serial.tools.list_ports.comports()
        for p in ports:
            if p.manufacturer is not None and "Arduino" in p.manufacturer:
                port = p.device
    return port


def handshake_arduino(arduino, sleep_time=1, print_handshake_message=False, handshake_code=0):
    """Make sure connection is established by sending and receiving bytes."""
    # Close and reopen
    arduino.close()
    arduino.open()

    # Chill out while everything gets set
    time.sleep(sleep_time)

    # Set a long timeout to complete handshake
    timeout = arduino.timeout
    arduino.timeout = 2

    # Read and discard everything that may be in the input buffer
    _ = arduino.read_all()

    # Send request to Arduino
    arduino.write(bytes([handshake_code]))

    # Read in what Arduino sent
    handshake_message = arduino.read_until()

    # Send and receive request again
    arduino.write(bytes([handshake_code]))
    handshake_message = arduino.read_until()

    # Print the handshake message, if desired
    if print_handshake_message:
        print("Handshake message: " + handshake_message.decode())

    # Reset the timeout
    arduino.timeout = timeout


port = find_arduino()
arduino = serial.Serial(port, baudrate=115200)
handshake_arduino(arduino, handshake_code=HANDSHAKE, print_handshake_message=True)

# with serial.Serial(port, baudrate=115200, timeout=1) as arduino:
#     handshake_arduino(arduino)
#     arduino.write(bytes([MOTOR_CENTER]))  # send code to move arduino to center position

# Ask Arduino for data - this is time and voltage but maybe it can be something else??
arduino.write(bytes([MOTOR_CENTER]))
raw = arduino.read_until()  # Receive data
raw_str = raw.decode()
print(raw_str)
t, V = raw_str.rstrip().split(",")
print(t, V)

# determine t and V of center, right, left, and full trial?
# each position determined by sensors/arduino will send unique string that can determine what GUI will show


def send_data_to_gui(raw_data):
    left = "left arduino string"
    right = "right arduino string"
    center = "center arduino string"
    if raw_data == center:
        gui_code = 0
    if raw_data == left:
        gui_code = 1
    if raw_data == right:
        gui_code = 2
    else:
        gui_code = None
    return gui_code
