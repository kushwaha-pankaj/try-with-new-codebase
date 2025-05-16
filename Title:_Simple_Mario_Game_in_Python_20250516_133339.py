Title: Simple Mario Game in Python

```python
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
PLAYER_COLOR = (255, 0, 0)
BG_COLOR = (135, 206, 235)
FRAMERATE = 60
GRAVITY = 1
JUMP_STRENGTH = 15

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Mario Game")

# Player attributes
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - PLAYER_HEIGHT
player_vy = 0
is_jumping = False

# Game loop
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                player_vy = -JUMP_STRENGTH
                is_jumping = True

    # Apply gravity
    player_vy += GRAVITY
    player_y += player_vy

    # Ground collision
    if player_y >= SCREEN_HEIGHT - PLAYER_HEIGHT:
        player_y = SCREEN_HEIGHT - PLAYER_HEIGHT
        player_vy = 0
        is_jumping = False

    # Drawing
    screen.fill(BG_COLOR)
    player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)
    pygame.display.update()

    # Cap the frame rate
    clock.tick(FRAMERATE)

pygame.quit()
sys.exit()
```