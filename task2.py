#Task 2

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

WINDOW_WIDTH,WINDOW_HEIGHT=700,700
b_speed=1.07
blink=False
freeze=False
blink_curr_col=True
blin_t=time.time()
poi_li=[]

def point(x,y,r,g,b,ba_size):
    glColor3f(r,g,b)
    glPointSize(ba_size)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def keyboard_listener(key,x,y):
    global freeze
    if key==b' ': 
        freeze=not freeze
    glutPostRedisplay()

def special_key_listener(key,x,y):
    global b_speed
    if freeze==True:
        return
    if key==GLUT_KEY_UP:
        b_speed=min(9,b_speed*1.08)
    elif key==GLUT_KEY_DOWN:
        b_speed=max(0.09,b_speed/1.08)
    glutPostRedisplay()

def mouse_listener(button,state,x,y):
    global blink
    if freeze==True: 
        return
    
    if button==GLUT_RIGHT_BUTTON and state==GLUT_DOWN:
        dx=random.choice([-1,1])
        dy=random.choice([-1,1]) 
        poi_li.append({
            'x':float(x),'y':float(y), 
            'dx':dx,'dy':dy, 
            'r':random.random(),'g':random.random(),'b':random.random()
        })
    elif button==GLUT_LEFT_BUTTON and state==GLUT_DOWN:
        blink=not blink
    glutPostRedisplay()

def setup_projection():
    glViewport(0,0,700,700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0,700.0,700.0,0.0,0.0,1.0)
    glMatrixMode(GL_MODELVIEW)

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    setup_projection()
    glColor3f(0.57,0.63,0.84)
    glBegin(GL_LINES)
    glVertex2f(3,3);glVertex2f(697,3)
    glVertex2f(697,3);glVertex2f(697,697)
    glVertex2f(697,697);glVertex2f(3,697)
    glVertex2f(3,697);glVertex2f(3,3)
    glEnd()

    for i in poi_li:
        if blink and not blink_curr_col:
            point(i['x'],i['y'],0,0,0,7)
        else:
            point(i['x'],i['y'],i['r'],i['g'],i['b'],7)

    glutSwapBuffers()

def animate():
    global blin_t,blink_curr_col
    curr=time.time()
    
    if blink and not freeze:
        if curr-blin_t>0.5:
            blink_curr_col=not blink_curr_col
            blin_t=curr
    elif not blink:
        blink_curr_col=True

    if freeze:
        glutPostRedisplay()
        return

    for i in poi_li:
        i['x']+=i['dx']*b_speed
        i['y']+=i['dy']*b_speed

        if i['x']>=697:
            i['x']=697-(i['x']-697)
            i['dx']*=-1
        elif i['x']<=3:
            i['x']=3+(3-i['x'])
            i['dx']*=-1

        if i['y']>=697:
            i['y']=697-(i['y']-697)
            i['dy']*=-1
        elif i['y']<=3:
            i['y']=3+(3-i['y'])
            i['dy']*=-1
            
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE)
    glutInitWindowSize(700,700) 
    glutInitWindowPosition(350,50)
    glutCreateWindow(b"Task2")
    glutDisplayFunc(display)
    glutIdleFunc(animate)
    glutKeyboardFunc(keyboard_listener)
    glutSpecialFunc(special_key_listener)
    glutMouseFunc(mouse_listener)
 
    glutMainLoop()

if __name__=="__main__":
    main()