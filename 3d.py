from math import *

from pyglet.gl import *
import pyglet
from life import *
from pyglet.window import key


try:
    # Try and create a window with multisampling (antialiasing)
    config = Config(sample_buffers=1, samples=4, 
                    depth_size=16, double_buffer=True,)
    window = pyglet.window.Window(resizable=True, config=config)
except pyglet.window.NoSuchConfigException:
    # Fall back to no multisampling for old hardware
    window = pyglet.window.Window(resizable=True)
    

@window.event
def on_resize(width, height):
    # Override the default on_resize handler to create a 3D projection
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluLookAt(0, 0, -1, 0, 0, 0, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)
    return pyglet.event.EVENT_HANDLED

def update(dt):
    global rx, ry, rz
    rx += dt * 1
    ry += dt * 80
    rz += dt * 30
    rx %= 360
    ry %= 360
    rz %= 360
pyglet.clock.schedule(update)

@window.event
def on_draw():
    def vec(*args):
        return (GLfloat * len(args))(*args)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    vertexList = a.getVertexList()
    #vertexList = [[1, 1, -4], [-1, 1, -4], [-1, -1, -4], [1, -1, -4], [0, 0, -4], [1, 0, -4], [-1, 0, -4], [0, 1, -4], [0, -1, -4]]
    sphere = gluNewQuadric()
    one = True
    sphere2 = gluNewQuadric()

    for i in range(len(vertexList)):
        x = vertexList[i][0]
        y = vertexList[i][1]
        z = vertexList[i][2]
        glTranslatef(x, y, z)
        if (one):
            glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, vec(1, 0, 1, 1))
            glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, vec(0, 0, 0, 1))
            glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 0)
            s = sphere
            one = False
        else:
            glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, vec(0, 0, 1, 1))
            glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, vec(0, 0, 0, 1))
            glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 0)
            s = sphere2
            one = True
        gluSphere(s, 0.4, 50, 50)
        glTranslatef(-x, -y, -z)
    
def setup():
    # One-time GL setup
    glClearColor(1, 1, 1, 1)
    glColor3f(1, 0, 0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)

    # Uncomment this line for a wireframe view
    #glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    # Simple light setup.  On Windows GL_LIGHT0 is enabled by default,
    # but this is not the case on Linux or Mac, so remember to always 
    # include it.
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)

    # Define a simple function to create ctypes arrays of floats:
    def vec(*args):
        return (GLfloat * len(args))(*args)

    glLightfv(GL_LIGHT0, GL_POSITION, vec(.5, .5, 1, 0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, vec(0.5, .5, 0.5, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, vec(1, 1, 1, 1))
    glLightfv(GL_LIGHT1, GL_POSITION, vec(1, 0, .5, 0))
    glLightfv(GL_LIGHT1, GL_DIFFUSE, vec(.5, .5, .5, 1))
    glLightfv(GL_LIGHT1, GL_SPECULAR, vec(1, 1, 1, 1))

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, vec(1, 0, 0, 1))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, vec(0, 0, 0, 1))
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 0)

a = GameOfLife(5, 5, 5)
setup()
rx = ry = rz = 0

pyglet.app.run()
