import unittest
from unittest.mock import patch
import game  # assuming the function is in a file named game.py

class TestGame(unittest.TestCase):
    # Test if get_user_choice returns 'rock' when user inputs 'rock'
    @patch('builtins.input', return_value='rock')
    def test_get_user_choice_rock(self, input):
        self.assertEqual(game.get_user_choice(), 'rock')

    # Test if get_user_choice returns 'paper' when user inputs 'paper'
    @patch('builtins.input', return_value='paper')
    def test_get_user_choice_paper(self, input):
        self.assertEqual(game.get_user_choice(), 'paper')

    # Test if get_user_choice returns 'scissors' when user inputs 'scissors'
    @patch('builtins.input', return_value='scissors')
    def test_get_user_choice_scissors(self, input):
        self.assertEqual(game.get_user_choice(), 'scissors')

    # Test if get_user_choice raises a SystemExit when user inputs 'invalid'
    @patch('builtins.input', return_value='invalid')
    def test_get_user_choice_invalid(self, input):
        with self.assertRaises(SystemExit):
            game.get_user_choice()

    # Test all possible outcomes of determine_winner
    def test_determine_winner(self):
        self.assertEqual(game.determine_winner('rock', 'scissors'), 'user')
        self.assertEqual(game.determine_winner('rock', 'paper'), 'computer')
        self.assertEqual(game.determine_winner('rock', 'rock'), 'tie')
        self.assertEqual(game.determine_winner('paper', 'rock'), 'user')
        self.assertEqual(game.determine_winner('paper', 'scissors'), 'computer')
        self.assertEqual(game.determine_winner('paper', 'paper'), 'tie')
        self.assertEqual(game.determine_winner('scissors', 'paper'), 'user')
        self.assertEqual(game.determine_winner('scissors', 'rock'), 'computer')
        self.assertEqual(game.determine_winner('scissors', 'scissors'), 'tie')

if __name__ == '__main__':
    unittest.main()