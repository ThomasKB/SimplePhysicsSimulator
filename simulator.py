import pyglet as pt
from pyglet.gl import *
from math import pi, sin, cos

#Mass
class Mass:
    def __init__(self,weight,x,y):
        self.weight = int(min(50,max(0,weight)))
        self.x,self.y = int(x),int(y)

    def __draw__(mass: Mass):
        iterations = int(2*weight*pi)
        s = sin(2*pi / iterations)
        c = cos(2*pi / iterations)

        dx, dy = 1, 0

        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(x, y)
        for i in range(iterations+1):
            glVertex2f(x+dx, y+dy)
            dx, dy = (dx*c - dy*s), (dy*c + dx*s)
        glEnd()

window = pt.window.Window()
label = pt.text.Label('Hello World',x=10,y=10)

@window.event
def on_draw():
    window.clear()
    label.draw()
    draw_circle()



if __name__ == '__main__':
    pt.app.run()
