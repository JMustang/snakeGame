import pygame, sys, time, random

speed = 15

# temanho da tela

frame_size_x = 720
frame_size_y = 480


check_errors = pygame.init()

if check_errors[1] > 0:
    print(f"Error {check_errors[1]}")
else:
    print("Game successfully initialized")
