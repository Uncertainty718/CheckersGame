

import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
from checkers.board import Board

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            """checks if any events happened"""
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                """if we press any mouse button"""
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                

        game.update()

    
    pygame.quit()


main()