"""
Tara Walton // tara1984

Lab 7: Due 3/19/15
Description: GUI interface for converting Celsius to Fahrenheit
"""
from tkinter import *

class Degrees(Frame):
    """creates a widget to convert Farenheit to Celsius and v/v"""
    def __init__(self):
        ''' sets up window and widgets'''
        Frame.__init__(self)
        self.master.title("Degree Conversions")
        self.grid()

        #label and field for Farenheit
        self._farenheitLabel = Label(self, text = "Farenheit")
        self._farenheitLabel.grid(row = 0, column = 0, sticky = N)
        self._farenheitVar = DoubleVar()
        self._farenheitVar.set(32.0) #default value
        self._farenheitEntry = Entry(self, justify = "center", width = 15,
                                     textvariable = self._farenheitVar)
        self._farenheitEntry.grid(row = 1, column = 0)
        
        #label and field for Celsius
        self._celsiusLabel = Label(self, text = "Celsius")
        self._celsiusLabel.grid(row = 0, column = 1, sticky = N)
        self._celsiusVar = DoubleVar()
        self._celsiusEntry = Entry(self, justify = "center", width = 15,
                                   textvariable = self._celsiusVar)
        self._celsiusEntry.grid(row = 1, column = 1)
        
        #command buttons
        self._fcButton = Button(self, text = ">>>>", command = self.getCelsius)
        self._fcButton.grid(row = 2, column = 0)
        self._cfButton = Button(self, text = "<<<<", command = self.getFarenheit)
        self._cfButton.grid(row = 2, column = 1)

    def getCelsius(self):
        farenheit = self._farenheitVar.get()
        celsius = (farenheit - 32) *(5/9)
        self._celsiusVar.set(celsius)
        
    def getFarenheit(self):
        celsius = self._celsiusVar.get()
        farenheit = celsius *(9/5) + 32
        self._farenheitVar.set(farenheit)

def main():
    Degrees().mainloop()

main()
