import pygame
import time

snake_speed = 15
X, Y = 720, 480

# define colour
BLACK, WHITE, RED, GREEN = (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0)

pygame.init()
pygame.display.set_caption('Snake Mines')
game_window = pygame.display.set_mode((X, Y))
fps = pygame.time.Clock()

# basic setting of snake
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# mine
mines = {(200, 200), (300, 300), (400, 400), (500, 200), (100,0)}
mines_hit = set()

direction = 'RIGHT'
movement = {'UP': (0, -10), 'DOWN': (0, 10), 'LEFT': (-10, 0), 'RIGHT': (10, 0)}
score = 0

def show_score():
    font = pygame.font.SysFont('times new roman', 20)
    score_surface = font.render(f'Score: {score}', True, WHITE)
    game_window.blit(score_surface, (10, 10))

def game_over():
    game_window.fill(BLACK)
    for mine in mines:
        pygame.draw.rect(game_window, RED, pygame.Rect(*mine, 10, 10))

    font = pygame.font.SysFont('times new roman', 50)
    text = font.render(f'Your Score: {score}', True, RED)
    game_window.blit(text, text.get_rect(center=(X // 2, Y // 4)))

    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    dx, dy = movement[direction]
    snake_position[0] += dx
    snake_position[1] += dy

    
    snake_body.insert(0, list(snake_position))
    snake_body.pop()

    game_window.fill(BLACK)
    
    pygame.draw.line(game_window, GREEN, (360, 0), (360, 480), 2)  # X=0
    pygame.draw.line(game_window, GREEN, (0, 240), (720, 240), 2)  # Y=0

    for pos in snake_body:
        pygame.draw.rect(game_window, GREEN, pygame.Rect(*pos, 10, 10))

    pos_tuple = tuple(snake_position)
    if pos_tuple in mines and pos_tuple not in mines_hit:
        score += 10
        mines_hit.add(pos_tuple)

    #collusion
    if (snake_position[0] not in range(0, X) or 
        snake_position[1] not in range(0, Y) ):
        game_over()

    show_score()
    pygame.display.update()
    fps.tick(snake_speed)
