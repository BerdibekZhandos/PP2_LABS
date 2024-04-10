import pygame
import sys 

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("The circle")
circle = pygame.draw.circle(screen,"red",(250,250),25)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("white")
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and 0<circle.left-5:
        circle.left-=20
    if keys[pygame.K_RIGHT] and circle.right+5<500:
        circle.right+=20
    if keys[pygame.K_DOWN] and circle.bottom+6<500:
        circle.bottom+=20
    if keys[pygame.K_UP] and 0<circle.top-5:
        circle.top-=20
    pygame.draw.circle(screen,"red",circle.center,25)
    pygame.display.update()
    pygame.time.Clock().tick(20)
