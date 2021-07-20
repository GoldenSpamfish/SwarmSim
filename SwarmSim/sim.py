import pygame

from utils import load_sprite
from member import swarmMember


class SwarmSim:
    def __init__(self):
        self.visData = []
        self._initPygame()
        self.screen = pygame.display.set_mode((2000, 1000))
        self.swarm = []
        self.clock = pygame.time.Clock()

        for i in range(24):
            self.swarm.append(swarmMember(
                # position tuple,         sprite,         velocity vector list, alive bool, color int
                (75*(i+1), 200),      load_sprite("Seabat"),        [1, 1 + 0.01*i],           True,       0,
                # battery int,   hp,     ideal distance, sight range,    sees target bool, attacking bool, team num
                2000,           100,           100,         200,             False,            False,        0))

    def mainLoop(self):
        running = True
        while running:
            self._handleInput()
            self._processGameLogic()
            self._draw()

    def _initPygame(self):
        pygame.init()
        pygame.display.set_caption("SwarmSim")

    def _handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

    def _processGameLogic(self):
        self.visData.clear()
        for data in self.swarm:
            self.visData.append([data.posCord, data.velocity, data.color])


        for i in self.swarm:
            i.computePos(self.visData)
            i.move()

    def _draw(self):
        self.screen.fill((255, 217, 133))
        for i in self.swarm:
            i.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(60)


pygame.quit()
