import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)

        asteroid_1_vel = self.velocity.rotate(random_angle)
        asteroid_2_vel = self.velocity.rotate(-random_angle)

        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid_1.velocity = asteroid_1_vel * ASTEROID_SPLIT_SPEED_INCREASE
        asteroid_2.velocity = asteroid_2_vel * ASTEROID_SPLIT_SPEED_INCREASE