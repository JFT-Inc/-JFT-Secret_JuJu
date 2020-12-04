#version 440

attribute vec2 position;

void main() {
    gl_position = vec4(position, 0.0, 0.1);
}
