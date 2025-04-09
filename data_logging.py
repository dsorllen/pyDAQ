# Class LoggingFile to create an object which saves into a file measurement data.
import datetime as dt

class LoggingFile:
    def __init__(self, *labels):
        # Log file name using current date
        today = dt.datetime.now().strftime('%Y%m%d_%H-%M')
        self.filename = today + '_ipcs.dat'

        # Header creation
        header = 'Datetime,'
        for label in labels:
            header = header + label + ','

        # File creation
        with open(self.filename,'w') as f:
            f.write(header[:-1]+'\n')
        f.close()

    def write_line(self, line):
        # Adding a new line to log file
        with open(self.filename, 'a') as f:
            f.write(line[:-1] + '\n')
        f.close()