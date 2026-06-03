from OpenGL.GL import *      
from OpenGL.GLUT import *   
from OpenGL.GLU import *     
import random
import time

WINDOW_WIDTH,WINDOW_HEIGHT=750,750
dia_x=random.randint(43,653)
dia_y=31
dia_speed=93 
init_speed=93   
dia_r,dia_g,dia_b=random.random(),random.random(),random.random()
cat_x=375
cat_y=680
cat_speed=267       
cheat_key=False
score=0
game_over=False
paused=False
last_time=time.time()

def find_zone(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    if abs(dx)>=abs(dy):
        if dx>=0 and dy>=0:
            zone=0     
        elif dx<0 and dy<0:
            zone=4
        elif dx>=0 and dy<0:
            zone = 7
        elif dx<0 and dy>=0:
            zone=3
        return zone
    else:
        if dx>=0 and dy>=0:
            zone=1
        elif dx<0 and dy<0:
            zone=5
        elif  dx>=0 and dy<0:
            zone = 6
        elif dx<0 and dy>=0:
            zone = 2
        return zone
         
def for_map(x,y,zone):
    if zone==0:
        xn=x
        yn=y
    elif zone==1:
        xn=y
        yn=x
    elif zone==2:
        xn=y
        yn=-x
    elif zone==3:
        xn=-x
        yn=y
    elif zone==4:
        xn=-x
        yn=-y
    elif zone==5:
        xn=-y
        yn=-x
    elif zone==6:
        xn=-y
        yn=x
    elif zone==7:
        xn=x
        yn=-y
    return xn,yn

def back_map(x,y,zone):
    if zone==0:
        xn=x
        yn=y
    elif zone==1:
        xn=y
        yn=x
    elif zone==2:
        xn=-y
        yn=x
    elif zone==3:
        xn=-x
        yn=y
    elif zone==4:
        xn=-x
        yn=-y
    elif zone==5:
        xn=-y
        yn=-x
    elif zone==6:
        xn=y
        yn=-x
    elif zone==7:
        xn=x
        yn=-y
    return xn,yn

def DrawLine(x1,y1,x2,y2,r=1,g=1,b=1,size=3.4):
    zone=find_zone(x1,y1,x2,y2)   
    x1new, y1new = for_map(x1,y1,zone)
    x2new, y2new = for_map(x2,y2,zone)
    if x1new>x2new:
        x1new,x2new=x2new,x1new
        y1new,y2new=y2new,y1new
    dx=x2new-x1new
    dy=y2new-y1new
    dinit=2*dy-dx
    deltaeast=2*dy
    deltanoeast=2*(dy-dx)
    x=x1new
    y=y1new

    glColor3f(r,g,b)        
    glPointSize(size)         
    glBegin(GL_POINTS)

    for i in range(int(x1new),int(x2new)+1): 
        if dinit>0:
            dinit+=deltanoeast
            x+=1
            y+=1
        else:
            dinit+=deltaeast
            x+=1
        prev_x,prev_y=back_map(x,y,zone)
        glVertex2f(prev_x,prev_y)

    glEnd()

def diamond_init(diax,diay,r,g,b):  
    top_po=(diax,diay-23)
    bottom_po=(diax,diay+23) 
    rig_po=(diax+17,diay)  
    lef_po=(diax-17,diay)  

    DrawLine(top_po[0],top_po[1],rig_po[0],rig_po[1],r,g,b)
    DrawLine(rig_po[0],rig_po[1],bottom_po[0],bottom_po[1],r,g,b)
    DrawLine(bottom_po[0],bottom_po[1],lef_po[0],lef_po[1],r,g,b)
    DrawLine(lef_po[0],lef_po[1],top_po[0],top_po[1],r,g,b)

def catcher_init(catx,caty,r,g,b):
    top_lepo=(catx-63,caty-13) 
    bot_lepo=(catx-47,caty+13)   
    top_ripo=(catx+63,caty-13)   
    bot_ripo=(catx+47,caty+13)  

    DrawLine(top_lepo[0],top_lepo[1],bot_lepo[0],bot_lepo[1],r,g,b)  
    DrawLine(bot_lepo[0],bot_lepo[1],bot_ripo[0],bot_ripo[1],r,g,b)  
    DrawLine(bot_ripo[0],bot_ripo[1],top_ripo[0],top_ripo[1],r,g,b)  
    DrawLine(top_ripo[0],top_ripo[1],top_lepo[0],top_lepo[1],r,g,b)  

def pause():
    DrawLine(362,21,362,71,1.0,0.67,0.0)   
    DrawLine(388,21,388,71,1.0,0.67,0.0)   

def play():
    DrawLine(362,21,388,46,1.0,0.67,0.0)  
    DrawLine(388,46,362,71,1.0,0.67,0.0)   
    DrawLine(362,21,362,71,1.0,0.67,0.0)  

def cross():
    DrawLine(653,21,713,71,1.0,0.0,0.0)  
    DrawLine(713,21,653,71,1.0,0.0,0.0)   

def restart():
    DrawLine(93,21,55,43,0.0,0.86,0.86)  
    DrawLine(55,43,93,61,0.0,0.86,0.86) 
    DrawLine(55,43,140,43,0.0,0.86,0.86) 

def collision_det():
    d_top=dia_y-23
    d_bot=dia_y+23
    d_left=dia_x-17
    d_right=dia_x+17
    c_top=cat_y-13
    c_bot=cat_y+13
    c_left=cat_x-63
    c_right=cat_x+63  
    return (d_left<c_right and d_right>c_left and d_top<c_bot and d_bot>c_top)

def new_diamond():
    global dia_x,dia_y,dia_r,dia_g,dia_b,dia_speed
    dia_x=random.randint(43,653)
    dia_y=31
    dia_r=random.uniform(0.53,1.0)
    dia_g=random.uniform(0.53,1.0)
    dia_b=random.uniform(0.51,1.0)
    if dia_speed<500:
        dia_speed+=10

def animate():
    global dia_y,game_over,score,last_time,cat_x
    curr=time.time()
    deltatime=curr-last_time
    last_time=curr
    if game_over==True or paused==True:
        glutPostRedisplay()
        return
    dia_y+=dia_speed*deltatime

    if collision_det()==True:
        score+= 1
        print(f"Score: {score}")
        new_diamond()
    elif dia_y>=750:
        game_over=True
        print(f"Game Over! Score: {score}")

    if cheat_key==True and game_over==False and paused==False:
        if cat_x<dia_x:
            cat_x=min(cat_x+2*cat_speed*deltatime,dia_x)
        elif cat_x> dia_x:
            cat_x=max(cat_x-2*cat_speed*deltatime,dia_x)
    glutPostRedisplay()

def special_key_listener(key,x,y):
    global cat_x
    if game_over==True or paused==True or cheat_key==True:
        return
    if key==GLUT_KEY_LEFT:
        cat_x=max(67,cat_x-cat_speed*0.04)  
    elif key==GLUT_KEY_RIGHT: 
        cat_x=min(684,cat_x+cat_speed*0.04) 
    glutPostRedisplay()

def keyboard_listener(key,x,y):
    global cheat_key
    if key==b'c':
        cheat_key=not cheat_key
    glutPostRedisplay()

def mouse_listener(button,state,x,y):
    global game_over,paused,score,dia_speed,cat_x,cheat_key
    global dia_x,dia_y,dia_r,dia_g,dia_b
    
    if button==GLUT_LEFT_BUTTON and state==GLUT_DOWN:
        if 653<=x<=713 and 21<=y<=71:
            print(f"Goodbye! Score: {score}")
            glutLeaveMainLoop()
        elif 362<=x<=388 and 21<=y<=71:
            if game_over==False:
                paused=not paused
        elif 55<=x<=140 and 21<=y<= 61:
            print("Starting Over!")
            game_over=False
            paused=False
            score=0
            dia_speed=init_speed
            cat_x=375
            cheat_key=False 
            new_diamond()
    glutPostRedisplay()

def setup_projection():
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,750,750,0,0,1)
    glMatrixMode(GL_MODELVIEW)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    setup_projection()
    restart()
    cross()
    if paused==True: 
        play()
    else:      
        pause()
    if game_over==False:
        diamond_init(dia_x,dia_y,dia_r,dia_g,dia_b)
    if game_over==True: 
        catcher_init(cat_x,cat_y,1.0,0.0,0.0)
    else:        
        catcher_init(cat_x,cat_y,0.97,0.71,1.0)
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(730,10)
    glutCreateWindow(b"Catch the diamond")
    glutDisplayFunc(display)
    glutSpecialFunc(special_key_listener)
    glutMouseFunc(mouse_listener)
    glutKeyboardFunc(keyboard_listener)
    glutIdleFunc(animate)
    glutMainLoop()

if __name__ == "__main__":
    main()



