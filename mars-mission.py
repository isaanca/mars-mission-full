import Tkinter
import math

WIDTH = 300
HEIGHT = 700
GRAVITY = 0.8
DELAY = 100

class Spaceship:
    def __init__(self, x, y, x_vel, y_vel):
        self.x_pos = x
        self.y_pos = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.game_state = True

    def update(self, HEIGHT, WIDTH):
        if self.y_pos == HEIGHT:
            self.game_state = False
            self.y_pos = HEIGHT
            self.x_vel = 0
            self.y_vel = 0
        if self.game_state:
            self.x_pos += self.x_vel
            self.y_pos += self.y_vel
            if self.y_pos > HEIGHT:
                self.y_pos = HEIGHT
            elif self.y_pos < 0:
                self.y_pos = 0
            if self.x_pos > WIDTH:
                self.x_pos = WIDTH
            elif self.x_pos < 0:
                self.x_pos = 0
            self.y_vel += GRAVITY

    def accelerate_y(self):
        if player.game_state:
            self.y_vel -= 2

    def accelerate_x_neg(self):
        if player.game_state:
            self.x_vel -= 2

    def accelerate_x_pos(self):
        if player.game_state:
            self.x_vel += 2

    def draw(self, canvas):
        canvas.create_polygon(self.x_pos, self.y_pos-20, self.x_pos-20, self.y_pos+20,
            self.x_pos+20, self.y_pos+20, fill="red", outline="")

def draw(canvas):
    canvas.delete(Tkinter.ALL)
    player.update(HEIGHT, WIDTH)
    player.draw(canvas)
    canvas.create_text(WIDTH-180, 20, text="ALTITUDE: "+str(HEIGHT-player.y_pos), fill='white', width=170)
    canvas.create_text(WIDTH-180, 40, text="HORIZONTAL SPEED: "+str(player.x_vel), fill='white', width=170)
    canvas.create_text(WIDTH-180, 60, text="VERTICAL SPEED: "+str(player.y_vel), fill='white', width=170)
    canvas.after(DELAY, draw, canvas)

def accelerate_y(event):
    player.accelerate_y()

def accelerate_x_neg(event):
    player.accelerate_x_neg()

def accelerate_x_pos(event):
    player.accelerate_x_pos()

root = Tkinter.Tk()
canvas = Tkinter.Canvas(root, width=WIDTH, height=HEIGHT, background="black")
canvas.pack()

player = Spaceship(WIDTH/2, HEIGHT/2, 0, 1)
root.bind('<Left>', accelerate_x_neg)
root.bind('<Right>', accelerate_x_pos)
root.bind('<Up>', accelerate_y)
draw(canvas)

root.mainloop()
