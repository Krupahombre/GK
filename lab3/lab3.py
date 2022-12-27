#!/usr/bin/env python3
import sys

import numpy as nump
import random as rand

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    global N
    global verticesArray
    global colorArray

    N = 25
    verticesArray = create_vertices_array(N)
    colorArray = create_random_color_array(N)


def create_vertices_array(N):
    verticesArray = nump.zeros((N, N, 3))

# utworzenie tabeli N elementowej z wypełnieniem komórek wartościami od 0 do 1 w zależności od N
    uArray: list = [u / (N - 1) for u in range(0, N)]
    vArray: list = [v / (N - 1) for v in range(0, N)]

    for i in range(0, N):
        for j in range(0, N):
            # x
            verticesArray[i][j][0] = ((-90 * uArray[i] ** 5
                                   + 225 * uArray[i] ** 4
                                   - 270 * uArray[i] ** 3
                                   + 180 * uArray[i] ** 2
                                   - 45 * uArray[i])
                                   * nump.cos(nump.pi * vArray[j]))
            # y
            verticesArray[i][j][1] = (160 * uArray[i] ** 4
                                   - 320 * uArray[i] ** 3
                                   + 160 * uArray[i] ** 2 - 5)
            # z
            verticesArray[i][j][2] = ((-90 * uArray[i] ** 5
                                    + 225 * uArray[i] ** 4
                                    - 270 * uArray[i] ** 3
                                    + 180 * uArray[i] ** 2
                                    - 45 * uArray[i])
                                   * nump.sin(nump.pi * vArray[j]))

    return verticesArray


def create_random_color_array(N):
    randomColorArray = nump.zeros((N, N, 3))

    for i in range(0, N):
        for j in range(0, N):
            randomColorArray[i][j][0] = rand.random()
            randomColorArray[i][j][1] = rand.random()
            randomColorArray[i][j][2] = rand.random()

    return randomColorArray


def shutdown():
    pass


def draw_egg_model_with_points():
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 1.0)
    for i in range(0, N):
        for j in range(0, N):
            glVertex3f(verticesArray[i][j][0],
                          verticesArray[i][j][1],
                          verticesArray[i][j][2])
    glEnd()


def draw_egg_model_with_lines():
    glColor3f(1.0, 0.0, 1.0)
    for i in range(0, N - 1):
        for j in range(0, N - 1):
            glBegin(GL_LINES)
            glVertex3f(verticesArray[i][j][0],
                          verticesArray[i][j][1],
                          verticesArray[i][j][2])
            glVertex3f(verticesArray[i + 1][j][0],
                          verticesArray[i + 1][j][1],
                          verticesArray[i + 1][j][2])
            glEnd()

            glBegin(GL_LINES)
            glVertex3f(verticesArray[i][j][0],
                          verticesArray[i][j][1],
                          verticesArray[i][j][2])
            glVertex3f(verticesArray[i][j + 1][0],
                          verticesArray[i][j + 1][1],
                          verticesArray[i][j + 1][2])
            glEnd()    


def draw_egg_model_with_triangles():
    for i in range(0, N - 1):
        for j in range(0, N - 1):
            glBegin(GL_TRIANGLES)
            glColor3f(colorArray[i][j][0],
                        colorArray[i][j][1],
                        colorArray[i][j][2])
            glVertex3f(verticesArray[i][j][0],
                        verticesArray[i][j][1],
                        verticesArray[i][j][2])

            glColor3f(colorArray[i + 1][j][0],
                        colorArray[i + 1][j][1],
                        colorArray[i + 1][j][2])
            glVertex3f(verticesArray[i + 1][j][0],
                        verticesArray[i + 1][j][1],
                        verticesArray[i + 1][j][2])

            glColor3f(colorArray[i][j + 1][0],
                        colorArray[i][j + 1][1],
                        colorArray[i][j + 1][2])
            glVertex3f(verticesArray[i][j + 1][0],
                        verticesArray[i][j + 1][1],
                        verticesArray[i][j + 1][2])
            glEnd()

            glBegin(GL_TRIANGLES)
            glColor3f(colorArray[i + 1][j][0],
                        colorArray[i + 1][j][1],
                        colorArray[i + 1][j][2])
            glVertex3f(verticesArray[i + 1][j][0],
                        verticesArray[i + 1][j][1],
                        verticesArray[i + 1][j][2])

            glColor3f(colorArray[i][j + 1][0],
                        colorArray[i][j + 1][1],
                        colorArray[i][j + 1][2])
            glVertex3f(verticesArray[i][j + 1][0],
                        verticesArray[i][j + 1][1],
                        verticesArray[i][j + 1][2])

            glColor3f(colorArray[i + 1][j + 1][0],
                        colorArray[i + 1][j + 1][1],
                        colorArray[i + 1][j + 1][2])
            glVertex3f(verticesArray[i + 1][j + 1][0],
                        verticesArray[i + 1][j + 1][1],
                        verticesArray[i + 1][j + 1][2])
            glEnd()

def draw_egg_model_wIth_triangle_strip():
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(N - 1):
        for j in range(N - 1):
            if (j != N - 2):
                glColor3f(colorArray[i][j][0],
                             colorArray[i][j][1],
                             colorArray[i][j][2])
                glVertex3f(verticesArray[i][j][0],
                              verticesArray[i][j][1],
                              verticesArray[i][j][2])

                glColor3f(colorArray[i][j + 1][0],
                             colorArray[i][j + 1][1],
                             colorArray[i][j + 1][2])
                glVertex3f(verticesArray[i][j + 1][0],
                              verticesArray[i][j + 1][1],
                              verticesArray[i][j + 1][2])

                glColor3f(colorArray[i + 1][j][0],
                             colorArray[i + 1][j][1],
                             colorArray[i + 1][j][2])
                glVertex3f(verticesArray[i + 1][j][0],
                              verticesArray[i + 1][j][1],
                              verticesArray[i + 1][j][2])

                glColor3f(colorArray[i + 1][j + 1][0],
                             colorArray[i + 1][j + 1][1],
                             colorArray[i + 1][j + 1][2])
                glVertex3f(verticesArray[i + 1][j + 1][0],
                              verticesArray[i + 1][j + 1][1],
                              verticesArray[i + 1][j + 1][2])
                              
            else:
                glColor3f(colorArray[i][j][0],
                             colorArray[i][j][1],
                             colorArray[i][j][2])
                glVertex3f(verticesArray[i][j][0],
                              verticesArray[i][j][1],
                              verticesArray[i][j][2])

                glColor3f(colorArray[i][j + 1][0],
                             colorArray[i][j + 1][1],
                             colorArray[i][j + 1][2])
                glVertex3f(verticesArray[i][j + 1][0],
                              verticesArray[i][j + 1][1],
                              verticesArray[i][j + 1][2])

                glColor3f(colorArray[i + 1][j][0],
                             colorArray[i + 1][j][1],
                             colorArray[i + 1][j][0])
                glVertex3f(verticesArray[i + 1][j][0],
                              verticesArray[i + 1][j][1],
                              verticesArray[i + 1][j][2])

                glColor3f(colorArray[i + 1][j + 1][0],
                             colorArray[i + 1][j + 1][1],
                             colorArray[i + 1][j + 1][0])
                glVertex3f(verticesArray[i + 1][j + 1][0],
                              verticesArray[i + 1][j + 1][1],
                              verticesArray[i + 1][j + 1][2])
    glEnd()            


def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)


def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -1.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -1.0)
    glVertex3f(0.0, 0.0, 1.0)

    glEnd()


def render(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    axes()

    # zad 1
    #draw_egg_model_with_points()

    # zad 2
    #spin(time * 180 / nump.pi)
    #draw_egg_model_with_lines()

    # zad 3
    #spin(time * 180 / nump.pi)
    #draw_egg_model_with_triangles()

    # zad 4
    spin(time * 180 / nump.pi)
    draw_egg_model_wIth_triangle_strip()

    glFlush()


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
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

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