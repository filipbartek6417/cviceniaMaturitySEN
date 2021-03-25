from tkinter import Canvas, Tk
from math import cos, sin, pi
from re import split

main = Tk()

can = Canvas(width=600, height=600, bg='white')
can.pack()


class Robot:
    def __init__(self, c):
        self.c = c
        self.x = 300
        self.y = 300
        self.angle = 90

    def draw(self):
        nx = self.x + 50 * cos(self.angle * pi / 180)
        ny = self.y - 50 * sin(self.angle * pi / 180)
        self.c.create_line(self.x, self.y, nx, ny)
        self.x = nx
        self.y = ny

    def left(self):
        self.angle = (self.angle + 90) % 360

    def right(self):
        self.angle = (self.angle - 90) % 360


robot = Robot(can)

f = open('robot.txt', 'r')
l = f.readline()
repeatMode = False
comms = []


def evaluate(comm):
    if comm == 'ciara':
        robot.draw()
    elif comm == 'vlavo':
        robot.left()
    elif comm == 'vpravo':
        robot.right()


while l != '':
    x = split(" |\n", l)[0]
    if x == 'opakuj':
        comms = []
        repeatMode = True
        index = int(split(" |\n", l)[1])
    elif x == 'koniecopakuj':
        repeatMode = False
        for i in range(index):
            for j in comms:
                evaluate(j)
    elif repeatMode:
        comms.append(x)
    else:
        evaluate(x)
    l = f.readline()

main.mainloop()
