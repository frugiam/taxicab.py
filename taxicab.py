# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 02/07/2024
# Description: Project 5b

class Taxicab:
    # constructor that sets the x and y coordinates and odometer to 0
    def __init__(self, x, y):
        self.__x_coord = x
        self.__y_coord = y
        self.__odometer = 0

    # get method for x coordinate
    def get_x_coord(self):
        return self.__x_coord

    # get method for y coordinate
    def get_y_coord(self):
        return self.__y_coord

    # get method for getting the odometer reading
    def get_odometer(self):
        return self.__odometer

    # method that updates the odometer reading and the current x coordinates
    def move_x(self, distance):
        if distance < 0:
            self.__odometer += (-distance)
        else:
            self.__odometer += (distance)
        self.__x_coord += distance

    # method that updates the odometer reading and the current y coordinates
    def move_y(self, distance):
        if distance < 0:
            self.__odometer += (-distance)
        else:
            self.__odometer += (distance)
        self.__y_coord += distance