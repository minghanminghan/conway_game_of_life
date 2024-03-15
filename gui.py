import pygame
import random

class gui:
    def __init__(self, screen_size:int=800, grid_size:int=40):
        self.screen_size = 800
        self.number_grids = 40
        self.grid_size = self.screen_size // self.number_grids #dimensions of each grid square

        self.screen = pygame.display.set_mode((screen_size, screen_size))
        
        self.draw_blank()

    def draw_blank(self) -> None:
        #draw 20x20 grid
        self.screen.fill((0,0,0)) #black
        for i in range(0, self.screen_size, self.grid_size):
            pygame.draw.line(self.screen, (200, 200, 200), (0, i), (self.screen_size, i))
            pygame.draw.line(self.screen, (200, 200, 200), (i, 0), (i, self.screen_size))
        pygame.display.update()

    #draw function: gets a list of bools and displays it
    def draw(self, indexes:list[bool]) -> None:
        self.draw_blank()
        for y in range(self.number_grids):
            for x in range(self.number_grids):
                #print(f'y: {y}, x: {x}, grid: {indexes[y][x]}')
                if indexes[y][x]:
                    pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x*self.grid_size, y*self.grid_size, self.grid_size, self.grid_size))

    '''
        while True:
            drawGrid()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit

            pygame.display.update()


    def drawGrid():
        blockSize = 20 #Set the size of the grid block
        for x in range(0, WINDOW_WIDTH, blockSize):
            for y in range(0, WINDOW_HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(SCREEN, WHITE, rect, 1)
    '''