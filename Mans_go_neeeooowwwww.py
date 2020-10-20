import pygame
pygame.init()

screen_x = 1000
screen_y = 600

win = pygame.display.set_mode((screen_x, screen_y))

pygame.display.set_caption("Mans go Neeeooowwwww")

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_vel = 5
        self.y_vel = 5
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.up = False
        self.left = False
        self.right = False
        self.down = False

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, 40, 60))
        self.hitbox = (self.x, self.y, 40, 60)

class projectile(object):
    def __init__(self, x, y, radius, color, x_dir, y_dir):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.x_vel = 10 * x_dir
        self.y_vel = 10 * y_dir

    def draw(self, win):
        pygame.draw.circle(win, self.color,
                           (int(self.x), int(self.y)), self.radius)

def redrawGameWindow():
    pygame.draw.rect(win, (0, 0, 0,), (0, 0, screen_x, screen_y))
    mans.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

#mainloop
mans = player(screen_x // 2, screen_y // 2, 40, 60)
bullets = []
up = False
left = False
right = False
down = False
run = True
while run:
    pygame.time.delay(16)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if (bullet.x < screen_x and bullet.x > 0) and (bullet.y < screen_y and bullet.y > 0):
            bullet.x += bullet.speed * bullet.x_dir
            bullet.y += bullet.speed * bullet.y_dir
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and mans.x > 0:
        mans.x -= mans.x_vel
        mans.up = False
        mans.left = True
        mans.right = False
        mans.down = False
    if keys[pygame.K_d] and mans.x < screen_x - mans.width:
        mans.x += mans.x_vel
        mans.up = False
        mans.left = False
        mans.right = True
        mans.down = False
    
    if keys[pygame.K_w] and mans.y > 0:
        mans.y -= mans.y_vel
        mans.up = True
        mans.left = False
        mans.right = False
        mans.down = False
    if keys[pygame.K_s] and mans.y < screen_y - mans.height:
        mans.y += mans.y_vel
        mans.up = False
        mans.left = False
        mans.right = False
        mans.down = True

    if keys[pygame.K_SPACE]:
        if up:
            y_dir = -1
        if left:
            x_dir = -1
        if down:
            y_dir = 1
        if right:
            x_dir = 1
        else:
            pass
        if len(bullets) < 1000:
            bullets.append(projectile(round(mans.x + mans.width // 2),
                                      round(mans.y + mans.height // 2),
                                      6, (0, 0, 255), x_dir, y_dir))

    redrawGameWindow()

pygame.quit()
