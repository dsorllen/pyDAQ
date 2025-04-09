import tkinter as tk
from close_app import CloseFrame
from plot_frame import PlotFrame
from temperatures_frame import TempFrame

class MainApp(tk.Tk):
    def __init__(self,title):
        super().__init__()
        self.title = title

        self.close_frame =  CloseFrame(self)

        # self.temp_frame = PlotFrame(self, 'Temperature [\u00B0C]')
        self.temp_frame = TempFrame(self)

        self.current_frame = PlotFrame(self, 'Current [A]')
        self.current_frame.log_axis()

    def add_sensors(self, sensors):
        self.temp_frame.create_table(sensors)