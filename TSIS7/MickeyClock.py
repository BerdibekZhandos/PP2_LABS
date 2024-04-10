import pygame
import os
import time
pygame.init()

from datetime import datetime

x = datetime.now()
minutestime = x.strftime("%M")
secondstime = x.strftime("%S")
print(minutestime)
print(secondstime)
monitor=pygame.display.set_mode((700,600))
pygame.display.set_caption("MickeyClock")

clock = pygame.time.Clock()
HIGHT=600
LENGHT=700

mickey_image=pygame.image.load(os.path.join('MickeyClock.jpeg'))
minutes_image=pygame.image.load(os.path.join('minutes_hand.png'))
seconds_image=pygame.image.load(os.path.join('seconds_hand.png'))

mickey = pygame.transform.scale(mickey_image,(LENGHT,HIGHT))
minutes = pygame.transform.scale(minutes_image,(70,400))
seconds = pygame.transform.scale(seconds_image,(120,280))
x, y = 350, 300
# Set the initial rotation angle to 0
angle2 = (int(minutestime)*-1)*6
angle = (int(secondstime)*-1)*6
# Set the rotation speed to 1 degree per second

check = True

while check:
    monitor.fill(("White"))
    for action in pygame.event.get():
        if action.type==pygame.QUIT:
            check = False
            pygame.quit()


    rotated_seconds = pygame.transform.rotate(seconds, angle2)
    rotated_minutes = pygame.transform.rotate(minutes, angle)
    monitor.blit(mickey, (0,0))
    monitor.blit(rotated_seconds, (x-int(rotated_seconds.get_width()/2), y-int(rotated_seconds.get_height()/2)))
    monitor.blit(rotated_minutes, (x-int(rotated_minutes.get_width()/2), y-int(rotated_minutes.get_height()/2)))

    pygame.display.update() 
        # Wait for a short amount of time to simulate 1 degree per second
    time.sleep(1)

    # Increase the rotation angle by 1 degree
    angle -= 6

    if angle%360 == 0:
        angle2-=6
