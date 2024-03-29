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

# Iniciando a tela do jogo

pygame.display.set_caption("Snake Eater")
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# Cores

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
