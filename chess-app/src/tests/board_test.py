import unittest
from board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board([["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                            ["", "", "", "", "", "", "", ""],
                            ["", "", "", "", "", "", "", ""],
                            ["", "", "", "", "", "", "", ""],
                            ["", "", "", "", "", "", "", ""],
                            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
                            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]])
    def test_move(self):
        pass
