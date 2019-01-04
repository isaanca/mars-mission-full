# THIS IS THE ANSWER KEY FOR THE MARS MISSION PROJECT -- DO NOT READ IF YOU ARE
# NOT FINISHED. This is not the only correct answer, there are many ways to
# solve the challenge.

# Imports everything from the Tkinter library.
import Tkinter

# The next four lines of code are constants that we will use throughout the rest
# of the file, as they don't change unless you, the programmer, want them to
# based on your particular version of the game.

# This adjusts the size of your Tkinter window. You can change this based on
# your preferences and device, although we recommend that the width is a minimum
# of 200.
WIDTH = 300
HEIGHT = 700
# This changes how fast the spaceship falls.
GRAVITY = 0.65
# This changes how quickly the canvas re-draws itself, which also affects how
# often the program updates (and reacts to) user changes.
DELAY = 75

# Creating the Spaceship class
class Spaceship:
    # This is the constructor of the Spaceship class. It is called every time
    # that there is a new instance of this class, and it takes 4 arguments, the
    # initial x-position, the initial y-position, the initial x-velocity, and
    # the initial y-velocity. Additionally, the constructor takes the argument
    # "self", which is how it will refer to itself, a specific instance of the
    # class. Self shows that the fields given are for that instance rather than
    # the class in general.
    def __init__(self, x, y, x_vel, y_vel):
        # This contains 5 fields: the x-position, the y-position, the
        # x-velocity, the y-velocity, and whether or not the user is allowed to
        # continue playing. These are set to the arguments given when the class
        # is created (or the arguments listed above).
        self.x_pos = x
        self.y_pos = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        # The game state is set to true, to show that the user is allowed to be
        # playing the game.
        self.game_state = True

    # This function ensures that the game stops when the user loses, the
    # spaceship never leaves the given window, the changed velocity has an
    # effect on the position of the spaceship, and that gravity changes the
    # velocity so that the spaceship will float down. This takes the arguments
    # of height and width, which are given when the function is called. When
    # called by the draw function below,
    # these arguments are the same as the constants above.
    def update(self, HEIGHT, WIDTH):
        # This checks if the y-position is equal to the height, or if the
        # spaceship has reached the bottom of the window (the origin is the top
        # left corner). If so, the game state is set to false, so pressing the
        # arrow keys has no effect and the speed in both directions is zero.
        if self.y_pos == HEIGHT:
            self.game_state = False
            # Since the origin is the top left corner, the height is the bottom
            # of the screen, where we want the spaceship to land.
            self.y_pos = HEIGHT
            self.x_vel = 0
            self.y_vel = 0
        # This ensures that any changes below only happen if the instance's
        # field game_state is True, meaning the user is allowed to keep playing.
        if self.game_state:
            # This is where the x and y velocities that will be changed below
            # have an effect, since the x and y positions are increased by the
            # velocities.
            self.x_pos += self.x_vel
            self.y_pos += self.y_vel
            # This ensures that the spaceship does not go beyond the boundaries
            # of the screen, resetting it to the last location if it moves too
            # far.
            if self.y_pos > HEIGHT:
                self.y_pos = HEIGHT
            elif self.y_pos < 0:
                self.y_pos = 0
            if self.x_pos > WIDTH:
                self.x_pos = WIDTH
            elif self.x_pos < 0:
                self.x_pos = 0
            # This is where we use the gravity constant from above. The
            # y-velocity increases (since the positive direction for y is down),
            # so that the spaceship naturally falls to the ground.
            self.y_vel += GRAVITY

    # When this function is called, it will first check if the user is allowed
    # to play, and then will decrease the y speed, or make it go upwards (since
    # the origin is the top left corner). This function also takes in the
    # argument event, since the bind that calls it automatically passes this.
    def accelerate_y(self, event):
        if player.game_state:
            self.y_vel -= 2

    # This is similar to the function above, except instead it decreases the x
    # speed, making the spaceship move left.
    def accelerate_x_neg(self, event):
        if player.game_state:
            self.x_vel -= 2

    # Also similar to the previous two functions, but it increases the x speed,
    # moving the sapeceship to the right.
    def accelerate_x_pos(self, event):
        if player.game_state:
            self.x_vel += 2

    # This is the function that actually draws our spaceship. We used the
    # create_polygon function, although you are free to draw whatever spaceship
    # you wish.
    def draw(self, canvas):
        canvas.create_polygon(self.x_pos, self.y_pos-20, self.x_pos-20,
            self.y_pos+20, self.x_pos+20, self.y_pos+20, fill="red", outline="")

# This function is no longer a function of the class spaceship. It is a callback
# function; it is constantly recalling itself, and basically runs the entire
# program by re-drawing the window, which is explained further below.
def draw(canvas):
    # This deletes everything that is currently on the window.
    canvas.delete(Tkinter.ALL)
    # This calls the update function that is in our Spaceship class. The
    # instance of this class, player, is created below, which is why player is
    # before the draw function. It gives the constants from the beginning of the
    # program as arguments. Just a reminder, this creates gravity, ends the
    # game, and/or moves the spaceship's position.
    player.update(HEIGHT, WIDTH)
    # This uses the draw function from the spaceship class, which draws the
    # spaceship.
    player.draw(canvas)
    # These are Tkinter functions that will display the y position and the
    # speeds in both directions. We used the height minus the y position as the
    # altitude to be more intuitive for the user, since the origin is in the top
    # left corner, although we thought that when reaching the bottom of the
    # screen the altitude should be zero.
    canvas.create_text(WIDTH-180, 20, text="ALTITUDE: "
        +str(HEIGHT-player.y_pos), fill='white', width=170)
    canvas.create_text(WIDTH-180, 40, text="HORIZONTAL SPEED: "
        +str(player.x_vel), fill='white', width=170)
    canvas.create_text(WIDTH-180, 60, text="VERTICAL SPEED: "
        +str(player.y_vel), fill='white', width=170)
    # This is Tkinter's after function, which after a given time calls the
    # function in the argument. The argument DELAY (the constant given above),
    # is the time until it calls itself again, and the argument draw specifies
    # which function is being called. Canvas is also an argument since it is an
    # argument of the draw function.
    canvas.after(DELAY, draw, canvas)

# The Tk class from the Tkinter library is an object which can hold graphical
# elements called widgets. It is the root of our Tkinter window.
root = Tkinter.Tk()

# The Canvas class is a widget that allows us to draw shapes. This is where it
# is convenient to have already defined our height and width. It also takes in
# the root window as an argument.
canvas = Tkinter.Canvas(root, width=WIDTH, height=HEIGHT, background="black")

# This is the pack method, which is used to fit the canvas window to the root
# and ensure that it has the correct dimensions.
canvas.pack()

# Creates a new instance of the Spaceship class in the middle of the screen. The
# fields were previously designated by us: x and y coordinates (which are in
# relation to the dimensions of the canvas), and x and y velocity
player = Spaceship(WIDTH/2, HEIGHT/2, 0, 1)

# These methods bind key presses to certain functions. In this case, the methods
# accelerate_x_neg and accelerate_x_pos are bound to the left and right arrow
# keys, meaning that they will be called whenever the respective keys are
# pressed.
root.bind('<Left>', player.accelerate_x_neg)
root.bind('<Right>', player.accelerate_x_pos)
# Similarly, the up arrow is bound to the accelerate_y method, causing the
# player to accelerate upwards whenever the up arrow is pressed.
root.bind('<Up>', player.accelerate_y)

# Calls the draw loop for the first time. From here it will repeatedly call
# itself.
draw(canvas)

# Keeps the Tkinter window open.
root.mainloop()
