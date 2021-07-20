import pygame
import math
from pygame.math import Vector2


class swarmMember(pygame.sprite.Sprite):
    def __init__(self, position, sprite, velocity, alive, color, battery, damage, distance,
                 sightRange, seesTarget, attacking, team):
        super(swarmMember, self).__init__()
        self.velocity = velocity
        self.sprite = sprite
        self.baseSprite = sprite
        self.team = team
        self.attacking = attacking
        self.seesTarget = seesTarget
        self.sightRange = sightRange
        self.distance = distance
        self.damage = damage
        self.battery = battery
        self.color = color
        self.alive = alive
        self.posCord = position
        self.position = Vector2(position)
        self.radius = 64
        self.turnRate = 0.001
        self.angle = math.degrees(
            math.atan(self.velocity[0] / self.velocity[1]) if self.velocity[0] != 0 and self.velocity[1] != 0 else 0)

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        self.sprite = pygame.transform.rotate(self.baseSprite, self.angle)
        surface.blit(self.sprite, blit_position)

    def move(self):
        self.position = self.position + self.velocity
        self.posCord = self.position

    def computePos(self, visData):

        for datum in visData:
            self.angle = math.degrees(math.atan(self.velocity[0] / self.velocity[1]) if self.velocity[0] != 0 and self.velocity[1] != 0 else 0)
            datumAngle = math.degrees(math.atan(datum[1][0] / datum[1][1]) if datum[1][0] != 0 and datum[1][1] != 0 else 0)
            angleDiff= self.angle-datumAngle
            diagDist = math.sqrt(
                (math.pow(datum[0][0] - datum[0][1], 2)) + (math.pow(self.posCord[0] - self.posCord[1], 2)))
            velocityDiffX = datum[1][0] - self.velocity[0]
            velocityDiffY = datum[1][1] - self.velocity[1]
            # print(velocityDiffX)
            # print(velocityDiffY)
            # print(self.angle)

            if datum[0] != self.position and not diagDist > self.sightRange:
                if angleDiff != 0:
                    print("adjusting...")
                    if velocityDiffX > 0:
                         self.velocity[0] -= self.turnRate
                    elif velocityDiffX < 0:
                         self.velocity[0] += self.turnRate

                    if velocityDiffY > 0:
                        self.velocity[1] -= self.turnRate
                    elif velocityDiffY < 0:
                        self.velocity[1] += self.turnRate
                else:
                    print("angle match")

