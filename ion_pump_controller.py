# Class IPController creates an object representing an Ion Pump Controller.
import serial
from pyipcmini.functions import IonPump

class IPController:
    def __init__(self, label, port):
        # Display name/label of this IPC
        self.label = label
        # USB port - COM3/COM4 - Check in Device Manager
        self.port = port

        self.serial_conn = serial.Serial(port=self.port,
                                    baudrate=9600,
                                    parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_ONE,
                                    bytesize=serial.EIGHTBITS)
        self.serial_conn.timeout = 1
        self.serial_conn.flushInput()
        self.ipc = IonPump(serial_connection=self.serial_conn)

    def get_current(self):
        return self.ipc.read_functions.read_current_measured()

    def get_pressure(self):
        return self.ipc.read_functions.read_pressure()

    def close_serial(self):
        self.serial_conn.close()
