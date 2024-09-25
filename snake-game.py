import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Snake settings
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction

# Food settings
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
food_spawn = True

# Game settings
clock = pygame.time.Clock()
speed = 15

# Game Over function
def game_over():
    pygame.quit()
    quit()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Validate direction
    if change_to == 'UP' and not snake_direction == 'DOWN':
        snake_direction = 'UP'
    if change_to == 'DOWN' and not snake_direction == 'UP':
        snake_direction = 'DOWN'
    if change_to == 'LEFT' and not snake_direction == 'RIGHT':
        snake_direction = 'LEFT'
    if change_to == 'RIGHT' and not snake_direction == 'LEFT':
        snake_direction = 'RIGHT'

    # Move the snake
    if snake_direction == 'UP':
        snake_pos[1] -= 10
    if snake_direction == 'DOWN':
        snake_pos[1] += 10
    if snake_direction == 'LEFT':
        snake_pos[0] -= 10
    if snake_direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
    food_spawn = True

    # Background
    screen.fill(black)

    # Draw snake
    for pos in snake_body:
        pygame.draw.rect(screen, white, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw food
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > width-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > height-10:
        game_over()

    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    clock.tick(speed)