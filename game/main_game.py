import pygame
from game.snake import Snake
from game.food import Food

class SnakeGame:
    def __init__(self):
        pygame.init()

        self.width = 600
        self.height = 600
        self.block = 20

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Hand Controlled Snake")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)

        self.snake = Snake(self.width, self.height, self.block)
        self.food = Food(self.width, self.height, self.block)

        self.score = 0

        self.last_move_time = pygame.time.get_ticks()
        self.move_delay = 180

    def update_direction(self, hand_direction):
        if hand_direction:
            self.snake.change_direction(hand_direction)

    def run_step(self):
        now = pygame.time.get_ticks()

        if now - self.last_move_time >= self.move_delay:
            self.snake.move()

            if self.snake.eat(self.food):
                self.food.spawn()
                self.score += 1

            self.last_move_time = now

        self.win.fill((0, 0, 0))
        self.food.draw(self.win)
        self.snake.draw(self.win)
        self.draw_score()
        pygame.display.update()

        self.clock.tick(60)
        return True  # NEVER STOPS

    def draw_score(self):
        text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.win.blit(text, (10, 10))
