import pygame

from const import *
from board import Board
from dragger import Dragger

class Game:
    
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger() 
   
        #blit methods
        #temabasico

    def show_bg(self,surface):
        for row in range (ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234,235,200) # verde claro
                else:
                    color = (119,154,88) # verde escuro
                rect =(col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface,color,rect)

    def show_pieces(self,surface):
        for row in range(ROWS):
            for col in range(COLS):
                #piece?
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    img = pygame.image.load(piece.texture) #importando a imagem com o pygame

                    img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2 #centralizando a imagem
                    piece.texture_rect = img.get_rect(center=img_center) #centralizando a imagem
                    surface.blit(img, piece.texture_rect)
