from PySide2.QtWidgets import QApplication, QPushButton, QGridLayout, QWidget, QOpenGLWidget, QMainWindow
from OpenGL.GL import *


import sys


class GLWidget(QOpenGLWidget):

    def initializeGL(self):
        self.f = self.context().currentContext().functions()
        self.shader = self.context().currentContext().functions().Shaders

        self.f.glViewport(self.x(), self.y(), self.width(), self.height())
        self.f.glClear(GL_COLOR_BUFFER_BIT)

        filestream = open('vertex_program.glsl')
        program_vertex = str(filestream.readlines())

        filestream.close()

        filestream = open('fragment_program.glsl')
        program_fragment = str(filestream.readlines())

        self.shader.glCreateShader(program_vertex)
        glShaderSource(program_vertex,)

    def paintGL(self):
        self.f.glClear(GL_COLOR_BUFFER_BIT)



class MainScreen(QMainWindow):
    def switch_flag(self):
        self.flag = not self.flag


    def __init__(self, qt_app: QApplication):
        super(MainScreen, self).__init__()

        self.setGeometry(
            qt_app.primaryScreen().geometry().width() / 2 - qt_app.primaryScreen().geometry().width() / 100 * 40 / 2,
            qt_app.primaryScreen().geometry().height() / 2 - qt_app.primaryScreen().geometry().height() / 100 * 40 / 2,
            qt_app.primaryScreen().geometry().width() / 100 * 40,
            qt_app.primaryScreen().geometry().height() / 100 * 40
                         )

        self.gl_widget = GLWidget()

        self.flag = True
        self.stop_go_button = QPushButton("Stop")

        self.stop_go_button.clicked.connect(self.switch_flag)

        self.the_layout = QGridLayout()
        self.the_layout.addWidget(self.gl_widget, 1, 1)
        self.the_layout.addWidget(self.stop_go_button, 2, 1)

        self.center_screen = QWidget()
        self.center_screen.setLayout(self.the_layout)

        self.setCentralWidget(self.center_screen)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainScreen(app)
    window.show()

    app.exec_()
