import pygame

class SwarmSim:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode([2000, 1000])

    def mainLoop 

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 217, 133))


    pygame.display.flip()

pygame.quit()
