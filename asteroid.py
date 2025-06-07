import pygame
from circleshape import CircleShape
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen, "grey", self.position ,PLAYER_RADIUS,2)
    
    def update(self,dt):
        self.position+=self.velocity*dt
        
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            angle_of_split=random.uniform(20,50)
            split_vector1=self.velocity.rotate(angle_of_split)
            split_vector2=self.velocity.rotate(-angle_of_split)
            new_radius=self.radius - ASTEROID_MIN_RADIUS
            asteroid1=Asteroid(self.position.x,self.position.y,new_radius)
            asteroid2=Asteroid(self.position.x,self.position.y,new_radius)
            asteroid1.velocity=split_vector1
            asteroid2.velocity=split_vector2
            self.kill()

