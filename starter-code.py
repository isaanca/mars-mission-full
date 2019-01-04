# Allows us to access the classes and methods from the Tkinter library.
import Tkinter

# These are constants. A common convention is that constant variables are in
# all caps. The width and height are the dimensions of the window, in pixels.
WIDTH = 400
HEIGHT = 600

# The animation frame rate, in milliseconds
DELAY = 100

# This class creates a circle
class Circle:
    # This constructor method takes two arguments, x and y. These are the
    # coordinates of the center of the circle
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # This method is meant to run every frame, moving the circle.
    def update(self):
        self.y += 5
        # If it reaches the bottom of the screen, it wraps around to the top.
        if (self.y > 590):
            self.y = 10
    # This method draws the circle on the canvas, at its current coordinates.
    def display(self):
        canvas.create_oval(self.x-10, self.y-10, self.x+10, self.y+10,
            fill="white", outline="")

# This is a draw loop. It is a recursive function, meaning that it calls itself
# every frame.
def draw(canvas):
    # Deletes all game objects
    canvas.delete(Tkinter.ALL)

    # Moves the circle
    circle.update()
    # Redraws the circle
    circle.display()

    # Waits [DELAY] milliseconds, before calling itself, with the canvas as an
    # argument
    canvas.after(DELAY, draw, canvas)

# The Tk class from the Tkinter library is an object which can hold graphical
# elements called widgets. It is the root of our Tkinter window.
root = Tkinter.Tk()

# The Canvas class is a widget that can draw shapes.
canvas = Tkinter.Canvas(root, width=WIDTH, height=HEIGHT, background="black")

# This method fits the canvas window to the correct size.
canvas.pack()

# Creates a new Circle object
circle = Circle(200, 200)

# Starts the draw loop
draw(canvas)

# This method of Tk keeps the window open.
root.mainloop()
