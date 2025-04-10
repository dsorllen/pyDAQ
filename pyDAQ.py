
import datetime as dt

from main_app_class import MainApp
from ion_pump_controller import IPController
from temperature_sensor import TemperatureSensor
from temperature_sensor import DAQ973A
from data_logging import LoggingFile

# Acquisition rate, in seconds
update_time = 1

# Creation of Ion Pump Controller object
# ipc_label = 'VAC1'
# vac1 = IPController(ipc_label, 'COM4')
# ipc_log = LoggingFile(ipc_label, mag = 'ipc')

# Creation of temperature sensors installed
# window_bottom =     TemperatureSensor('Window Bottom', 1, 50)
window_right =      TemperatureSensor('Window Right', 2, 50)
window_left =       TemperatureSensor('Window Left', 3, 50)
window_top =        TemperatureSensor('Window Top', 4, 50)
harm_2nd =          TemperatureSensor('2nd Harmonic', 5, 50)
harm_3rd =          TemperatureSensor('3rd Harmonic', 6, 50)

# Combination of all sensors
temperature_sensors = TemperatureSensor.sensors_created

daq = DAQ973A('169.254.18.18', temperature_sensors)
daq.connect()
temp_log = LoggingFile([sensor.label for sensor in temperature_sensors], mag = 'temp')

# pyDAQ = MainApp('pyDAQ')
pyDAQ = MainApp('pyDAQ', daq)
pyDAQ.temp_frame.create_table(temperature_sensors)

def acquire():
    now = dt.datetime.now()
    # Acquire and write temperatures
    acq_temps = daq.acquire_temps()
    # print(acq_temps)
    pyDAQ.temp_frame.update_table(temperature_sensors, acq_temps)
    # Log temperature data
    logline = now.strftime('%Y/%m/%d %H:%M:%S') + ','
    for temp in acq_temps:
        logline = logline + f'{temp},'
    temp_log.write_line(logline[:-1] + '\n')

    pyDAQ.after(update_time*1000,acquire)

acquire()

pyDAQ.mainloop()
