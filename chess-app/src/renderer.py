import pygame


class Renderer:
    def __init__(self, display, board):
        self._display = display
        self._board = board

    def render(self):
        monitor = pygame.display.Info()
        height = monitor.current_h
        width = monitor.current_w

        square_side_length = min(monitor.current_w, monitor.current_h)//12
        square = (square_side_length, square_side_length)
        
        black = (0, 0, 0)
        white = (255, 255, 255)
        color = black
        
        pygame.font.init()
        piece_font = pygame.font.SysFont(pygame.font.get_default_font(), square_side_length)
        
        for i in range(8):
            for j in range(8):
                square_center_location_height = (height-(8-2*i)*square_side_length)//2
                square_center_location_width = (width-(8-2*j)*square_side_length)//2
                square_center_location = (square_center_location_width, square_center_location_height)

                #draws squares for the chessboard
                if((i+j)%2==0):
                    pygame.draw.rect(self._display, (200,200,200), rect=(square_center_location, square))
                else:
                    pygame.draw.rect(self._display, (50,50,50), rect=(square_center_location, square))
                
                #no piece
                if(self._board[i][j]==""):
                    continue
                #check piece color
                if(list(self._board[i][j])[0]=="b"):
                    color = white
                else:
                    color = black

                #draw piece
                text_surface = piece_font.render(list(self._board[i][j])[1], False, color)
                self._display.blit(text_surface, (square_center_location_width+square_side_length//4, square_center_location_height+square_side_length//4))

                    

        pygame.display.update()
        
