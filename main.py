import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from bullet import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for object in updatable:
            object.update(dt)
        
        for object in asteroids:
            hit = object.collision(player)
            if hit == True:
                print("Game Over!")
                return
        
        for asteroid in asteroids:
            for shot in shots:
                hit = asteroid.collision(shot)
                if hit == True:
                    asteroid.split()
                    shot.kill()
                    hit = False
                else:
                    hit = False
    
        screen.fill((0, 0, 0))

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()