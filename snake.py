import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen settings
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game with Pause')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)

# Game settings
snake_block = 10  # Size of each segment of the snake
snake_speed = 15  # Speed of the snake
clock = pygame.time.Clock()  # Game clock for controlling the game speed
font_style = pygame.font.SysFont(None, 35)  # Font for displaying text

# Display the score on the screen
def show_score(score):
    score_text = font_style.render("Score: " + str(score), True, red)
    screen.blit(score_text, [0, 0])

# Display the pause menu
def show_pause():
    pause_text = font_style.render("Game Paused. Press P to Resume", True, red)
    screen.blit(pause_text, [width / 6, height / 3])
    pygame.display.update()

# Pause function
def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Resume game on pressing 'P'
                    paused = False
        # Display pause message
        screen.fill(black)
        show_pause()
        clock.tick(5)

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initial snake position in the center of the screen
    x, y = width / 2, height / 2
    x_change, y_change = 0, 0  # Movement directions

    # Snake body and initial length
    snake = []
    length_of_snake = 1

    # Generate food at a random location
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Main game loop
    while not game_over:

        # Check if the game is in a "game over" state
        while game_close:
            screen.fill(black)
            msg = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, red)
            screen.blit(msg, [width / 6, height / 3])
            show_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Quit game
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # Restart game
                        game_loop()

        # Event handling for movement and pausing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change, y_change = -snake_block, 0
                elif event.key == pygame.K_RIGHT:
                    x_change, y_change = snake_block, 0
                elif event.key == pygame.K_UP:
                    x_change, y_change = 0, -snake_block
                elif event.key == pygame.K_DOWN:
                    x_change, y_change = 0, snake_block
                elif event.key == pygame.K_p:  # Pause the game on 'P'
                    pause()

        # Check for boundaries; if hit, end the game
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        # Update the snake's position
        x += x_change
        y += y_change
        screen.fill(black)

        # Draw the food
        pygame.draw.rect(screen, green, [food_x, food_y, snake_block, snake_block])

        # Add the new position to the snake
        snake_head = [x, y]
        snake.append(snake_head)

        # Remove the oldest segment if the snake is longer than its length
        if len(snake) > length_of_snake:
            del snake[0]

        # Check for collisions with itself
        for segment in snake[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw the snake
        for segment in snake:
            pygame.draw.rect(screen, white, [segment[0], segment[1], snake_block, snake_block])

        # Display score
        show_score(length_of_snake - 1)
        pygame.display.update()

        # Check if the snake has eaten the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1  # Increase the length of the snake

        # Control the game speed
        clock.tick(snake_speed)

    # Exit pygame
    pygame.quit()
    quit()

# Run the game
game_loop()
