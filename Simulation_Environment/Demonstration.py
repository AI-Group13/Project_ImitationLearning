from Imitation_Learn import Imitation_Learn
import numpy as np

class Demonstration(Imitation_Learn):

    def __init__(self):
        Imitation_Learn.__init__(self)

    def make_robot_follow_path(self):
        '''To make the robot follow a particular path, sort of demonstration'''
