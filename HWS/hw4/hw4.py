"""
Tara Walton // tara1984
HW 4 - Due 04/08/15

Description: GUI using mouse and keyboard events. Program will draw a circle with r=50 pixels
    expandable with the frame. Program will respond to mouse and keyboard events.
    Mouse click - message centered in circle states if mouse click is in/out of circle
    arrow keys - move circle 5 pixels in appropriate direction
    
Output: GUI
"""
from tkinter import *

class Circle(Frame):
    """creates a class of circle, movable and able to interact by mouse and keyboard"""
    def __init__(self):
        '''set up window and widgets'''
        Frame.__init__(self)
        self.master.title("Special Events")
        #self.master.resizable(1, 1) #default setting
        self.master.geometry("200x200")
        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.grid(sticky = N+S+E+W)
        
        self._x = 100 #starting x-center point for default sizing
        self._y = 100 #starting y-center point for default sizing
        
        #set canvas
        self.canvas = Canvas(self, bg = "white")
        self.canvas.grid(row = 0, column = 0)
        self.canvas.pack(fill = BOTH, expand = True)  #from google
        
        #draw circle (radius 50)
        self.canvas.create_oval(self._x - 50, self._y - 50,
                                self._x + 50, self._y + 50, tags = "circle")

        #bind with mouse events
        self.canvas.bind("<Button-1>", self.insideCircle)
    
        #bind with keyboard events
        self.canvas.focus_set()
        self.canvas.bind("<Key>", self.moveCircle)

    def insideCircle(self, event):
        '''defines position of cursor as inside/outside circle'''
        import math
        distance = math.sqrt((self._x - event.x)**2 + (self._y - event.y)**2)
        if distance <= 50:
            self.displayString("inside")
        if distance > 50:
            self.displayString("outside")

    def displayString(self, position):
        '''creates string in the center of the circle'''
        self.canvas.delete("string")
        if position == "inside":
            self.canvas.create_text(self._x, self._y, text = "Mouse pointer is INSIDE the circle",
                                    font = "Arial 8", tags = "string",
                                    fill = self.getRandomColor())
        if position == "outside":
            self.canvas.create_text(self._x, self._y, text = "Mouse pointer is OUTSIDE the circle",
                                    font = "Arial 8", tags = "string",
                                    fill = self.getRandomColor())

    def moveCircle(self, event):
        '''move circle up, down, left or right when user clicks an arrow key'''
        self.canvas.delete("string")
        if event.keysym == "Up":
            self.canvas.move("circle", 0, -5)
            self._y -= 5
        elif event.keysym == "Down":
            self.canvas.move("circle", 0, 5)
            self._y += 5
        elif event.keysym == "Left":
            self.canvas.move("circle", -5, 0)
            self._x -= 5
        elif event.keysym == "Right":
            self.canvas.move("circle", 5, 0)
            self._x += 5

    #Random color code from Dr. Jamil Saquer
    def getRandomColor(self):
        """ Generates and returns a random color string such as '#c2f74a'"""
        digits = "0123456789abcdef"
        color = "#"
        from random import randint
        for i in range(6):
            randomIndex = randint(0, 15)
            color += digits[randomIndex]
        return color

def main():
    Circle().mainloop()

main()
