import pygame
from player import Player
from pygame.locals import *
from constants import *
from asteroidfield import AsteroidField
from asteroid import Asteroid
def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    dt=0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers=(updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable,drawable)
    player=Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    field=AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((1,1,1))
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision_check(asteroid) == True :
                print("Game over!")
                return
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt=(clock.tick(60))/1000
if __name__ == "__main__":
    main()