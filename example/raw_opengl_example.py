import sys
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import ctypes


def display():
    glut.glutSwapBuffers()


def reshape(width, height):
    gl.glViewport(0, 0, width, height)


def keyboard(key, x, y):
    if key == b'\x1b':
        sys.exit()


if __name__ == "__main__":
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE, glut.GLUT_RGBA)
    glut.glutCreateWindow('!!!')
    glut.glutReshapeWindow(1000, 1000)
    glut.glutReshapeFunc(reshape)
    glut.glutDisplayFunc(display)
    glut.glutKeyboardFunc(keyboard)
    glut.glutMainLoop()