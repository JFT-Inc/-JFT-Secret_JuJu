from glumpy import app, gloo, gl

filestream = open('vertex_program.glsl')
program_vertex = str(filestream.readlines())

filestream.close()

filestream = open('fragment_program.glsl')
program_fragment = str(filestream.readlines())

window = app.Window()

quad = gloo.Program(program_vertex, program_fragment, count=4)

quad['position'] = (-1, +1), (+1, +1), (-1, -1), (+1, -1)

@window.event
def on_draw(dt):
    window.clear()
    quad.draw(gl.GL_TRIANGLE_STRIP)

app.run()

