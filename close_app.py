# Class CloseFrame creates a FRAME object that hosts the EXIT button
# The EXIT button ensures closing all windows and connections to devices.

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

def close_app(window):
    plt.close('all')
    window.destroy()

class CloseFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(anchor = 'e')

        # Button settings
        btn_text = 'EXIT'
        btn_width = 10
        btn_color = 'red'
        btn_fontsize = 12
        # Button creation
        a_button = tk.Button(self,
                             text=btn_text,
                             command=lambda: close_app(parent) ,
                             width=btn_width)
        # Button positioning
        a_button.pack(anchor='e')
        # Button configuration
        a_button.config(bg=btn_color)
        a_button.config(font=btn_fontsize)