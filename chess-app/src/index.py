import pygame
from game_loop import GameLoop
from event_queue import EventQueue
from renderer import Renderer
from clock import Clock
from board import Board

inital_board_state = [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                      ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                      ["", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", ""],
                      ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
                      ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
                      ]


def main():

    display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    pygame.display.set_caption("Chess")
    pygame.font.init()

    clock = Clock()
    event_queue = EventQueue()
    board = Board(inital_board_state)
    renderer = Renderer(display, board)
    game_loop = GameLoop(renderer, event_queue, clock)


    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
