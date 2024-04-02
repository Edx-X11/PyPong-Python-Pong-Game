import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_SPEED = 0.5
BALL_SPEED_X = 0.25
BALL_SPEED_Y = 0.25

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Player variables
player1_score = 0
player2_score = 0

# Player objects
player1 = pygame.Rect(50, HEIGHT // 2 - 50, 10, 100)
player2 = pygame.Rect(WIDTH - 60, HEIGHT // 2 - 50, 10, 100)

# Ball object
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= PLAYER_SPEED
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += PLAYER_SPEED
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += PLAYER_SPEED

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Ball collision with players
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x = -ball_speed_x

    # Score update
    if ball.left <= 0:
        player2_score += 1
        ball_speed_x = BALL_SPEED_X
        ball_speed_y = BALL_SPEED_Y
        ball.x, ball.y = WIDTH // 2 - 15, HEIGHT // 2 - 15
    if ball.right >= WIDTH:
        player1_score += 1
        ball_speed_x = -BALL_SPEED_X
        ball_speed_y = BALL_SPEED_Y
        ball.x, ball.y = WIDTH // 2 - 15, HEIGHT // 2 - 15

    # Draw everything on the screen
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Display scores
    font = pygame.font.Font(None, 36)
    player1_text = font.render(str(player1_score), True, WHITE)
    player2_text = font.render(str(player2_score), True, WHITE)
    screen.blit(player1_text, (WIDTH // 4, 50))
    screen.blit(player2_text, (3 * WIDTH // 4, 50))

    pygame.display.flip()

    # Control the game's speed
    clock.tick(60)