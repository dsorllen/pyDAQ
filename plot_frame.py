import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk

# Number of visible measurements in the live plot
# N_visible = 20

class PlotFrame(ttk.Frame):
    def __init__(self, parent, magnitude):
        super().__init__(parent)
        self.pack()
        self._height = 4
        self._length = 8
        self.magnitude = magnitude

        self.fig = plt.figure(figsize=(self._length,self._height))
        self.ax = self.fig.gca()
        self.ax.set_xlabel('Timestamp')
        self.ax.set_ylabel(f'{self.magnitude}')
        self.ax.grid()

        canvas = FigureCanvasTkAgg(self.fig, master= self)
        canvas.get_tk_widget().pack()
        self.pack()

    def log_axis(self):
        self.ax.set_yscale('log')



# # Variables
# time_stamps = []
# currents = []
#
# # Empty line to be filled with data from the IPC
# line1, = ax.plot([], [], 'g.-', label="Current")
#
#
# # Loop to acquire data
# try:
#     while True:
#         now = dt.datetime.now()
#         time_stamps.append(now)
#         currents.append(vac1.get_current())
#
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