import unittest
import tic_tac_toe

class InputTestCase(unittest.TestCase):
    def test_win_x(self):
        board = [1, 2, 3, 'X', 'X', 'X', 'O', 'O', 9]
        self.assertEqual(tic_tac_toe.check_win(board), 'X')

    def test_win_o(self):
        board = ['X', 'X', 'O', 'X', 'X', 'O', 7, 8, 'O']
        self.assertEqual(tic_tac_toe.check_win(board), 'O')
