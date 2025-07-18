import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (200, 200, 200), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            rotation = random.uniform(20, 50)
            new_velocity1 = self.velocity.rotate(rotation)
            new_velocity2 = self.velocity.rotate(-rotation)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_1.velocity = new_velocity1 *1.2
            new_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_2.velocity = new_velocity2 * 1.2
            