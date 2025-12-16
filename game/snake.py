import pygame

class Snake:
    def __init__(self, width, height, block):
        self.width = width
        self.height = height
        self.block = block

        self.x = width // 2
        self.y = height // 2

        self.direction = "RIGHT"
        self.body = [(self.x, self.y)]
        self.grow = False

    def change_direction(self, new_dir):
        # Prevent direct reversal (this rule STAYS)
        opposite = {
            "UP": "DOWN",
            "DOWN": "UP",
            "LEFT": "RIGHT",
            "RIGHT": "LEFT"
        }

        if new_dir and new_dir != opposite[self.direction]:
            self.direction = new_dir

    def move(self):
        if self.direction == "UP":
            self.y -= self.block
        elif self.direction == "DOWN":
            self.y += self.block
        elif self.direction == "LEFT":
            self.x -= self.block
        elif self.direction == "RIGHT":
            self.x += self.block

        # ---- WRAP AROUND ----
        if self.x < 0:
            self.x = self.width - self.block
        elif self.x >= self.width:
            self.x = 0

        if self.y < 0:
            self.y = self.height - self.block
        elif self.y >= self.height:
            self.y = 0

        head = (self.x, self.y)

        # ---- NO GAME OVER ON SELF COLLISION ----
        self.body.insert(0, head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

        return True  # ALWAYS ALIVE

    def eat(self, food):
        if self.x == food.x and self.y == food.y:
            self.grow = True
            return True
        return False

    def draw(self, win):
        for segment in self.body:
            pygame.draw.rect(
                win,
                (0, 255, 0),
                (segment[0], segment[1], self.block, self.block)
            )


# hello test trial

