import pygame
from pygame.locals import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

def init_lighting():
    glEnable(GL_LIGHTING) #lighting
    glEnable(GL_LIGHT0) #light 0
    glEnable(GL_COLOR_MATERIAL) # color with light
    glShadeModel(GL_SMOOTH) #shadeee

    light_position = [0.5, 0, 1.5, 1]
    ambient_light = [0.6, 0.4, 0.4, 1.0]
    diffuse_light = [1.0, 0.7, 0.6, 1.0]
    specular_light = [0.9, 0.5, 0.5, 1.0]

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_light)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse_light)
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular_light)

    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 64.0)

def circle(radius = 1, stacks = 50, slices = 50):
    top_color = (0.85, 0.1, 0.1)   # red (RGB)
    bottom_color = (0.55, 0.45, 0.35)   # brown

    for i in range(stacks):
        lat0 = math.pi * (-0.5 + float(i) / stacks)
        z0 = radius * math.sin(lat0)
        zr0 = radius * math.cos(lat0)

        lat1 = math.pi * (-0.5 + float(i+1) / stacks)
        z1 = radius * math.sin(lat1)
        zr1 = radius * math.cos(lat1)

        t0 = (i / stacks) # warna top jika 0
        t1 = ((i + 1) / stacks) # warna bottom jika 1

        #linear interpolation formula 
        color0 = [top_color[j] * (1 - t0) + bottom_color[j] * t0 for j in range(3)]
        color1 = [top_color[j] * (1 - t1) + bottom_color[j] * t1 for j in range(3)]

        glBegin(GL_QUAD_STRIP)
        for j in range(slices + 1):
            lng = 2 * math.pi * float(j) / slices
            x = math.cos(lng)
            y = math.sin(lng)

            glNormal3f(x * zr0 / radius, y * zr0 / radius, z0 / radius)
            glColor3fv(color0)
            glVertex3f(x * zr0, y * zr0, z0)

            glNormal3f(x * zr1 / radius, y * zr1 / radius, z1 / radius)
            glColor3fv(color1)
            glVertex3f(x * zr1, y * zr1, z1)
        glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL|RESIZABLE)

    gluPerspective(60, display[0]/display[1], 0.1, 50)
    glTranslatef(0.0, 0.0, -5)
    glEnable(GL_DEPTH_TEST)

    init_lighting()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # glScalef(1.2, 0.9, 1.0) 
        glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)
        glRotatef(1, 1, 1, 1)
        glScalef(1, 1, 1)
        circle(1.5, 50, 50)
        pygame.display.flip()
        pygame.time.wait(20)

main()
