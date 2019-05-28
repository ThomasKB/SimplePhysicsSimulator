import pyglet as pt
from pyglet.gl import *
from math import pi, sin, cos

class Mass:


window = pt.window.Window()
label = pt.text.Label('Hello World',x=10,y=10)

@window.event
def on_draw():
    window.clear()
    label.draw()
    draw_circle()

def draw_circle(mass: Mass):
    iterations = int(2*1*pi)
    s = sin(2*pi / iterations)
    c = cos(2*pi / iterations)

    dx, dy = 1, 0

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(100, 100)
    for i in range(iterations+1):
        glVertex2f(100+dx, 100+dy)
        dx, dy = (dx*c - dy*s), (dy*c + dx*s)
    glEnd()

if __name__ == '__main__':
    pt.app.run()
