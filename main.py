import pygame
from game import Board

BLACK = (0,) * 3
GRAY = (100,) * 3
WHITE = (255,) * 3
RED = (255,0,0)
YELLOW = (255,255,0)
LIGHTGREEN = (0,200,200)

CROSS = '#046582'
CIRCLE = '#e4bad4'

pygame.init()

#win - Surface
size = W,H = 600, 600
win = pygame.display.set_mode(size)
background_color = (255,255,255)
board = Board(3,3,W,H,0,0,200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.click(event.pos)

    win.fill(WHITE)
    board.render(win)
    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.QUIT]:
        pygame.quit()
        exit()
    if board.check_end(win):
        pygame.quit()
        exit()