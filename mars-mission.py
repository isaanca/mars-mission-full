import Tkinter
# import keyboard
WIDTH = 400
HEIGHT = 600
GRAVITY = -0.5
DELAY = 100

class Spaceship:
    def __init__(self, x, y, x_vel, y_vel):
        self.x_pos = x
        self.y_pos = y
        self.x_vel = x_vel
        self.y_vel = y_vel

    def update(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel
        if self.y_pos > 600:
            self.y_pos = 600
        elif self.y_pos < 0:
            self.y_pos = 0
        self.y_vel += 0.5

    def accelerate(self):
        self.y_vel -= 2

    def draw(self, canvas):
        canvas.create_polygon(self.x_pos, self.y_pos-20, self.x_pos-20, self.y_pos+20,
            self.x_pos+20, self.y_pos+20, fill="red", outline="")

def draw(canvas):
    canvas.delete(Tkinter.ALL)
    player.update()
    player.draw(canvas)
    canvas.after(DELAY, draw, canvas)

def accelerate(event):
    player.accelerate()

game_state = True
root = Tkinter.Tk()
root.bind('<space>', accelerate)
canvas = Tkinter.Canvas(root, width=WIDTH, height=HEIGHT, background="black")
canvas.pack()

player = Spaceship(WIDTH/2, HEIGHT/2, 0, 1)
draw(canvas)

root.mainloop()
