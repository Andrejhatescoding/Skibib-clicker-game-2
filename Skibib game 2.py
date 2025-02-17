import pygame
import time
import random  # We'll need random for the gambling feature

# Initialize pygame
pygame.init()

# Set up display
screen_width = 700
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Clicker Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define fonts
font = pygame.font.Font(None, 36)

class ClickerGame:
    def __init__(self):
        self.score = 0
        self.score_per_click = 1
        self.cost_per_upgrade = 10
        self.cost_per_upgrade2 = 500
        self.cost_per_upgrade3 = 10000
        self.cost_per_upgrade4 = 50000
        self.cost_per_upgrade5 = 250000
        self.auto_clicker_cost = 1000000
        self.auto_clicker_rate = 10  # Auto-clicker speed in milliseconds
        self.auto_clicker_active = False
        self.last_auto_click_time = 0

        self.buttons = {
            "click_button": pygame.Rect(250, 100, 200, 50),
            "upgrade_button": pygame.Rect(200, 160, 300, 50),
            "upgrade_button2": pygame.Rect(200, 220, 300, 50),
            "upgrade_button3": pygame.Rect(200, 280, 300, 50),
            "upgrade_button4": pygame.Rect(200, 340, 300, 50),
            "upgrade_button5": pygame.Rect(200, 400, 300, 50),
            "auto_clicker_button": pygame.Rect(200, 460, 300, 50),
            "gambling_button": pygame.Rect(200, 520, 300, 50)  # Gambling button
        }

    def draw_text(self, text, x, y, color=BLACK):
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))

    def draw_buttons(self):
        pygame.draw.rect(screen, BLUE, self.buttons["click_button"])
        pygame.draw.rect(screen, BLUE, self.buttons["upgrade_button"])
        pygame.draw.rect(screen, BLUE, self.buttons["upgrade_button2"])
        pygame.draw.rect(screen, BLUE, self.buttons["upgrade_button3"])
        pygame.draw.rect(screen, BLUE, self.buttons["upgrade_button4"])
        pygame.draw.rect(screen, BLUE, self.buttons["upgrade_button5"])
        pygame.draw.rect(screen, BLUE, self.buttons["auto_clicker_button"])
        pygame.draw.rect(screen, BLUE, self.buttons["gambling_button"])

        self.draw_text("Click Me!", 250, 115, WHITE)
        self.draw_text(f"Upgrade (Cost: {self.cost_per_upgrade})", 220, 175, WHITE)
        self.draw_text(f"Upgrade (Cost: {self.cost_per_upgrade2})", 220, 235, WHITE)
        self.draw_text(f"Upgrade (Cost: {self.cost_per_upgrade3})", 220, 295, WHITE)
        self.draw_text(f"Upgrade (Cost: {self.cost_per_upgrade4})", 220, 355, WHITE)
        self.draw_text(f"Upgrade (Cost: {self.cost_per_upgrade5})", 220, 415, WHITE)
        self.draw_text(f"      Auto-Grind (Cost: {self.auto_clicker_cost})", 150, 475, WHITE)
        self.draw_text("                         Gamble all!", 100, 535, WHITE)

    def increase_score(self):
        self.score += self.score_per_click

    def buy_upgrade(self):
        if self.score >= self.cost_per_upgrade:
            self.score -= self.cost_per_upgrade
            self.cost_per_upgrade *= 2
            self.score_per_click += 1

    def buy_upgrade2(self):
        if self.score >= self.cost_per_upgrade2:
            self.score -= self.cost_per_upgrade2
            self.cost_per_upgrade2 *= 2
            self.score_per_click += 25

    def buy_upgrade3(self):
        if self.score >= self.cost_per_upgrade3:
            self.score -= self.cost_per_upgrade3
            self.cost_per_upgrade3 *= 2
            self.score_per_click += 150

    def buy_upgrade4(self):
        if self.score >= self.cost_per_upgrade4:
            self.score -= self.cost_per_upgrade4
            self.cost_per_upgrade4 *= 2
            self.score_per_click += 500

    def buy_upgrade5(self):
        if self.score >= self.cost_per_upgrade5:
            self.score -= self.cost_per_upgrade5
            self.cost_per_upgrade5 *= 2
            self.score_per_click += 2000

    def activate_auto_clicker(self):
        if self.score >= self.auto_clicker_cost and not self.auto_clicker_active:
            self.score -= self.auto_clicker_cost
            self.auto_clicker_active = True
            self.last_auto_click_time = pygame.time.get_ticks()

    def start_auto_clicker(self):
        if self.auto_clicker_active and pygame.time.get_ticks() - self.last_auto_click_time >= self.auto_clicker_rate:
            self.increase_score()
            self.last_auto_click_time = pygame.time.get_ticks()

    def draw_score(self):
        self.draw_text(f"Score: {self.score}", 250, 40, WHITE)

    def gamble(self):
        if self.score > 0:  # Player should have some score to gamble
            gamble_result = random.random()  # Generates a float between 0.0 and 1.0
            if gamble_result <= 0.30:  # 30% chance
                self.score *= 2  # Double the total score
            else:  # 70% chance
                self.score = 0  # Lose everything

# Initialize game
game = ClickerGame()

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Handle button clicks
            if game.buttons["click_button"].collidepoint(mouse_x, mouse_y):
                game.increase_score()
            elif game.buttons["upgrade_button"].collidepoint(mouse_x, mouse_y):
                game.buy_upgrade()
            elif game.buttons["upgrade_button2"].collidepoint(mouse_x, mouse_y):
                game.buy_upgrade2()
            elif game.buttons["upgrade_button3"].collidepoint(mouse_x, mouse_y):
                game.buy_upgrade3()
            elif game.buttons["upgrade_button4"].collidepoint(mouse_x, mouse_y):
                game.buy_upgrade4()
            elif game.buttons["upgrade_button5"].collidepoint(mouse_x, mouse_y):
                game.buy_upgrade5()
            elif game.buttons["auto_clicker_button"].collidepoint(mouse_x, mouse_y):
                game.activate_auto_clicker()
            elif game.buttons["gambling_button"].collidepoint(mouse_x, mouse_y):
                game.gamble()

    # Handle auto-clicker
    game.start_auto_clicker()

    # Draw everything
    game.draw_score()
    game.draw_buttons()

    # Update display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)

# Quit pygame
pygame.quit()
