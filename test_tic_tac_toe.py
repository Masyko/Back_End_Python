import unittest
from tic_tac_toe import main, check_win, take_input, draw_board

class InputTestCase(unittest.TestCase):
    def test_take_input(self):
        game = main()
        assert a == input('ron')
        assert b == input('dgfhghuijlok;ojihugfdgfhgjkhljk;ljhlgk')