# Tiffany Bo
# ITP 115, Fall 2019
# Final Project

import random
from Diner import Diner



class RestaurantHelper(object):
    FILENAME = "names.txt"

    # Input: -
    # Return value: a new Diner object with a random name
    #             OR
    #             None (aka no new diner has arrived)
    @staticmethod
    def randomDinerGenerator():
        if random.randint(1, 10) % 3 == 0:
            return Diner(RestaurantHelper.generateRandName())
        else:
            return None

    @staticmethod
    def generateRandName():
        fin = open(RestaurantHelper.FILENAME, 'r')
        names = [line.strip() for line in fin]
        fin.close()
        return random.choice(names)
