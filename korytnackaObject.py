#!/usr/bin/python3

from math import cos, sin, pi


class Kora:
    def __init__(self, c):
        self.home(c)

    def left(self, du):
        self.angle = (self.angle + du) % 360

    def right(self, du):
        self.angle = (self.angle - du) % 360

    def changePC(self, pc):
        self.color = pc

    def changeHP(self, hp):
        self.hp = hp

    def erase(self):
        self.c.delete("all")

    def home(self, c):
        self.c = c
        self.x = int(c['width']) / 2
        self.y = int(c['height']) / 2
        self.pendown = True
        self.hp = 1
        self.color = 'black'
        self.angle = 90

    def fwd(self, dist):
        nx = self.x + dist * cos(self.angle * pi / 180)
        ny = self.y - dist * sin(self.angle * pi / 180)
        if self.pendown:
            self.c.create_line(self.x, self.y, nx, ny, fill=self.color, width=self.hp)
        self.x = nx
        self.y = ny
