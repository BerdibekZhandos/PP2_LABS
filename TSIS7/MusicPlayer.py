import pygame
import sys
import os

pygame.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Music Player")
font = pygame.font.Font(None, 36)
song = ["TF2_Meme_Audio","Better Call Saul","Breaking Bad"]

resume = pygame.image.load(os.path.join("play-button.png"))
stop = pygame.image.load(os.path.join("pause.png"))
next_m = pygame.image.load(os.path.join("next.png"))
prev_m = pygame.image.load(os.path.join("back.png"))
pause= [resume,stop]
music = ["TF2_Meme_Audio.mp3", "Better Call Saul.mp3", "Breaking Bad.mp3"]
current = 0
s = 1

pygame.mixer.music.load(music[current])
pygame.mixer.music.play()
MUSIC_END = pygame.USEREVENT+1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           exit() 
        elif event.type == MUSIC_END:
            current = (current + 1) % len(music)
            pygame.mixer.music.load(music[current])
            pygame.mixer.music.play()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.unpause()
                s = 1
            elif event.key == pygame.K_ESCAPE:
                pygame.mixer.music.pause()
                s = 0
            elif event.key == pygame.K_RIGHT:
                current = (current + 1) % len(music)
                pygame.mixer.music.load(music[current])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current = (current - 1) % len(music)
                pygame.mixer.music.load(music[current])
                pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(MUSIC_END)
    screen.fill("White")
    text = font.render(song[current], True, "Black")
    screen.blit(text, (90, 50))
    screen.blit(pause[s],(175,100))
    screen.blit(prev_m,(100,100))
    screen.blit(next_m,(250,100))

    pygame.display.update()
