#Task 1

import random
from OpenGL.GL import *    
from OpenGL.GLUT import *   
from OpenGL.GLU import *    

brightness=1.0    
d_target=1.0

rain=[[random.uniform(0,1000),random.uniform(0,1000)] for i in range(153)]
speed=0.0
t_speed=0.0

def sky_bagr():
    glColor3f (0.05+0.35*brightness, 
        0.13+0.67*brightness,  
        0.20+0.80*brightness)

    glBegin(GL_TRIANGLES)
    glVertex2f(1000,0)
    glVertex2f(1000,1000)
    glVertex2f(500,500)
  
    glVertex2f(1000,0)
    glVertex2f(500,500)
    glVertex2f(0,0)
 
    glVertex2f(1000,1000)
    glVertex2f(0,1000)
    glVertex2f(500,500)
   
    glVertex2f(500,500)
    glVertex2f(0,1000)
    glVertex2f(0,0)
    glEnd()
    
def ground():
  
    glColor3f (0.23+0.75*brightness,
        0.57+0.63*brightness,
        0.31+0.25*brightness)

    glBegin(GL_TRIANGLES)
    glVertex2f(1000,0)
    glVertex2f(500,500)
    glVertex2f(0,0)

    glVertex2f(1000,600)
    glVertex2f(500,500)
    glVertex2f(1000,0)

    glVertex2f(0,600)
    glVertex2f(500,500)
    glVertex2f(1000,600)

    glVertex2f(0,0)
    glVertex2f(500,500)
    glVertex2f(0,600)

    glEnd()


    glColor3f (0.10+0.10*brightness,
        0.17+0.25*brightness,
        0.10+0.00*brightness)

    glLineWidth(17)
    glBegin(GL_LINES)
    glVertex2f(0,600)
    glVertex2f(1000,600)
    glEnd()

    glLineWidth(7)
    glBegin(GL_LINES)
    glVertex2f(0,500)
    glVertex2f(1000,500)
    glEnd()
   
def grassocc():

    glColor3f( 0.05+0.05*brightness,
        0.13+0.59*brightness,
        0.05+0.17*brightness)

    glBegin(GL_TRIANGLES)

    glVertex2f(0,500); glVertex2f(25,590); glVertex2f(50,500)
  
    glVertex2f(50,500); glVertex2f(75,590); glVertex2f(100,500)
   
    glVertex2f(100,500); glVertex2f(125,590); glVertex2f(150,500)

    glVertex2f(150,500); glVertex2f(175,590); glVertex2f(200,500)
   
    glVertex2f(200,500); glVertex2f(225,590); glVertex2f(250,500)
   
    glVertex2f(250,500); glVertex2f(275,590); glVertex2f(300,500)
   
    glVertex2f(300,500); glVertex2f(325,590); glVertex2f(350,500)
    
    glVertex2f(350,500); glVertex2f(375,590); glVertex2f(400,500)
    
    glVertex2f(400,500); glVertex2f(425,590); glVertex2f(450,500)
    
    glVertex2f(450,500); glVertex2f(475,590); glVertex2f(500,500)
 
    glVertex2f(500,500); glVertex2f(525,590); glVertex2f(550,500)
   
    glVertex2f(550,500); glVertex2f(575,590); glVertex2f(600,500)
    
    glVertex2f(600,500); glVertex2f(625,590); glVertex2f(650,500)
  
    glVertex2f(650,500); glVertex2f(675,590); glVertex2f(700,500)
   
    glVertex2f(700,500); glVertex2f(725,590); glVertex2f(750,500)

    glVertex2f(750,500); glVertex2f(775,590); glVertex2f(800,500)
    
    glVertex2f(800,500); glVertex2f(825,590); glVertex2f(850,500)
    
    glVertex2f(850,500); glVertex2f(875,590); glVertex2f(900,500)
   
    glVertex2f(900,500); glVertex2f(925,590); glVertex2f(950,500)

    glVertex2f(950,500); glVertex2f(975,590); glVertex2f(1000,500)

    glEnd()

def wall():

    glColor3f (0.32+0.45*brightness,
        0.32+0.37*brightness,
        0.33+0.43*brightness)

    glBegin(GL_TRIANGLES)

    glVertex2f(700,300); glVertex2f(500,405); glVertex2f(300,300)

    glVertex2f(700,510); glVertex2f(500,405); glVertex2f(700,300)

    glVertex2f(300,300); glVertex2f(500,405); glVertex2f(300,510)

    glVertex2f(300,510); glVertex2f(500,405); glVertex2f(700,510)

    glEnd()
    glColor3f(0.0,0.0,0.0)
    glLineWidth(3)
    glBegin(GL_LINES)

    glVertex2f(300,300)
    glVertex2f(700,300)  

    glVertex2f(700,300)
    glVertex2f(700,510)  

    glVertex2f(700,510)
    glVertex2f(300,510)  

    glVertex2f(300,510)
    glVertex2f(300,300) 
  
    glEnd()

    glColor3f(0.33, 0.71, 0.44)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(340,300); glVertex2f(340,510)
    glVertex2f(660,300); glVertex2f(660,510)
    glVertex2f(440,300); glVertex2f(440,510)
    glVertex2f(560,300); glVertex2f(560,510)
    glEnd()

def roof():
    glColor3f(0.43+0.41*brightness,   
    0.23+0.27*brightness,   
    0.05+0.37*brightness)

    glBegin(GL_TRIANGLES)
    glVertex2f(800,510)
    glVertex2f(500,650)
    glVertex2f(200,510)
    glEnd()

    glColor3f(0.0,0.0,0.0)
    glLineWidth(3)
    glBegin(GL_LINES)

    glVertex2f(200,510)
    glVertex2f(800,510)

    glVertex2f(200,510)
    glVertex2f(500,650) 

    glVertex2f(500,650)
    glVertex2f(800,510)   
    glEnd()


def doorh():
   
    glColor3f(0.33+0.61*brightness,
        0.24+0.33*brightness,
        0.17+0.29*brightness)
    glBegin(GL_TRIANGLES)

    glVertex2f(550,300)
    glVertex2f(450,450)
    glVertex2f(450,300)

    glVertex2f(550,300)
    glVertex2f(550,450)
    glVertex2f(450,450)

    glEnd()

    glColor3f(0.2,0.5,0.7)  
    glPointSize(13)
    glBegin(GL_POINTS)
    glVertex2f(530,375)
    glEnd()


def windowh():
    glColor3f(0.91+0.07*brightness,
        0.83+0.19*brightness,
        0.00+0.37*brightness)
    glBegin(GL_TRIANGLES)
    
    glVertex2f(400,390)
    glVertex2f(350,420)
    glVertex2f(350,390)
   
    glVertex2f(400,390)
    glVertex2f(400,420)
    glVertex2f(350,420)

    glVertex2f(650,390)
    glVertex2f(600,420)
    glVertex2f(600,390)
 
    glVertex2f(650,390)
    glVertex2f(650,420)
    glVertex2f(600,420)

    glEnd()

    glColor3f(0.10+0.10*brightness,
    0.10+0.10*brightness,
    0.10+0.10*brightness)
    glLineWidth(3)
    glBegin(GL_LINES)
   
    glVertex2f(350,405);  glVertex2f(400,405)   
    glVertex2f(375,390);  glVertex2f(375,420)   
   
    glVertex2f(600,405);  glVertex2f(650,405)   
    glVertex2f(625,390);  glVertex2f(625,420)  

    glEnd()

def stair():

    glColor3f (0.67+0.40*brightness,
        0.53+0.04*brightness,
        0.06+0.01*brightness )

    glBegin(GL_TRIANGLES)

    glVertex2f(400,250); glVertex2f(300,300); glVertex2f(200,250)

    glVertex2f(500,300); glVertex2f(300,300); glVertex2f(400,250)

    glVertex2f(600,250); glVertex2f(500,300); glVertex2f(400,250)

    glVertex2f(700,300); glVertex2f(600,250); glVertex2f(500,300)

    glVertex2f(800,250); glVertex2f(700,300); glVertex2f(600,250)
    glEnd()

    
    glColor3f(0.1,0.0,0.1)
    glLineWidth(7)
    glBegin(GL_LINES)

    glVertex2f(260,280); glVertex2f(740,280)  
    glVertex2f(200,250); glVertex2f(800,250)  
    glVertex2f(300,300); glVertex2f(700,300)
    glEnd()

def treesin():
    glColor3f (0.30+0.40*brightness,
        0.20+0.35*brightness,
        0.15+0.25*brightness )
    glBegin(GL_TRIANGLES)

    glVertex2f(150,300); glVertex2f(100,350); glVertex2f(100,300)

    glVertex2f(150,350); glVertex2f(100,350); glVertex2f(150,300)

    glVertex2f(150,400); glVertex2f(100,350); glVertex2f(150,350)

    glVertex2f(150,400); glVertex2f(100,400); glVertex2f(100,350)

    glEnd()

    glColor3f (0.05+0.05*brightness,   
        0.35+0.59*brightness,
        0.25+0.15*brightness )
    glBegin(GL_TRIANGLES)
    glVertex2f(180,400); glVertex2f(130,490); glVertex2f(70,400)
    
    glEnd()
  
    glColor3f(0.17,0.1,0.13)
    glLineWidth(1)
    glBegin(GL_LINES)

    glVertex2f(100,300); glVertex2f(150,300)   
    glVertex2f(150,300); glVertex2f(150,400)   
    glVertex2f(150,400); glVertex2f(100,400)   
    glVertex2f(100,400); glVertex2f(100,300)   

    glVertex2f(180,400); glVertex2f(130,490)  
    glVertex2f(130,490); glVertex2f(70,400)   
    glVertex2f(70,400); glVertex2f(180,400)   

    glEnd()

    glColor3f (0.05+0.05*brightness,   
        0.35+0.59*brightness,   
        0.25+0.15*brightness)
    glBegin(GL_TRIANGLES)
   
    glVertex2f(170,460) ; glVertex2f(130,520)  ; glVertex2f(80,460)  
    glEnd()

    glColor3f(0.17,0.1,0.13)
    glBegin(GL_LINES)
    glVertex2f(170,460); glVertex2f(130,520)
    glVertex2f(130,520); glVertex2f(80,460)
    glVertex2f(80,460); glVertex2f(170,460)
    glEnd()

   
def d_rain():
    glLineWidth(2)
    glBegin(GL_LINES)
    for i, j in enumerate(rain):
        if i % 2 !=0:
            glColor3f (0.20+0.23*brightness,
                0.70 + 0.21*brightness,
                1.00)
        else:
            glColor3f(0.40+0.20*brightness,
                0.55+0.17*brightness,
                0.50+0.15*brightness)
        glVertex2f(j[0],j[1])
        glVertex2f(j[0]+speed,j[1]-63)
    glEnd()

def special_key_listener(key,x,y):
    global t_speed
    if key==GLUT_KEY_LEFT:
        t_speed=max(-47,t_speed-.75)  
    elif key == GLUT_KEY_RIGHT:
        t_speed=min(47,t_speed+.75)  
  
def kboard(key,x,y):
    global d_target
    if key==b'7':
        d_target=1.0   
    elif key==b'8':
        d_target=0.0  
    glutPostRedisplay()

def update_brightness():
    global brightness, speed, t_speed

    if brightness<d_target:
        brightness+=.007
    elif brightness>d_target:
        brightness-=.007

    if speed<t_speed:
        speed+=0.47
    elif speed>t_speed:
        speed-=0.47

    for j in rain:
        j[1]-=7
        j[0]+=speed
        if j[1]< 0:
            j[1]=1000
            j[0]=random.uniform(0, 1000)

        if j[0]>1000:  
            j[0]=0
        if j[0]<0:     
            j[0]=1000

    glutPostRedisplay()

def setup_projection():
    glViewport(0,0,1000,1000)     
    glMatrixMode(GL_PROJECTION)    
    glLoadIdentity()              
    glOrtho(0.0,1000,0.0,1000,0.0,1.0) 
    glMatrixMode(GL_MODELVIEW)    

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  
    glLoadIdentity()                                   
    setup_projection()                                 
    glColor3f(1.0,1.0,0.0)                            
    sky_bagr()
    ground() 
    grassocc() 
    wall() 
    roof()  
    doorh() 
    windowh() 
    stair()
    treesin()  
    d_rain()
    glutSwapBuffers()                                  

def main():
    glutInit()                               
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)        
    glutInitWindowSize(1000,1000)            
    glutInitWindowPosition(0,0)            
    glutCreateWindow(b"Task 1")    
    glutDisplayFunc(display)
    glutKeyboardFunc(kboard)                  
    glutSpecialFunc(special_key_listener)
    glutIdleFunc(update_brightness) 
    glutMainLoop()                         

if __name__ == "__main__":
    main()

