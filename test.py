import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncing Circle")

# Define colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Circle properties
circle_radius = 20
circle_color = WHITE

# Initial circle position and velocity
circle_x = SCREEN_WIDTH // 2
circle_y = SCREEN_HEIGHT // 2
circle_velocity_x = 5
circle_velocity_y = 5

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update circle position
    circle_x += circle_velocity_x
    circle_y += circle_velocity_y

    # Bounce off the walls
    if circle_x - circle_radius < 0 or circle_x + circle_radius > SCREEN_WIDTH:
        circle_velocity_x = -circle_velocity_x

    if circle_y - circle_radius < 0 or circle_y + circle_radius > SCREEN_HEIGHT:
        circle_velocity_y = -circle_velocity_y

    # Set the background color
    screen.fill(BLUE)

    # Draw the circle
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

    # Update the display
    pygame.display.flip()
