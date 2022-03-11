import pygame
pygame.init()
pygame.mixer.music.load('Ex.021_Tocando_Um_MP3.mp3')
pygame.mixer.music.play()
pygame.event.wait()