
import pyvisa
from aux_functions import temp_2_float

class DAQ973A:
    def __init__(self, ip, sensors):
        self.ip = ip
        self.sensors = sensors
        self._inst = None

    def connect(self):
        try:
            rm = pyvisa.ResourceManager()
            self._inst = rm.open_resource(f'TCPIP0::{self.ip}::inst0::INSTR')
            print(self._inst.query("*IDN?"))
        except Exception as exception:
            print(exception)

    def acquire_temps(self):
        # String listing all sensor channels.
        ch_list = '@'
        temps = []  # empty list to have the temperature of each channel
        for sensor in self.sensors:
            ch = sensor.channel
            ch_list = ch_list + f'10{ch},'
        temps_acquired = self._inst.query(f'MEAS:TEMP:FRTD? 100,({ch_list[:-1]})')
        for t in temps_acquired.split(','):
            result = temp_2_float(t)  # Changes the format
            temps.append(result)
        return temps

class TemperatureSensor:
    sensors_created = []
    def __init__(self, label, channel, alarm):
        self.label = label
        self.channel = channel
        self.alarm = alarm
        TemperatureSensor.sensors_created.append(self)
