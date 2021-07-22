import pygame
import math
from pygame.math import Vector2


def diagLength(x, y):
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))


def pointDist(x1, y1, x2, y2):
    return math.sqrt(
        (math.pow(x1 - y1, 2)) + (math.pow(x2 - y2, 2)))


def tanAngle(x, y):
    if x != 0 and y != 0:
        return math.degrees(
            math.atan(x / y))
    else:
        return 0


def vectorComponents(magnitude, angle):
    radAngle = math.radians(angle)
    return [math.sin(radAngle) * magnitude, math.cos(radAngle) * magnitude]


class swarmMember(pygame.sprite.Sprite):
    def __init__(self, position, sprite, velocityMagnitude, angle, alive, color, battery, damage, distance,
                 sightRange, seesTarget, attacking, team):
        super(swarmMember, self).__init__()
        self.closestDatum = []
        self.velocityMagnitude = velocityMagnitude
        self.angle = angle
        self.velocity = vectorComponents(self.velocityMagnitude, self.angle)
        self.sprite = sprite
        self.baseSprite = pygame.transform.scale(self.sprite, (30, 12))
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
        self.turnRate = 1

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)

        self.sprite = pygame.transform.rotate(self.baseSprite, self.angle)

        surface.blit(self.sprite, blit_position)

    def move(self):
        self.position = self.position + self.velocity
        self.posCord = self.position

    def computePos(self, visData):

        # Loop to find closest UAV
        lowestIndex = 0
        lowestVal = float("inf")

        for i in range(len(visData)):
            diagDist = pointDist(visData[i][0][0], visData[i][0][1], self.posCord[0], self.posCord[1])
            if diagDist < lowestVal:
                lowestVal = diagDist
                lowestIndex = i
        datum = visData[lowestIndex]

        datumAngle = datum[2]
        angleDiff = self.angle - datumAngle
        halfwayAngle = (self.angle + datumAngle) / 2
        diagDist = pointDist(datum[0][0], datum[0][1], self.posCord[0], self.posCord[1])
        velocityDiffX = datum[1][0] - self.velocity[0]
        velocityDiffY = datum[1][1] - self.velocity[1]

        # print(velocityDiffX)
        # print(velocityDiffY)
        # print(self.angle)

        if datum[0] != self.position and not diagDist > self.sightRange:
            self.velocity = vectorComponents(self.velocityMagnitude, self.angle)
            if self.angle != halfwayAngle:
                if self.angle < halfwayAngle:
                    self.angle += self.turnRate
                elif self.angle > halfwayAngle:
                    self.angle -= self.turnRate

        #     # print("adjusting...")
        #     if velocityDiffX > 0:
        #         self.velocity[0] -= self.turnRate
        #     elif velocityDiffX < 0:
        #         self.velocity[0] += self.turnRate
        #
        #     if velocityDiffY > 0:
        #         self.velocity[1] -= self.turnRate
        #     elif velocityDiffY < 0:
        #         self.velocity[1] += self.turnRate
        # else:
        #     print("angle match")
