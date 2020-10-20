import pygame
pygame.init()

screen_x = 1000
screen_y = 600

win = pygame.display.set_mode((screen_x, screen_y))

pygame.display.set_caption("Mans go Neeeooowwwww")

width = 40
height = 60
x = (screen_x // 2) - (width // 2)
y = (screen_y // 2) - (height // 2)
vel = 5
isJump = False
jumpCount = 20

run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > 0:
        x -= vel
        left = True
        right = False
    if keys[pygame.K_d] and x < screen_x - width:
        x += vel
    
    if not(isJump):
        if keys[pygame.K_w] and y > 0:
            y -= vel
        if keys[pygame.K_s] and y < screen_y - height:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -20:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.05 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 20
    

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
