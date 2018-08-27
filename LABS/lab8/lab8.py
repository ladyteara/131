"""
Tara Walton // tara1984
Lab 8 - Due 3/26

Description: GUI that draws a rectangle and oval. Allows the user to select
    radio buttons and a check box for "filled" objects. Use nested frames to
    acheive the appropriate layout.

Output: GUI
"""
from tkinter import *
import math

class Geometry(Frame):
    """Allows the drawing of a rectangle and oval defined by user"""
    def __init__(self):
        '''Creates a window and widgets'''
        #main frame
        Frame.__init__(self)
        self.master.title("Geometry")
        self.grid()
        
        #canvas pane
        self._canvas = Canvas(self, width = 300, height = 300, bg = "white")
        self._canvas.grid(row = 0, column = 0)

        #button pane
        frame = Frame(self)
        frame.grid(row = 1, column = 0)
        
        #place buttons
        self.radVar = IntVar()
        self.rectangle = Radiobutton(frame, text = "Rectangle",
                                     command = self.displayRectangle,
                                     variable = self.radVar, value = 1)
        self.rectangle.grid(row = 0, column = 0)
        self.oval = Radiobutton(frame, text = "Oval",
                                command = self.displayOval,
                                variable = self.radVar, value = 2)
        self.oval.grid(row = 0, column = 1)
        
        self.fillVar = IntVar(value=0)
        self.fill = Checkbutton(frame, text = "Fill",
                                variable = self.fillVar)
        self.fill.grid(row = 0, column = 2)
        
        clear = Button(frame, text="Clear", command = self.clearCanvas)
        clear.grid(row = 0, column = 3)

    def fillObj(self):
        '''Re-tags geometric object's fill attribute'''
        print("Checkbutton clicked value is", self.fillVar.get())

    def displayRectangle(self):
        '''Draws a rectangle bounded by the canvas'''
        print("Rect")
        self._canvas.create_rectangle(50, 50, 250, 250, fill = "red" if self.fillVar.get()==1 else None, tags = "rect")
         
    def displayOval(self):
        '''Draws an Oval bounded by the Rectangle'''
        print("Oval")
        self._canvas.create_oval(50, 100, 250, 200, fill = "yellow" if self.fillVar.get()==1 else None, tags = "oval")

    def clearCanvas(self):
        '''clears the canvas back to white background'''   
        self.fill.deselect()
        self.radVar.set(0)
        self._canvas.delete(ALL)
         
def main():
    """Creates the pop up window"""
    Geometry().mainloop()

main()

        
