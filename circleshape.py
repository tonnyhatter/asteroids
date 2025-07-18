import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # Always use type(self) to get the containers at class level
        containers = getattr(type(self), "containers", None)
        if containers:
            super().__init__(*containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        
    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision_check(self, other):
        # Check for collision with another CircleShape
        return self.position.distance_to(other.position) < (self.radius + other.radius)