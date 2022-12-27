#!/usr/bin/env python3
import sys
import random

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

d = random.random()

RED_VALUE = random.random()
GREEN_VALUE = random.random()
BLUE_VALUE = random.random()

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass

def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

    # zad 1
    #draw_triangle()

    # zad 2
    #draw_rectangle(0, 0, 160, 60)

    # zad 3
    #draw_rectangle_deform(0, 0, 160, 60, d)

    # zad 4
    draw_sierpinski_carpet(0, 0, 150, 120, 3)

    glFlush()

def draw_triangle():
    # zmiana koloru wierzchołka przed jego utworzeniem

    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3ub(255, 0, 0)
    glVertex2f(50.0, 0.0)
    glColor3ub(0, 255, 0)
    glVertex2f(0.0, 50.0)
    glColor3ub(0, 0, 255)
    glVertex2f(-50.0, 0.0)
    glEnd()    

def draw_rectangle(x, y, width, height):
    glColor3f(0.6, 0.3, 0.1)
    glBegin(GL_TRIANGLES)
    glVertex2f(x-(width/2), y+(height/2))
    glVertex2f(x-(width/2), y-(height/2))
    glVertex2f(x+(width/2), y-(height/2))
    glEnd()

    glColor3f(0.6, 0.3, 0.1)
    glBegin(GL_TRIANGLES)
    glVertex2f(x-(width/2), y+(height/2))
    glVertex2f(x+(width/2), y+(height/2))
    glVertex2f(x+(width/2), y-(height/2))
    glEnd()   

def draw_rectangle_deform(x, y, width, height, d = 0.0):
    glColor3f(RED_VALUE, GREEN_VALUE, BLUE_VALUE)
    glBegin(GL_TRIANGLES)
    glVertex2f((x-(width/2)) * d, (y+(height/2)) * d)
    glVertex2f((x-(width/2)) * d, (y-(height/2)) * d)
    glVertex2f((x+(width/2)) * d, (y-(height/2)) * d)
    glEnd()

    glColor3f(RED_VALUE, GREEN_VALUE, BLUE_VALUE)
    glBegin(GL_TRIANGLES)
    glVertex2f((x-(width/2)) * d, (y+(height/2)) * d)
    glVertex2f((x+(width/2)) * d, (y+(height/2)) * d)
    glVertex2f((x+(width/2)) * d, (y-(height/2)) * d)
    glEnd()

# rysowanie dywanu na zasadzie rysowania prostokątów dookoła pustego miejsca na środku; wywoływanie rekurencyjne
def draw_sierpinski_carpet(x, y, width, height, level):
    if level > 0:
        level -= 1
        width /= 3
        height /= 3

        draw_sierpinski_carpet(x - width, y + height, width, height, level) # lewo-góra
        draw_sierpinski_carpet(x, y + height, width, height, level) # góra
        draw_sierpinski_carpet(x + width, y + height, width, height, level) # prawo-góra
        draw_sierpinski_carpet(x + width, y, width, height, level) # prawo
        draw_sierpinski_carpet(x + width, y - height ,width, height, level) # prawo-dół
        draw_sierpinski_carpet(x, y - height, width, height, level) # dół
        draw_sierpinski_carpet(x - width, y - height, width, height, level) # lewo-dół
        draw_sierpinski_carpet(x - width, y, width, height, level) # lewo

    else:
        draw_rectangle(x, y, width, height)


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()