# 1. Import the Pygame module.
import pygame
import math

# 2. Initialize the project.
# This, essentially, “turns on” the different features of Pygame like sound, the keyboard, the mouse, etc.
pygame.init()
# 3. Create a window. This window will be 400 pixels wide by 400 pixels tall.
# There needs to be two sets of parentheses when creating the window.
window = pygame.display.set_mode((400, 400))
# 4. Create a caption for the window
pygame.display.set_caption("Inheritance Animation")
clock = pygame.time.Clock()


class Hexagon:
    def __init__(self, center, radius, window):
        self.center = center
        self.radius = radius
        self.window = window
        self.points = 6
        self.angle = math.radians(360 / self.points)
        self.color = (179, 55, 113)
        self.stroke_weight = 3

    def calculate_vertices(self):
        vertices = []

        for i in range(self.points + 1):
            x = math.cos(i * self.angle) * self.radius + self.center[0]
            y = math.sin(i * self.angle) * self.radius + self.center[1]
            vertices.append((x, y))
        return vertices

    def draw(self):
        pygame.draw.polygon(self.window, self.color, self.calculate_vertices())


if __name__ == '__main__':
    run = True
    hexagon = Hexagon((200, 200), 125, window)
    while run:
        pygame.time.delay(100)
        window.fill((12, 24, 186))  # change the color of the window
        hexagon.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()  # update the window with any changes
        clock.tick(30)
    pygame.quit()
