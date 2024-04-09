import pygame
import sys 
import datetime

pygame.init()
screen = pygame.display.set_mode((700,525))
pygame.display.set_caption("The Mickey Clock")
mickey = pygame.image.load(r"C:\Users\Ruslan\Desktop\Git\py_repo\tsis7\mickeyclock2.jpg")
hand2 = pygame.image.load(r"C:\Users\Ruslan\Desktop\Git\py_repo\tsis7\minute_hand.png")
hand1 = pygame.image.load(r"C:\Users\Ruslan\Desktop\Git\py_repo\tsis7\hour_hand.png")
def angle1():
    t = datetime.datetime.now().time()
    return -1*(30*(t.hour%12)+(t.minute/2))
def angle2():
    t = datetime.datetime.now().time()
    return -1*(6*t.minute+t.second/10)
def rotate1():
    rotated = pygame.transform.rotate(hand1,angle1()+90)
    rect = rotated.get_rect(center = mickey.get_rect().center)
    screen.blit(rotated,rect)
def rotate2():
    rotated = pygame.transform.rotate(hand2,angle2()+90)
    rect = rotated.get_rect(center = mickey.get_rect().center)
    screen.blit(rotated,rect)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(mickey,(0,0))
    rotate1()
    rotate2()
    pygame.display.update()
