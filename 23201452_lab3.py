import math
import random
from OpenGL.GL   import *
from OpenGL.GLUT import *
from OpenGL.GLU  import *
width=1000
height=800

gri_length=600
no_of_cells=7
ce_size=gri_length / no_of_cells
boundary_height=71

px= 0.0
py= 0.0
p_ang= 0.0
P_SPEED= 12.0
P_ROT = 3.0
E_BODY_R= 26
E_HEAD_R= 13
pulse_t=0.0
PULSE_SPD=3.0
enemies= []
bullets = []
B_SPEED = 13.0
B_SIZE= 9
MAX_DIST= gri_length *1.2
player_life= 5
game_score= 0
bullet_missed = 0
game_over = False
cam_h= 0.0
cam_v= 39.0
cam_r=1100.0
CAM_R_MIN = 600.0
CAM_R_MAX= 1300.0
cam_z= 0.0
CAM_Z_MIN= -200.0
CAM_Z_MAX= 400.0
fovY = 71
first_person= False
cheat_mode= False
cheat_cam_follow = False
cheat_fire_timer = 0
CHEAT_FIRE_RATE = 9

def draw_grid():
    total = no_of_cells * 2
    glBegin(GL_QUADS)
    for row in range(total):
        for col in range(total):
            x0 = -gri_length + col * ce_size
            y0 = -gri_length + row * ce_size
            x1, y1 = x0 + ce_size, y0 + ce_size
            if (row + col) % 2 == 0:
                glColor3f(0.82, 0.72, 1.0)
            else:
                glColor3f(1.0, 1.0, 1.0)
            glVertex3f(x0, y0, 0)
            glVertex3f(x1, y0, 0)
            glVertex3f(x1, y1, 0)
            glVertex3f(x0, y1, 0)
    glEnd()

def draw_boundaries():
    G, H = gri_length, boundary_height
    def wall(x0, y0, x1, y1, r, g, b):
        glColor3f(r, g, b)
        glBegin(GL_QUADS)
        glVertex3f(x0, y0, 0); glVertex3f(x1, y1, 0)
        glVertex3f(x1, y1, H); glVertex3f(x0, y0, H)
        glEnd()
    wall(-G,  G,  G,  G,  0,   1,   1  )
    wall(-G, -G,  G, -G,  1,   1,   1  )
    wall(-G, -G, -G,  G,  0.2, 0.4, 1  )
    wall( G, -G,  G,  G,  0.1, 0.8, 0.1)

def draw_player():
    glPushMatrix()
    glTranslatef(px, py, 0)

    if game_over:
        glTranslatef(0, 0, 40)
        glRotatef(90, 1, 0, 0)
    else:
        glRotatef(-p_ang, 0, 0, 1)

    quad=gluNewQuadric()

    glColor3f(0.1, 0.1, 0.9)
    glPushMatrix()
    glTranslatef(-11, 0, 45)
    glRotatef(180, 1, 0, 0)
    gluCylinder(quad, 13, 5, 35, 23, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(11, 0, 45)
    glRotatef(180, 1, 0, 0)
    gluCylinder(quad, 13, 5, 35, 23, 10)
    glPopMatrix()

    glPushMatrix()
    glColor3f(0.3, 0.6, 0.3)
    glTranslatef(0, 0, 41)
    gluCylinder(quad, 15, 14, 32, 34, 15)
    glPopMatrix()

    glColor3f(0.85, 0.70, 0.60)
    glPushMatrix()
    glTranslatef(-15, 5, 75)
    glRotatef(-90, 1, 0, 0)
    gluCylinder(quad, 10, 4, 60, 15, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(15, 5, 75)
    glRotatef(-90, 1, 0, 0)
    gluCylinder(quad, 10, 4, 60, 15, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 8, 75)
    glRotatef(-90, 1, 0, 0)
    if cheat_mode:
        glColor3f(1.0, 0.84, 0.0)
    else:
        glColor3f(0.5, 0.5, 0.5)
    gluCylinder(quad, 8, 3, 70, 10, 5)
    glPopMatrix()

    if not first_person:
        glPushMatrix()
        glTranslatef(0, 0, 90)
        glColor3f(0, 0, 0)
        gluSphere(quad, 17, 23, 15)
        glPopMatrix()

    glPopMatrix()

def draw_enemies():
    scale = 1.0 + 0.30 * math.sin(math.radians(pulse_t))
    quad  = gluNewQuadric()
    for e in enemies:
        glPushMatrix()
        glTranslatef(e["x"], e["y"], 0)
        glScalef(scale, scale, scale)
        glPushMatrix()
        glTranslatef(0, 0, E_BODY_R)
        glColor3f(0.88, 0.08, 0.08)
        gluSphere(quad, E_BODY_R, 14, 14)
        glPopMatrix()
        glPushMatrix()
        glTranslatef(0, 0, E_BODY_R * 2 + E_HEAD_R)
        glColor3f(0.05, 0.05, 0.05)
        gluSphere(quad, E_HEAD_R, 10, 10)
        glPopMatrix()
        glPopMatrix()

def draw_bullets():
    for b in bullets:
        glPushMatrix()
        glTranslatef(b["x"], b["y"], b["z"])
        glColor3f(1.0, 0.85, 0.0)
        glutSolidCube(B_SIZE)
        glPopMatrix()
def draw_text(x,y,text,color=(1,1,1)):
    glColor3f(*color)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
def draw_text_show():
    if game_over:
        draw_text(10, height - 26,
                  f"Game is Over. Your Score is {game_score}.",
                  color=(1.0, 0.35, 0.35))
        draw_text(10, height - 52,
                  'Press "R" to RESTART the Game.',
                  color=(1.0, 1.0, 1.0))
    else:
        draw_text(10, height - 26, f"Player Life Remaining: {player_life}")
        draw_text(10, height - 52, f"Game Score: {game_score}")
        draw_text(10, height - 78, f"Player Bullet Missed: {bullet_missed}")

def gun_dir():
    rad = math.radians(p_ang)
    return math.sin(rad), math.cos(rad)

def angle_to_enemy(tx,ty):
    return math.degrees(math.atan2(tx - px, ty - py)) % 360.0

def spawn_enemy():
    while True:
        x = random.uniform(-gri_length + 60, gri_length - 60)
        y = random.uniform(-gri_length + 60, gri_length - 60)
        if math.hypot(x - px, y - py) > 300:
            return {"x": x, "y": y}
def init_enemies():
    global enemies
    enemies = [spawn_enemy() for _ in range(5)]
    print(f"Remaining Player Life: {player_life}")
def fire(is_cheat=False):
    if game_over:
        return
    dx, dy = gun_dir()
    bullets.append({
        "x":    px + dx * 60,
        "y":    py + dy * 60,
        "z":    85,
        "dx":   dx,
        "dy":   dy,
        "dist": 0.0,
        "cheat": is_cheat
    })
    print("Player Bullet Fired!")
def update_enemies():
    global player_life

    for e in enemies[:]:
        dx = px - e["x"]
        dy = py - e["y"]
        dist = math.hypot(dx, dy)

        if dist != 0:
            if dist > 67:
                e["x"] += dx / dist * 0.35
                e["y"] += dy / dist * 0.35

        if dist < 67:
            if not cheat_mode:
                player_life -= 1
                print(f"Remaining Player Life: {player_life}")

            enemies.remove(e)
            enemies.append(spawn_enemy())
def cheat_aim():
    global p_ang
    if game_over or not enemies:
        return
    nearest = min(enemies, key=lambda e: math.hypot(e["x"] - px, e["y"] - py))
    p_ang = angle_to_enemy(nearest["x"], nearest["y"])

def cheat_fire():
    if game_over or not enemies:
        return
    fire(is_cheat=True)


def enemy_in_sight(threshold=3.0):
    dx, dy = gun_dir()
    for e in enemies:
        ex = e["x"] - px
        ey = e["y"] - py
        dist = math.hypot(ex, ey)
        if dist == 0:
            continue
        ex /= dist
        ey /= dist
        dot = dx * ex + dy * ey
        angle = math.degrees(math.acos(max(-1, min(1, dot))))
        if angle < threshold:
            return True
    return False

def bullet_enemy_collision():
    global game_score
    for b in bullets[:]:
        for e in enemies[:]:
            if math.hypot(b["x"] - e["x"], b["y"] - e["y"]) < 30:
                try:
                    bullets.remove(b)
                except:
                    pass
                enemies.remove(e)
                enemies.append(spawn_enemy())
                game_score += 1
                break

def check_game_over():
    global game_over, cheat_mode, cheat_cam_follow, first_person
    if cheat_mode:
        return
    if player_life <= 0 or bullet_missed >= 10:
        if not game_over:
            print("GAME OVER")
            cheat_mode = False
            cheat_cam_follow = False
            first_person = False
        game_over = True

def reset_game():
    global px, py, p_ang, bullets, enemies
    global player_life, game_score, bullet_missed, game_over
    global cheat_mode, cheat_cam_follow, cheat_fire_timer
    global first_person, cam_h, cam_r, cam_z

    px, py, p_ang    = 0.0, 0.0, 0.0
    bullets.clear()
    enemies.clear()
    init_enemies()
    player_life      = 5
    game_score       = 0
    bullet_missed    = 0
    game_over        = False
    cheat_mode       = False
    cheat_cam_follow = False
    cheat_fire_timer = 0
    first_person     = False
    cam_h            = 0.0
    cam_r            = 1100.0
    cam_z            = 0.0
    print("\nGame Reset")
    print(f"Remaining Player Life: {player_life}")

def setup_camera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fovY, width / height,1.0,5000.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    if first_person:
        dx, dy = gun_dir()
        if cheat_mode:
            ez = 100.0     
            if cheat_cam_follow:
                lx = px + dx * 200
                ly = py + dy * 200
            else:           
                lx = px + 0 
                ly = py + 200         
            lz = 85.0 
        else:      
            ez = 107.0
            lx = px + dx * 100
            ly = py + dy * 100
            lz = 100.0

        gluLookAt(px, py, ez, lx, ly, lz, 0, 0, 1)
        
    else:
        rh = math.radians(cam_h)
        rv = math.radians(cam_v)
        cx = cam_r * math.cos(rv) * math.sin(rh)
        cy = -cam_r * math.cos(rv) * math.cos(rh)
        cz = cam_r * math.sin(rv) + cam_z
        gluLookAt(cx, cy, cz, 0, 0, 0, 0, 0, 1)

def keyboardListener(key, x, y):
    global px, py, p_ang
    global cheat_mode, cheat_cam_follow, cheat_fire_timer
    global first_person

    if key in (b'r', b'R'):
        reset_game()
        return

    if game_over:
        return

    if key in (b'c', b'C'):
        cheat_mode = not cheat_mode
        if not cheat_mode:
            cheat_cam_follow = False
            first_person     = False
        print(f"[Cheat Mode {'ON' if cheat_mode else 'OFF'}]")
        return

    if key in (b'v', b'V'):
        if cheat_mode and first_person:
            cheat_cam_follow = not cheat_cam_follow
        return

    dx, dy = gun_dir()

    if key in (b'w', b'W'):
        nx, ny = px + dx * P_SPEED, py + dy * P_SPEED
        if abs(nx) < gri_length - 30 and abs(ny) < gri_length - 30:
            px, py = nx, ny

    elif key in (b's', b'S'):
        nx, ny = px - dx * P_SPEED, py - dy * P_SPEED
        if abs(nx) < gri_length - 30 and abs(ny) < gri_length - 30:
            px, py = nx, ny

    elif key in (b'a', b'A') and not cheat_mode:
        p_ang = (p_ang - P_ROT) % 360.0

    elif key in (b'd', b'D') and not cheat_mode:
        p_ang = (p_ang + P_ROT) % 360.0

def specialKeyListener(key, x, y):
    global cam_h, cam_z

    if game_over:
        return

    if not first_person:
        if   key == GLUT_KEY_LEFT:  cam_h -= 1.5
        elif key == GLUT_KEY_RIGHT: cam_h += 1.5
        elif key == GLUT_KEY_UP:
            cam_z = min(cam_z + 10.0, CAM_Z_MAX)
        elif key == GLUT_KEY_DOWN:
            cam_z = max(cam_z - 10.0, CAM_Z_MIN)
        glutPostRedisplay()

def mouseListener(button, state, x, y):
    global first_person, cheat_cam_follow

    if game_over:
        return

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if not cheat_mode:
            fire(is_cheat=False)

    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        first_person = not first_person
        if not first_person:
            cheat_cam_follow = False


def idle():
    global pulse_t, bullets, bullet_missed, cheat_fire_timer, p_ang

    pulse_t = (pulse_t + PULSE_SPD) % 360.0

    if cheat_mode and not game_over:
     
        p_ang = (p_ang + 2.0) % 360.0

        if enemy_in_sight():
            cheat_fire_timer += 1
            if cheat_fire_timer >= CHEAT_FIRE_RATE:
                cheat_fire_timer = 0
                fire(is_cheat=True)

    keep = []
    for b in bullets:
        b["x"] += b["dx"] * B_SPEED
        b["y"] += b["dy"] * B_SPEED
        b["dist"] += B_SPEED

        alive = (b["dist"] < MAX_DIST and
                 abs(b["x"]) < gri_length and
                 abs(b["y"]) < gri_length)

        if alive:
            keep.append(b)
        else:
            if not game_over and not b.get("cheat", False):
                bullet_missed += 1
                print(f"Bullet missed: {bullet_missed}")

    bullets = keep

    if not game_over:
        update_enemies()
        bullet_enemy_collision()
        check_game_over()

    glutPostRedisplay()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    setup_camera()
    draw_grid()
    draw_boundaries()
    draw_player()
    draw_enemies()
    draw_bullets()
    draw_text_show()
    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Assignment03")
    init_enemies()
    glutDisplayFunc(showScreen)
    glutIdleFunc(idle)
    glutKeyboardFunc(keyboardListener)
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseListener)
    glutMainLoop()

if __name__ == "__main__":
    main()