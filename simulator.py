import pyglet as pt
from pyglet.gl import *
from math import pi, sin, cos, ceil, sqrt, atan
WEIGHT_MAX = 20
WEIGHT_SCALAR = 1000
GRAV_CONSTANT = 6.67408e-11
window = pt.window.Window()

dist = lambda m1, m2 : sqrt((m2.x-m1.x)**2+(m2.y-m1.y)**2)
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

mass = Mass(1, 100, 260)
mass2 = Mass(10, 100, 250)

@window.event
def on_draw():
    window.clear()
    attract_x,attract_y = calc_attraction(mass,mass2)
    mass.__update__(attract_x,attract_y)
    mass2.__update__(0,0)
    print(attract_x,attract_y)
    mass.__draw__()
    mass2.__draw__()
def call_on_draw(args): on_draw()

def calc_attraction(mass,masses):
    if masses.x == mass.x:
        theta = 270
    else:
        theta = atan((masses.y-mass.y)/(masses.x-mass.x))
    v = GRAV_CONSTANT*mass.weight*masses.weight/dist(mass,masses)**2
    vx = v*cos(theta)
    vy = v*sin(theta)
    return vx,vy
if __name__ == '__main__':
    pyglet.clock.schedule_interval(call_on_draw, 1/40)
    pt.app.run()
