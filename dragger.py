import pygame

from const import *

class Dragger:

    def __init__(self):
        self.piece = None
        self.dragging = False
        self.initial_row = 0
        self.initial_col = 0
        self.mouseX = 0
        self.mouseY = 0

    # blit methods

    def update_blit(self, surface):
        self.piece.set_texture(size=128)
        texture = self.piece.texture

        img = pygame.image.load(self.piece.texture)

        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)

        surface.blit(img, self.texture_rect)


    # other methods
    def update_mouse(self,pos):
        self.mouseX, self.mouseY = pos #(xcor,ycor)
    
    def save_initial(self, pos):
        self.initial_row = pos.row[1] // SQSIZE
        self.initial_col = pos.col[0] // SQSIZE
    
    def drag_piece(self,piece):
        self.piece = piece
        self.dragging = True
    
    def ungrag_piece(self):
        self.piece = None
        self.dragging = False