import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clicker Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.Font(None, 36)

# Game variables
score = 0
click_power = 1
multiplier = 1.0
auto_clickers = 0  # Number of auto clickers owned
auto_clicker_power = 1  # Base power of each auto clicker
auto_clicker_cost = 150  # Starting cost of auto clickers
last_auto_click = 0  # Timer for auto clickers

# Button positions
button_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 - 50, 200, 100)
multiplier_button = pygame.Rect(WIDTH//2 - 150, HEIGHT//2 + 100, 200, 50)
power_button = pygame.Rect(WIDTH//2 + 50, HEIGHT//2 + 100, 200, 50)
auto_button = pygame.Rect(WIDTH//2 - 50, HEIGHT//2 + 170, 200, 50)
gamble_button = pygame.Rect(WIDTH//2 - 50, HEIGHT//2 + 240, 200, 50)

# Gambling variables
import random
last_gamble_result = None
gamble_cooldown = 0

# Upgrade costs
multiplier_cost = 100
power_cost = 50

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                score += math.floor(click_power * multiplier)
            elif multiplier_button.collidepoint(event.pos) and score >= multiplier_cost:
                score -= multiplier_cost
                multiplier *= 1.05
                multiplier_cost = math.floor(multiplier_cost * 1.5)
            elif power_button.collidepoint(event.pos) and score >= power_cost:
                score -= power_cost
                click_power += 1
                power_cost = math.floor(power_cost * 1.3)
            elif auto_button.collidepoint(event.pos) and score >= auto_clicker_cost:
                score -= auto_clicker_cost
                auto_clickers += 1
                auto_clicker_cost = math.floor(auto_clicker_cost * 1.2)
            elif gamble_button.collidepoint(event.pos) and score > 0 and gamble_cooldown <= 0:
                if random.random() < 0.3:  # 30% chance to win
                    score *= 3
                    last_gamble_result = "Won! Score Tripled!"
                else:
                    score = 0
                    last_gamble_result = "Lost Everything!"
                gamble_cooldown = 60  # Set cooldown to prevent spam

    # Auto clicker logic (clicks once per second)
    current_time = pygame.time.get_ticks()
    if current_time - last_auto_click >= 1000:  # 1000ms = 1 second
        score += math.floor((auto_clickers * auto_clicker_power) * multiplier)
        last_auto_click = current_time

    # Clear the screen
    screen.fill(WHITE)

    # Draw the main button
    pygame.draw.rect(screen, (0, 100, 0), button_rect)
    button_text = font.render("Click Me!", True, WHITE)
    screen.blit(button_text, (button_rect.centerx - button_text.get_width() // 2, button_rect.centery - button_text.get_height() // 2))


    # Draw score and stats
    score_text = font.render(f"Score: {score}", True, BLACK)
    power_text = font.render(f"Click Power: {click_power}", True, BLACK)
    multiplier_text = font.render(f"Multiplier: {multiplier:.2f}x", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(power_text, (10, 50))
    screen.blit(multiplier_text, (10, 90))

    # Draw upgrade buttons
    pygame.draw.rect(screen, (100, 200, 100), multiplier_button)
    pygame.draw.rect(screen, (200, 100, 100), power_button)

    mult_button_text = font.render(f"Buy 5% Multi ({multiplier_cost})", True, WHITE)
    power_button_text = font.render(f"Buy +1 Power ({power_cost})", True, WHITE)
    screen.blit(mult_button_text, (multiplier_button.x + 10, multiplier_button.y + 15))
    screen.blit(power_button_text, (power_button.x + 10, power_button.y + 15))

    # Draw auto clicker button and stats
    pygame.draw.rect(screen, (100, 100, 200), auto_button)
    auto_button_text = font.render(f"Buy Auto ({auto_clicker_cost})", True, WHITE)
    auto_stats = font.render(f"Auto Clickers: {auto_clickers}", True, BLACK)
    screen.blit(auto_button_text, (auto_button.x + 10, auto_button.y + 15))
    screen.blit(auto_stats, (10, 130))

    # Draw gambling button
    button_color = (200, 50, 50) if gamble_cooldown <= 0 else (100, 50, 50)
    pygame.draw.rect(screen, button_color, gamble_button)
    gamble_text = font.render("Gamble All! (30%)", True, WHITE)
    screen.blit(gamble_text, (gamble_button.x + 10, gamble_button.y + 15))

    # Show gambling result
    if last_gamble_result:
        result_text = font.render(last_gamble_result, True, BLACK)
        screen.blit(result_text, (10, 170))

    # Update cooldown
    if gamble_cooldown > 0:
        gamble_cooldown -= 1

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()