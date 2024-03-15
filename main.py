import pygame
import gui
import game_of_life

def main():
    #initialize objects: game of life, pygame, display
    g = game_of_life.grid(40)
    g.populate_random()
    pygame.init()
    display = gui.gui(800, 40) #length of screen=800, squares=40
    clock = pygame.time.Clock()

    pygame.time.delay(3000)

    #main game loop
    count = 0
    while True:
        if count > 100: #exit condition 1
            print('100 iterations elapsed.')
            break
        elif sum(pygame.key.get_pressed()) != 0: #exit condition 2
            print('exit key pressed.')
            break
        clock.tick(1)

        display.draw_blank()
        display.draw(g.grid)

        pygame.display.update()
        pygame.event.pump()
        g.step()
        print(f'iter {count}: {clock.get_time()} ms')
        count += 1
    pygame.quit()

if __name__ == '__main__':
    main()