from tkinter import ttk
import tkinter as tk

class TempFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack()

        self._label_fontsize = 16
        self._label_entry_width = 15
        self._pdx = 10; self._pdy = 2
        title_color = 'steel blue'

        self.temp_entries = []

        # TABLE HEADERS
        lbl_str = 'RTD Position'
        lbl = tk.Label(self, text = lbl_str, font = ('bold', self._label_fontsize))
        lbl.config(fg=title_color)
        lbl.grid(column = 0, row = 0, sticky = 'w', pady = self._pdy, padx = self._pdx)

        lbl_str = 'Measurement [\u00B0C] '
        lbl = tk.Label(self, text=lbl_str, font=('bold', self._label_fontsize))
        lbl.config(fg=title_color)
        lbl.grid(column=1, row=0, sticky='w', pady = self._pdy, padx = self._pdx)

        lbl_str = 'Alarm [\u00B0C]'
        lbl = tk.Label(self, text=lbl_str, font=('bold', self._label_fontsize))
        lbl.config(fg=title_color)
        lbl.grid(column=2, row=0, sticky='w', pady = self._pdy, padx = self._pdx)

    def create_table(self, sensors):
        row_count = 1
        for sensor in sensors:
            # Label entry
            label_e = tk.Entry(self,
                            font=('normal', self._label_fontsize - 2),
                            width= self._label_entry_width,
                            state='normal',
                            )
            label_e.grid(column=0, row=row_count, pady = self._pdy, padx = self._pdx)
            label_e.insert(0, sensor.label)
            label_e.config(state='disabled')
            ###########################################################################
            # Temperature entry
            temp_e = tk.Entry(self,
                           font=('normal', self._label_fontsize - 2),
                           width=self._label_entry_width,
                           state='normal',
                           )
            self.temp_entries.append(temp_e)
            temp_e.grid(column=1, row=row_count, pady = self._pdy, padx = self._pdx)
            ###########################################################################
            # Alarm entry
            alarm_e = tk.Entry(self,
                            font=('normal', self._label_fontsize - 2),
                            width=self._label_entry_width,
                            state='normal',
                            )
            alarm_e.grid(column=2, row=row_count, pady = self._pdy, padx = self._pdx)
            # alarm_entries.append(alarm_e)
            alarm_e.insert(0, sensor.alarm)
            alarm_e.config(state='disabled')
            ###########################################################################
            row_count = row_count + 1