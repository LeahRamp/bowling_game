"""
Bowling Game Implementation
A module for calculating bowling game scores.
"""


class BowlingGame:
    """A class representing a ten-pin bowling game and scoring logic"""
    def __init__(self):
        """
        Initialize a new bowling game instance

        The game starts with an empty list if rolls. a complete game will include 
        10 frames, with each frame allowing up to 2 rolls, except in the 10th frame 
        which can allow for up to 3 rolls if there is a strike or spare.
        """
        self.rolls = []
        

    def roll(self, pins: int):
        """
        Record a roll in the game.

        Args:
            pins (int): Number of pint knocked down in this roll. must be between 0 and 10 pins.

        Raises: 
            ValueError: If the number of pins is not an integer or within the range of 0 - 10.
        """
        if not isinstance(pins, int) or pins < 0 or pins > 10:
            raise ValueError(f"Invalid roll value: {pins}")
        self.rolls.append(pins)
        

    def score(self):
        """
        Calculate the score for the current game.
        
        Returns:
            int: The final score of the game based on current rolls.
        """
        total_score = 0
        index = 0

        for _ in range(10): # Each bowling game has 10 frames
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
        """
        Sum of the number of pins knocked down in a frame.

        Args:
            Index: Index of the first roll of the frame.

        Returns:
            The sum of 2 rolls on the frame.
        """
        return self._get_roll(index) + self._get_roll(index + 1)
    
    def _get_roll(self, index):
        """
        Safely get the number of pins knocked down in a roll.

        Args:
            Index: The roll index

        Returns:
            The number of pins knocked down in the roll, or 0 if the index is out of bounds.
        """
        return self.rolls[index] if index < len(self.rolls) else 0