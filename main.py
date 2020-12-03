

import pygame
from checkers.constants import WIDTH, HEIGHT

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
from checkers.board import Board


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        board = Board()
        
        for event in pygame.event.get():
            """checks if any events happened"""
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                """if we press any mouse button"""
                pass

        board.draw_squares(WIN)
        pygame.display.update()

    pygame.quit()
            
main()