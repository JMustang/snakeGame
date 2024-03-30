import pygame, sys, time, random

speed = 15

# Temanho da tela

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

fps_controller = pygame.time.Clock()

# Tamanho dos blocos
square_size = 20

# Coordenadas da cobra


def init_vars():
    global head_pos, snake_body, food_pos, food_spawn, score, direction
    direction = "RIGHT"
    head_pos = [120, 60]
    snake_body = [[120, 60]]
    food_pos = [
        random.randrange(1, (frame_size_x // square_size)) * square_size,
        random.randrange(1, (frame_size_y // square_size)) * square_size,
    ]
    food_spawn = True
    score = 0


init_vars()


def show_score():
    print("Showing score")


# Loop do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if (
                event.key == pygame.K_UP
                or event.key == ord("w")
                and direction != "DOWN"
            ):
                direction = "UP"
            elif (
                event.key == pygame.K_DOWN
                or event.key == ord("s")
                and direction != "UP"
            ):
                direction = "DOWN"
            elif (
                event.key == pygame.K_LEFT
                or event.key == ord("a")
                and direction != "RGHT"
            ):
                direction = "LEFT"
            elif (
                event.key == pygame.K_RIGHT
                or event.key == ord("d")
                and direction != "LEFT"
            ):
                direction = "RIGHT"

    if direction == "UP":
        head_pos[1] -= square_size
    elif direction == "DOWN":
        head_pos[1] += square_size
    elif direction == "LEFT":
        head_pos[0] -= square_size
    else:
        head_pos[0] += square_size

    if head_pos[0] < 0:
        head_pos[0] = frame_size_x - square_size
    elif head_pos[0] > frame_size_x - square_size:
        head_pos[0] = 0
    elif head_pos[1] < 0:
        head_pos[1] = frame_size_y - square_size
    elif head_pos[1] > frame_size_y - square_size:
        head_pos[1] = 0

    # Comendo macao
    snake_body.insert(0, list(head_pos))
    if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn macao
    if not food_spawn:
        food_pos = [
            random.randrange(1, (frame_size_x // square_size)) * square_size,
            random.randrange(1, (frame_size_y // square_size)) * square_size,
        ]
