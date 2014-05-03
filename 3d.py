from math import *

from pyglet.gl import *
import pyglet
from life import *
from pyglet.window import key


tx = ty = ry = rz = rx = 0
tz = -1
try:
    # Tty and create a window with multisampling (antialiasing)
    config = Config(sample_buffers=1, samples=4, 
                    depth_size=16, double_buffer=True,)
    window = pyglet.window.Window(resizable=True, config=config)
except pyglet.window.NoSuchConfigException:
    # Fall back to no multisampling for old hardware
    window = pyglet.window.Window(resizable=True)
    

@window.event
def on_key_press(symbol, modifiers):
    step_size = 1
    global tx, ty, tz, ry, rz, rx
    if symbol == pyglet.window.key.UP:
        ty += step_size
    if symbol == pyglet.window.key.DOWN:
        ty -= step_size
    if symbol == pyglet.window.key.RIGHT:
        tx += step_size
    if symbol == pyglet.window.key.LEFT:
        tx -= step_size
    if symbol == pyglet.window.key.EQUAL:
        tz += step_size
    if symbol == pyglet.window.key.MINUS:
        tz -= step_size
    if symbol == pyglet.window.key._0:
        ry += 10
        ry %= 360
    if symbol == pyglet.window.key._9:
        ry -= 10
        ry %= 360
    if symbol == pyglet.window.key.F:
        rz -= 10
        rz %= 360
    if symbol == pyglet.window.key.H:
        rz += 10
        rz %= 360
    if symbol == pyglet.window.key.G:
        rx -= 10
        rx %= 360
    if symbol == pyglet.window.key.T:
        rx += 10
        rx %= 360
    if symbol == pyglet.window.key.S:
        a.update()
    if symbol == pyglet.window.key.R:
        a.reset()
    if symbol == pyglet.window.key.P:
        global play
        play = not play
        
@window.event
def on_resize(width, height):
    # Override the default on_resize handler to create a 3D projection
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45., width / float(height), .1, 1000.)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    return pyglet.event.EVENT_HANDLED

def update(dt):
    if play:
        a.update()

pyglet.clock.schedule(update)

@window.event
def on_draw():
    r = 0.4
    p = 2.0
    def vec(*args):
        return (GLfloat * len(args))(*args)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    vertexList = a.getVertexList()
    #vertexList = [[1, 1, -4], [-1, 1, -4], [-1, -1, -4], [1, -1, -4], [0, 0, -4], [1, 0, -4], [-1, 0, -4], [0, 1, -4], [0, -1, -4]]
    sphere = gluNewQuadric()
    one = True
    sphere2 = gluNewQuadric()

    
    glTranslatef(-tx,-ty,tz)
    glTranslatef(-gameWidth / 2.0 / p + 0.25, -gameHeight / 2.0 / p + 0.25, -gameDepth / p)
    glTranslatef(gameWidth / 2.0 / p, 0, -gameDepth / 2.0 / p)
    glRotatef(rx, 1.0, 0, 0)
    glRotatef(rz, 0, 0, 1.0)
    glRotatef(ry, 0, 1.0, 0)

    glTranslatef(-gameWidth / 2.0 / p, 0, -gameDepth/ 2.0 / p)

    for i in range( len(vertexList) ):
        x = vertexList[i][0] / p
        y = vertexList[i][1] / p
        z = vertexList[i][2] / p
        num = vertexList[i][3]
        glTranslatef(x, y, z)
        if (1 == num):
            glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, vec(1, 0, 0, 1))
            #glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, vec(1, 1, 1, 1))
            #glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 20)
            s = sphere
        else:
            glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, vec(0, 0, 1, 1))
            #glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, vec(1, 1, 1, 1))
            #glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 20)
            s = sphere2
        gluSphere(s, r/p, 50, 50)
        glTranslatef(-x, -y, -z)
    
def setup():
    # One-time GL setup
    glClearColor(0, 0, 0, 1)
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
    #glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, vec(1, 1, 1, 1))
    #glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 20)


play = False
gameWidth = 5
gameHeight = 5
gameDepth = 5
#a = GameOfLife2D(gameWidth, gameHeight, gameDepth, None)
#a = GameOfLife(gameWidth, gameHeight, gameDepth, None, [5], [4,5,9])
#a = GameOfLife(gameWidth, gameHeight, gameDepth, None, [5, 6], [4])
#a = GameOfWar(gameWidth, gameHeight, gameDepth, None)
a = GameOfWar(5, 5, 5, randomMap(5, 5, 5, 4))
#a.update()
a.update()
setup()


pyglet.app.run()
