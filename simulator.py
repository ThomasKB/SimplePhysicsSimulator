import pyglet as pt
from pyglet.gl import *
from math import pi, sin, cos, ceil
WEIGHT_MAX = 20
WEIGHT_SCALAR = 1000
window = pt.window.Window()

class Mass:
    def __init__(self,radius,x,y):
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.radius = int(min(WEIGHT_MAX,max(0,radius)))
        self.weight = radius*WEIGHT_SCALAR
        self.x,self.y = int(x),int(y)

    def __draw__(self):
        iterations = int(2*self.radius*pi)
        s = sin(2*pi / iterations)
        c = cos(2*pi / iterations)

        dx, dy = self.radius, 0

        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(self.x, self.y)
        for i in range(iterations+1):
            glVertex2f(self.x+dx, self.y+dy)
            dx, dy = (dx*c - dy*s), (dy*c + dx*s)
        glEnd()

    def __update__(self,fx,fy):
        self.ax = fx/self.weight
        self.vx += self.ax
        self.x += self.vx

        self.ay = fy/self.weight
        self.vy += self.ay
        self.y += self.vy

mass = Mass(2, 10,400)
mass2 = Mass(5, 10,250)

@window.event
def on_draw():
    window.clear()
    mass.__update__(1,-9.82*mass.weight)
    mass2.__update__(1,-9.82*mass2.weight)
    mass.__draw__()
    mass2.__draw__()
def call_on_draw(args): on_draw()

if __name__ == '__main__':
    pyglet.clock.schedule_interval(call_on_draw, 1/10)
    pt.app.run()
