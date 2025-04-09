
import datetime as dt

from main_app_class import MainApp

from ion_pump_controller import IPController
from temperature_sensor import TemperatureSensor
from temperature_sensor import DAQ973A

# Creation of Ion Pump Controller object
# vac1 = IPController('VAC1', 'COM4')

# Creation of temperature sensors installed
window_bottom =     TemperatureSensor('Window Bottom', 1, 50)
window_right =      TemperatureSensor('Window Right', 2, 50)
window_left =       TemperatureSensor('Window Left', 3, 50)
window_top =        TemperatureSensor('Window Top', 4, 50)
harm_2nd =          TemperatureSensor('2nd Harmonic', 5, 50)
harm_3rd =          TemperatureSensor('3rd Harmonic', 6, 50)

# Combination of all sensors
temperature_sensors = TemperatureSensor.sensors_created

daq = DAQ973A('169.254.18.18', temperature_sensors)
# daq.connect()

pyDAQ = MainApp('pyDAQ')
pyDAQ.add_sensors(temperature_sensors)
pyDAQ.mainloop()




# Loop to acquire data
# try:
#     while True:
#         now = dt.datetime.now()
#         time_stamps.append(now)
#         currents.append(vac1.get_current())
# #
#         # Write data to file
#         log_line = now.strftime('%Y/%m/%d %H:%M:%S') + ','
#         log_line = log_line + f'{currents[-1]}'
#         logfile.write_line(log_line)
#
#         # Show only N items
#         if len(time_stamps) > N_visible:
#             time_stamps.pop(0)
#             currents.pop(0)
#
#         line1.set_xdata(time_stamps)
#         line1.set_ydata(currents)
#         ax.relim()
#         ax.autoscale_view()
#         fig.canvas.draw()
#         fig.canvas.flush_events()
#
#         time.sleep(0.25)
#
# except KeyboardInterrupt:
#     pass
# finally:
#     print("Program interrupted by user (ctrl+C)")
#     vac1.close_serial()
#     print("Serial connection closed")