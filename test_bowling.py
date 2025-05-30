"""
Unit tests for the Bowling Game

This module contains basic unit tests for the BowlingGame class.
The test suite verifies core game logic, score calculation, and input validation.

Classes:
    TestBowlingGame: Unit tests for BowlingGame.
"""

import unittest
from bowling_game import BowlingGame


class TestBowlingGame(unittest.TestCase):
    """Unit test suite for the BowlingGame class."""

    def setUp(self):
        """Set up a new game before each test."""
        self.game = BowlingGame()

    def roll_many(self, n, pins):
        """
        Helper to roll the same number of pins multiple times.
        
        Args:
            n (int): Number of rolls.
            pins (int): Pins knocked down in each roll.
        """
        for _ in range(n):
            self.game.roll(pins)

    def roll_sequence(self, pins_list):
        """
        Roll a sequence of pin values.

        Args:
            pins_list (list[int]): A list of pin values to roll.
        """
        for pins in pins_list:
            self.game.roll(pins)

    def test_gutter_game(self):
        """
        Test a game where no pins are knocked down.

        Expected Score:
            0
        """
        self.roll_many(20, 0)
        self.assertEqual(0, self.game.score())

    def test_all_ones(self):
        """
        Test a game where one pin is knocked down on each roll.
        
        Expected Score:
            300
        """
        self.roll_many(20, 1)
        # Expected score: 20 (1 pin × 20 rolls)
        self.assertEqual(20, self.game.score())

    def test_perfect_game(self):
        """Test a perfect game (12 strikes)"""
        self.roll_many(12, 10)
        self.assertEqual(300, self.game.score())

    def test_10th_frame_strike(self):
        """
        Test strike in the 10th frame with 2 bonus strikes
        
        Rolls:
            18 gutter balls + 10 (strike) + 10 + 10

        Expected Score:
            30
        """
        self.roll_many(18, 0) # 9 frames of gutter balls
        self.game.roll(10) # 10th frame strike
        self.game.roll(10) # bonus 1
        self.game.roll(10) # bonus 2
        self.assertEqual(30, self.game.score())

    def test_mixed_game(self):
        """
        Test a realistic mixed game.

        Rolls:
            [10, 7, 3, 9, 0, 10, 0, 8, 8, 2, 0, 6, 10, 10, 10, 8, 1]

        Expected Score:
            167
        """
        self.roll_sequence([10, 7, 3, 9, 0, 10, 0, 8, 8, 2, 0, 6, 10, 10, 10, 8, 1])
        self.assertEqual(167, self.game.score())

    def test_invalid_negative(self):
        """
        Test if rolling a negative number raises an error.
        
        Raises:
            ValueError
        """
        with self.assertRaises(ValueError):
            self.game.roll(-1)

    def test_invalid_positive(self):
        """
        Test if rolling a number higher than 10 raises an error.
        
        Raises:
            ValueError
        """
        with self.assertRaises(ValueError):
            self.game.roll(11)

if __name__ == "__main__":
    unittest.main()