"""
Bowling Game Implementation
A module for calculating bowling game scores.
"""


class BowlingGame:
    def __init__(self):
        # Initialize a new game with 10 frames
        # Each frame has up to 2 rolls (except the 10th frame which can have 3)
        self.rolls = []
        

    def roll(self, pins: int):
        if not isinstance(pins, int) or pins < 0 or pins > 10:
            raise ValueError(f"Invalid roll value: {pins}")
        """
        Records a roll in the game.

        Args:
            pins: Number of pins knocked down in this roll
        """
        self.rolls.append(pins)
        

    def score(self):
        """Calculate the score for the current game."""
        total_score = 0
        index = 0

        for _ in range(10):
            if self._is_strike(index):
                # Strike
                total_score += 10 + self._strike_bonus(index)
                index += 1
            elif self._is_spare(index):
                # Spare
                total_score += 10 + self._spare_bonus(index)
                index += 2
            else:
                # Open frame
                total_score += self._sum_of_balls_in_frame(index)
                index += 2

        return total_score

    def _is_strike(self, index):
        """
        Check if the roll at index is a strike.

        Args:
            index: Index of the roll to check

        Returns:
            True if the roll is a strike, False otherwise
        """
        return index < len(self.rolls) and self.rolls[index] == 10

    def _is_spare(self, index):
        """
        Check if the rolls at index and index + 1 form a spare.

        Args:
            index: Index of the first roll in a frame

        Returns:
            True if the rolls form a spare, False otherwise
        """
        return index + 1 < len(self.rolls) and self.rolls[index] + self.rolls[index + 1] == 10

    def _strike_bonus(self, index):
        """
        Calculate the bonus for a strike.

        Args:
            index: Index of the strike roll

        Returns:
            The value of the next two rolls after the strike
        """
        return self.rolls[index + 1] + self.rolls[index + 2]

    def _spare_bonus(self, index):
        """
        Calculate the bonus for a spare.

        Args:
            index: Index of the first roll in a spare

        Returns:
            The value of the roll after the spare
        """
        return self.rolls[index + 2]
    
    def _sum_of_balls_in_frame(self, index):
        return self._get_roll(index) + self._get_roll(index + 1)
    
    def _get_roll(self, index):
        return self.rolls[index] if index < len(self.rolls) else 0