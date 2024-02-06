# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 02/07/2024
# Description: Project 5b

class Taxicab:
    def __init__(self, x, y):
        # Initialize the Taxicab with initial coordinates (x, y) and an odometer reading of 0
        self.__x_coord = x
        self.__y_coord = y
        self.__odometer = 0

    def get_x_coord(self):
        # Return the current x-coordinate of the Taxicab
        return self.__x_coord

    def get_y_coord(self):
        # Return the current y-coordinate of the Taxicab
        return self.__y_coord

    def get_odometer(self):
        # Return the current odometer reading of the Taxicab
        return self.__odometer

    def move_x(self, distance):
        # Move the Taxicab horizontally (left or right) by the given distance
        # Update the odometer reading by the absolute value of the distance
        self.__odometer += abs(distance)
        self.__x_coord += distance

    def move_y(self, distance):
        # Move the Taxicab vertically (up or down) by the given distance
        # Update the odometer reading by the absolute value of the distance
        self.__odometer += abs(distance)
        self.__y_coord += distance
