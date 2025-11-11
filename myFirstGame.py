import pygame
import random
pygame.init()

CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
WIDTH = GRID_WIDTH * CELL_SIZE
HEIGHT = GRID_HEIGHT * CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
color = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)
score = 0
clock = pygame.time.Clock()
pygame.display.set_caption("Snake")

snake = [(2,0), (1,0), (0,0)]
direction = (1, 0)

food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, 
        (segment[0] * CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
def draw_food():
    pygame.draw.rect(screen, RED, (food[0]*CELL_SIZE, food[1]*CELL_SIZE, CELL_SIZE,
    CELL_SIZE))

font = pygame.font.SysFont("arial", 24)
def show_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

running = True 
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction!=(0,-1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction !=(1,0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction!=(-1,0):
                direction = (1, 0)
    draw_snake()
    draw_food()
    show_score()
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head) # Προσθήκη της νέας κεφαλής
    snake.pop() # αφαίρεση ουράς
    
    if new_head == food:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        snake.insert(0, new_head)
        score += 1
    
    # Έλεγχος σύγκρουσης με τοίχο ή σώμα
    if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
    new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
        running = False
        break
    pygame.display.update()
    clock.tick(5)
pygame.quit()
