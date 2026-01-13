from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def drawRect(x1, y1, x2, y2):
    glBegin(GL_POLYGON)
    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glVertex2f(x2, y2)
    glVertex2f(x1, y2)
    glEnd()


# ---------------------- LETTER K -----------------------
def drawK(x, y, w, h):
    t = w * 0.2

    drawRect(x, y, x + t, y + h)

    glBegin(GL_POLYGON)
    glVertex2f(x + t, y + h * 0.6)
    glVertex2f(x + w, y + h)
    glVertex2f(x + w - t, y + h)
    glVertex2f(x + t, y + h * 0.5)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(x + t, y + h * 0.4)
    glVertex2f(x + w - t, y)
    glVertex2f(x + w, y)
    glVertex2f(x + t, y + h * 0.5)
    glEnd()


# ---------------------- LETTER A -----------------------
def drawA(x, y, w, h):
    t = w * 0.2
    drawRect(x, y, x + t, y + h)
    drawRect(x + w - t, y, x + w, y + h)
    drawRect(x, y + h - t, x + w, y + h)
    drawRect(x, y + h / 2 - t / 2, x + w, y + h / 2 + t / 2)


# ---------------------- LETTER D  -----------------------
def drawD(x, y, w, h):
    t = w * 0.2

    drawRect(x, y, x + t, y + h)

    glBegin(GL_POLYGON)
    glVertex2f(x + t, y)
    glVertex2f(x + w, y + h * 0.25)
    glVertex2f(x + w, y + h * 0.75)
    glVertex2f(x + t, y + h)
    glEnd()

    # Inner cut-out
    glColor3f(0.1, 0.1, 0.1)
    glBegin(GL_POLYGON)
    glVertex2f(x + t * 1.5, y + t)
    glVertex2f(x + w - t * 1.5, y + h * 0.25 + t)
    glVertex2f(x + w - t * 1.5, y + h * 0.75 - t)
    glVertex2f(x + t * 1.5, y + h - t)
    glEnd()

    glColor3f(0.0, 1.0, 1.0)


# ---------------------- LETTER E -----------------------
def drawE(x, y, w, h):
    t = w * 0.2
    drawRect(x, y, x + t, y + h)
    drawRect(x + t, y + h - t, x + w, y + h)
    drawRect(x + t, y + h / 2 - t / 2, x + w * 0.9, y + h / 2 + t / 2)
    drawRect(x + t, y, x + w, y + t)


# ---------------------- LETTER L -----------------------
def drawL(x, y, w, h):
    t = w * 0.2
    drawRect(x, y, x + t, y + h)
    drawRect(x, y, x + w, y + t)


# ---------------------- MAIN DISPLAY -----------------------
def display():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.0, 1.0, 1.0)

    startX = -0.9
    y = -0.2
    w = 0.25
    h = 0.6
    gap = 0.05

    drawK(startX, y, w, h)
    drawA(startX + (w + gap), y, w, h)
    drawD(startX + 2 * (w + gap), y, w, h)
    drawE(startX + 3 * (w + gap), y, w, h)
    drawL(startX + 4 * (w + gap), y, w, h)

    glFlush()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"KADEL - OpenGL Letters (Python)")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()


if __name__ == "__main__":
    main()
