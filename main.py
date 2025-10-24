import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() 
    attack_shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)   
    Asteroid.containers = (asteroids, updatable, drawable) 
    AsteroidField.containers = (updatable)
    Shot.containers = (attack_shots, updatable, drawable) 

    player = Player(x = SCREEN_WIDTH / 2 , y = SCREEN_HEIGHT / 2)
    asteroidfields = AsteroidField()
    dt = 0

    # Gameloop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.is_collided(player):
                print("Game Over!")
                return 

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
