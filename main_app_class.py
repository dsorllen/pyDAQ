import tkinter as tk
from close_app import CloseFrame
from plot_frame import PlotFrame
from temperatures_frame import TempFrame

class MainApp(tk.Tk):
    def __init__(self,title, daq, *ipcs):
        super().__init__()
        self.title = title
        self.daq = daq
        self.ipcs = ipcs

        # Frame creation for the EXIT button
        self.close_frame =  CloseFrame(self)

        # Frame creation for temperature monitoring
        # self.temp_frame = PlotFrame(self, 'Temperature [\u00B0C]')
        self.temp_frame = TempFrame(self)

        # Frame creation for Ion Pump current monitoring plot
        self.current_frame = PlotFrame(self, 'Current [A]')
        self.current_frame.log_axis()

    def close_devices(self):
        self.daq.close()
        for ipc in self.ipcs:
            ipc.close_serial()
