#!/usr/bin/env python3
import sys

import math as math

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


viewer = [0.0, 0.0, 10.0]

space_pressed = 0

theta, phi = 0.0, 0.0
pix2angle = 1.0

scale = 1
R = 1

left_mouse_button_pressed, right_mouse_button_pressed = 0, 0
mouse_x_pos_old, mouse_y_pos_old = 0, 0
delta_x, delta_y = 0, 0


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


def shutdown():
    pass


def update_glu_look_at(x, y, z):
    gluLookAt(x, y, z, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


def calculate_theta_phi_on_button_pressed(theta, phi):
    if left_mouse_button_pressed:
        theta += delta_x * pix2angle
        phi += delta_y * pix2angle

    return theta%360, phi%360


def calculate_x_y_x_on_button_pressed(theta, phi):
    global R   

    new_x = math.cos(theta * math.pi / 180) * math.cos(phi * math.pi / 180) * R 
    new_y = math.sin(phi * math.pi / 180) * R
    new_z = math.sin(theta * math.pi / 180) * math.cos(phi * math.pi / 180) * R

    return new_x, new_y, new_z  


def scale_fixup():
    global scale
    global R

    scale = 0.3 if scale < 0.3 else scale
    R = 0.3 if R < 0.3 else R

    scale = 1.5 if scale > 1.5 else scale
    R = 10.0 if R > 10.0 else R

def rotate_object_x_axis():
    global theta, phi

    theta, phi = calculate_theta_phi_on_button_pressed(theta, phi)

    glRotatef(theta, 0.0, 1.0, 0.0)
    glRotatef(phi, 1.0, 0.0, 0.0)


def rotate_and_scale_object():
    global theta, phi, scale

    theta, phi = calculate_theta_phi_on_button_pressed(theta, phi)
    
    if right_mouse_button_pressed:
        scale += 0.01 * delta_y

    glRotatef(theta, 0.0, 1.0, 0.0)
    glRotatef(phi, 1.0, 0.0, 0.0)
    glScalef(scale, scale, scale)


def move_camera_around():
    global theta, phi, R

    theta, phi = calculate_theta_phi_on_button_pressed(theta, phi)

    if right_mouse_button_pressed:
        R += 0.01 * delta_y

    x, y, z = calculate_x_y_x_on_button_pressed(theta, phi)

    update_glu_look_at(x, y, z)


def move_camera_in_a_proper_way():
    global theta, phi, R

    theta, phi = calculate_theta_phi_on_button_pressed(theta, phi)

    if right_mouse_button_pressed:
        R += 0.01 * delta_y    
        
    x, y, z = calculate_x_y_x_on_button_pressed(theta, phi)

    if 90 < phi < 270:
        print(1,phi)
        update_glu_look_at(x, y, z)
    else:
        print(-1,phi)
        gluLookAt(x, y, z, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0)    


def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()


def example_object():
    glColor3f(1.0, 1.0, 1.0)

    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_LINE)
    glRotatef(90, 1.0, 0.0, 0.0)
    glRotatef(-90, 0.0, 1.0, 0.0)

    gluSphere(quadric, 1.5, 10, 10)

    glTranslatef(0.0, 0.0, 1.1)
    gluCylinder(quadric, 1.0, 1.5, 1.5, 10, 5)
    glTranslatef(0.0, 0.0, -1.1)

    glTranslatef(0.0, 0.0, -2.6)
    gluCylinder(quadric, 0.0, 1.0, 1.5, 10, 5)
    glTranslatef(0.0, 0.0, 2.6)

    glRotatef(90, 1.0, 0.0, 1.0)
    glTranslatef(0.0, 0.0, 1.5)
    gluCylinder(quadric, 0.1, 0.0, 1.0, 5, 5)
    glTranslatef(0.0, 0.0, -1.5)
    glRotatef(-90, 1.0, 0.0, 1.0)

    glRotatef(-90, 1.0, 0.0, 1.0)
    glTranslatef(0.0, 0.0, 1.5)
    gluCylinder(quadric, 0.1, 0.0, 1.0, 5, 5)
    glTranslatef(0.0, 0.0, -1.5)
    glRotatef(90, 1.0, 0.0, 1.0)

    glRotatef(90, 0.0, 1.0, 0.0)
    glRotatef(-90, 1.0, 0.0, 0.0)
    gluDeleteQuadric(quadric)


def render(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(viewer[0], viewer[1], viewer[2], 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    # zad 1
    #rotate_object_x_axis()

    # zad 2
    #rotate_and_scale_object()

    # zad 3
    #move_camera_around()

    #zad 4
    scale_fixup()

    if space_pressed:
        rotate_and_scale_object()
    else:
        move_camera_in_a_proper_way()

    axes()
    example_object()

    glFlush()


def update_viewport(window, width, height):
    global pix2angle
    pix2angle = 360.0 / width

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(70, 1.0, 0.1, 300.0)

    if width <= height:
        glViewport(0, int((height - width) / 2), width, width)
    else:
        glViewport(int((width - height) / 2), 0, height, height)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def keyboard_key_callback(window, key, scancode, action, mods):
    if key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
        glfwSetWindowShouldClose(window, GLFW_TRUE)

    global space_pressed
    if key == GLFW_KEY_SPACE and action == GLFW_PRESS:
        space_pressed = not space_pressed


def mouse_motion_callback(window, x_pos, y_pos):
    global delta_x, delta_y
    global mouse_x_pos_old, mouse_y_pos_old

    delta_x = x_pos - mouse_x_pos_old
    mouse_x_pos_old = x_pos

    delta_y = y_pos - mouse_y_pos_old
    mouse_y_pos_old = y_pos


def mouse_button_callback(window, button, action, mods):
    global left_mouse_button_pressed, right_mouse_button_pressed

    if button == GLFW_MOUSE_BUTTON_LEFT and action == GLFW_PRESS:
        left_mouse_button_pressed = 1
    else:
        left_mouse_button_pressed = 0

    if button == GLFW_MOUSE_BUTTON_RIGHT and action == GLFW_PRESS:
        right_mouse_button_pressed = 1
    else:
        right_mouse_button_pressed = 0


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSetKeyCallback(window, keyboard_key_callback)
    glfwSetCursorPosCallback(window, mouse_motion_callback)
    glfwSetMouseButtonCallback(window, mouse_button_callback)
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