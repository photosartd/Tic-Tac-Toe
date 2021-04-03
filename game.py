import pygame
GRAY = (100,)*3
RED = CROSS = (255,0,0)
class Board:
    def __init__(self, w, h, W, H, left, top, size):
        self.w, self.h = w,h #size of the map
        self.W, self.H = W,H #size of the win
        self.board = [[0] * w for _ in range(h)]
        self.l = left #left point of the map
        self.t = top #top point of the map
        self.size = size #cell size of the map
        self.move = 1 #move order

    def render(self, sc):
        def draw_circle(self, x, y):
            '''draw circle inside the cell with coordinates x, y'''
            x = self.l + (x + .5) * self.size
            y = self.t + (y + .5) * self.size
            pygame.draw.circle(sc, GRAY, (x,y), (self.size - 3)//2, 3)
        def draw_cross(self, x, y):
            '''draw cross inside the cell with coordinates x, y'''
            x = self.l + x*self.size + 3
            y = self.t + y*self.size + 3
            pygame.draw.line(sc, CROSS, (x,y), (x + self.size - 3, y + self.size - 3), 3)
            pygame.draw.line(sc, CROSS, (x + self.size - 3,y), (x, y + self.size - 3), 3)
        
        for y in range(1, self.h + 1):
            pygame.draw.line(sc, GRAY,
            (self.l,self.t + y*self.size), (self.l + self.size*self.w, self.t + y*self.size), 3)
        for x in range(1, self.w + 1):
            pygame.draw.line(sc, GRAY,
            (self.l + x*self.size,self.t), (self.l + x*self.size, self.t + self.h*self.size), 3)
        for y in range(self.h):
            for x in range(self.w):
                if self.board[y][x] == 1:
                    draw_cross(self, x, y)
                elif self.board[y][x] == -1:
                    draw_circle(self, x, y)

    def get_cells_coords(self, mouse_pos):
        '''get cells coords (x,y) of the cell on the map'''
        x = (mouse_pos[0] - self.l)//self.size
        y = (mouse_pos[1] - self.t)//self.size
        if 0 <= x <= self.w and 0 <= y <= self.h:
            return x, y
        else:
            None

    def click(self, mouse_pos):
        cell_coords = self.get_cells_coords(mouse_pos)
        if not self.board[cell_coords[1]][cell_coords[0]]:
            self.board[cell_coords[1]][cell_coords[0]] = self.move
            self.move = - self.move

    def check_end(self, screen):
        '''rendering winning'''
        def is_end():
            '''checking whether end or not
            return (num_1, num_2) where num_1 - kind of winning:
            num_1 == 1 & num_2 == i -> ith column
            num_1 == 2 & num_2 == i -> ith line
            num_1 == 3 -> diagonals (num_2 == 1 -> main | num_2 == 2 -> secondary)
            if there is no winning returns None'''
            check_i_line = lambda x, i: True if x[i][0] == x[i][1] == x[i][2] != 0 else False
            check_i_col = lambda x, i: True if x[0][i] == x[1][i] == x[2][i] != 0 else False
            check_main_diag = lambda x: True if x[0][0] == x[1][1] == x[2][2] != 0 else False
            check_secondary_diag = lambda x: True if x[0][2] == x[1][1] == x[2][0] != 0 else False

            for i in range(3):
                if check_i_col(self.board, i):
                    return 1, i
                if check_i_line(self.board, i):
                    return 2, i

            if check_main_diag(self.board):
                return 3, 1
            if check_secondary_diag(self.board):
                return 3, 2
            return None
        
        is_end = is_end()
        shift = self.W//10
        if is_end is not None:
            if is_end[0] == 1:
                x0, y0 = self.l + (is_end[1] + .5) * self.size, self.t + shift
                x1, y1 = self.l + (is_end[1] + .5) * self.size, self.t + self.size * self.h - shift
            elif is_end[0] == 2:
                x0, y0 = self.l + shift, self.t + (is_end[1] + .5) * self.size
                x1, y1 = self.l + self.w * self.size - shift, self.t + (is_end[1] + .5) * self.size
            elif is_end[0] == 3:
                if is_end[1] == 1:
                    x0, y0 = self.l + shift, self.t + shift
                    x1, y1 = self.l + self.w*self.size - shift, self.t + self.h * self.size - shift
                else:
                    x0,y0 = self.l + self.w*self.size - shift, self.t + shift
                    x1,y1 = self.l + shift, self.t + self.h*self.size - shift
            pygame.draw.line(screen, RED, (x0,y0), (x1,y1), 10)
            pygame.display.update()
            pygame.time.delay(1000)
            return True
        else:
            return False