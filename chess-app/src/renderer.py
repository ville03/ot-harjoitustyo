import pygame
from textfield import TextField

black = (0, 0, 0)
white = (255, 255, 255)
class Renderer:
    def __init__(self, display, board):
        self._display = display
        self.board = board
        monitor = pygame.display.Info()
        self._height = monitor.current_h
        self._width = monitor.current_w

        self._square_side_length = min(self._width, self._height)//12
        self._square = (self._square_side_length, self._square_side_length)

        self._textfield = TextField((self._width+10*self._square_side_length)//2, self._height//2, 140, 32)


    def render(self):
        color = black
        backgroud=((0, 0), (self._width, self._height))
        pygame.draw.rect(self._display, (0, 100, 0), backgroud)

        piece_font = pygame.font.SysFont(
            pygame.font.get_default_font(), self._square_side_length)

        for i in range(8):
            for j in range(8):
                square_center_location_height = (
                    self._height-(8-2*i)*self._square_side_length)//2
                square_center_location_width = (
                    self._width-(8-2*j)*self._square_side_length)//2
                square_center_location = (
                    square_center_location_width, square_center_location_height)

                # draws squares for the chessboard
                if (i+j) % 2 == 0:
                    pygame.draw.rect(self._display, (200, 200, 200), rect=(
                        square_center_location, self._square))
                else:
                    pygame.draw.rect(self._display, (50, 50, 50), rect=(
                        square_center_location, self._square))

                # no piece
                if self.board.board()[i][j] == "":
                    continue
                # check piece color
                if list(self.board.board()[i][j])[0] == "w":
                    color = white
                else:
                    color = black

                # draw piece
                text_surface = piece_font.render(
                    list(self.board.board()[i][j])[1], False, color)
                piece_location = (square_center_location_width+self._square_side_length //4,
                                  square_center_location_height+self._square_side_length//4)
                self._display.blit(text_surface, piece_location)
        self._textfield.draw(self._display)
        pygame.display.update()
    def tf(self):
        return self._textfield
