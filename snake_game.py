import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = 600
GRID_SIZE = 20
GRID_COUNT = WINDOW_SIZE // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (240, 220, 180)  # A warm beige color

# Initialize screen
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Snake Game')

class Snake:
    def __init__(self):
        self.body = [(GRID_COUNT // 2, GRID_COUNT // 2)]
        self.direction = [1, 0]  # Start moving right
        self.grow = False

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
            
        self.body.insert(0, new_head)

    def check_collision(self):
        head = self.body[0]
        # Check wall collision
        if (head[0] < 0 or head[0] >= GRID_COUNT or 
            head[1] < 0 or head[1] >= GRID_COUNT):
            return True
        
        # Check self collision
        if head in self.body[1:]:
            return True
        
        return False

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = self.spawn_food()
        self.score = 0
        self.clock = pygame.time.Clock()
        self.speed = 10  # Initial speed

    def spawn_food(self):
        while True:
            food = (random.randint(0, GRID_COUNT-1), random.randint(0, GRID_COUNT-1))
            if food not in self.snake.body:
                return food

    def update(self):
        self.snake.move()
        
        # Check food collision
        if self.snake.body[0] == self.food:
            self.snake.grow = True
            self.food = self.spawn_food()
            self.score += 1
            self.speed += 1  # Increase speed as score increases

        # Check game over
        if self.snake.check_collision():
            return False
            
        return True

    def draw_background(self):
        screen.fill(BACKGROUND_COLOR)
        for i in range(GRID_COUNT):
            pygame.draw.line(screen, (200, 200, 200), (i * GRID_SIZE, 0), (i * GRID_SIZE, WINDOW_SIZE))
            pygame.draw.line(screen, (200, 200, 200), (0, i * GRID_SIZE), (WINDOW_SIZE, i * GRID_SIZE))

    def get_food_color(self):
        score = self.score
        if score < 10:
            return (255, 0, 0)  # Red
        elif score < 20:
            return (255, 165, 0)  # Orange
        elif score < 30:
            return (255, 255, 0)  # Yellow
        else:
            return (0, 128, 0)  # Green

    def draw(self):
        self.draw_background()
        
        # Draw snake
        for segment in self.snake.body:
            pygame.draw.rect(screen, GREEN, 
                           (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, 
                            GRID_SIZE - 2, GRID_SIZE - 2))
        
        # Draw food
        pygame.draw.rect(screen, self.get_food_color(),
                        (self.food[0] * GRID_SIZE, self.food[1] * GRID_SIZE,
                         GRID_SIZE - 2, GRID_SIZE - 2))
        
        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {self.score}', True, WHITE)
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.direction != [0, 1]:
                        self.snake.direction = [0, -1]
                    elif event.key == pygame.K_DOWN and self.snake.direction != [0, -1]:
                        self.snake.direction = [0, 1]
                    elif event.key == pygame.K_LEFT and self.snake.direction != [1, 0]:
                        self.snake.direction = [-1, 0]
                    elif event.key == pygame.K_RIGHT and self.snake.direction != [-1, 0]:
                        self.snake.direction = [1, 0]

            if not self.update():
                running = False
                
            self.draw()
            self.clock.tick(self.speed)  # Control game speed

        # Game Over screen
        font = pygame.font.Font(None, 74)
        text = font.render('Game Over!', True, WHITE)
        text_rect = text.get_rect(center=(WINDOW_SIZE/2, WINDOW_SIZE/2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()