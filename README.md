# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 02/07/2024
# Description: Project 5b

class Taxicab:
    """
    A class representing a Taxicab with x and y coordinates and an odometer.
    """

    def __init__(self, x, y):
        """
        Initializes a Taxicab object with the given x and y coordinates and sets the odometer to zero.

        Args:
            x (int): The initial x-coordinate.
            y (int): The initial y-coordinate.
        """
        self._x_coord = x
        self._y_coord = y
        self._odometer = 0

    def get_x_coord(self):
        """
        Get the current x-coordinate.

        Returns:
            int: The current x-coordinate.
        """
        return self._x_coord

    def get_y_coord(self):
        """
        Get the current y-coordinate.

        Returns:
            int: The current y-coordinate.
        """
        return self._y_coord

    def get_odometer(self):
        """
        Get the current odometer reading.

        Returns:
            int: The current odometer reading.
        """
        return self._odometer

    def move_x(self, distance):
        """
        Move the Taxicab horizontally by the given distance.

        Args:
            distance (int): The distance to move left (negative) or right (positive).
        """
        self._x_coord += distance
        self._odometer += abs(distance)

    def move_y(self, distance):
        """
        Move the Taxicab vertically by the given distance.

        Args:
            distance (int): The distance to move up (positive) or down (negative).
        """
        self._y_coord += distance
        self._odometer += abs(distance)
