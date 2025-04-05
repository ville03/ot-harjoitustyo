import pygame
from game_loop import GameLoop
from event_queue import EventQueue
from renderer import Renderer
from clock import Clock

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
    display.fill("green")

    pygame.display.set_caption("Chess")

    clock = Clock()
    event_queue = EventQueue()
    renderer = Renderer(display, inital_board_state)
    game_loop = GameLoop(renderer, event_queue, clock)

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
