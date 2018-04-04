from VrepHelper import VrepHelper
import math
import numpy as np
import vrep

class Imitation_Learn(VrepHelper):

    def __init__(self):

        '''Inheriting the V-REP helper functions' class while keeping the two discrete'''

        VrepHelper.__init__(self)
        self.recorder = None
        self.noiseInducer = None

    def deg2rad(self, ang_deg):
        '''Degree to radians conversion'''
        return ang_deg * (math.pi) / 180

    def rad2deg(self, ang_rad):
        '''Radians to degree conversion'''
        return ang_rad * 180 /math.pi

    def cart_dist(self, p1, p2):
        '''Cartesian Distance Calculater'''
        summ = 0
        for a, b in zip(p1, p2):
            summ += (a - b) ** 2
        return np.sqrt(summ)

    def log_data(self, data_list, filename):
        '''Given the 1D list(list of data points) and the filename, this writes the content to a csv file'''
        import csv
        try:
            with open(filename, 'wb') as datafile:                              # 'original_data.csv'
                self.recorder = csv.writer(datafile, quoting=csv.QUOTE_ALL)
                self.recorder.writerow(data_list)
            return 0
        except:
            print("Data logging failed")
            return 1

    def record_demo(self, file):
        '''Given the file name where the data is to be stored while logging, it reads the joint angles and writes them into it for each time step'''
        for ii, joint_handle in enumerate(self.joint_handles):
            _, self.q[ii] = vrep.simxGetJointPosition(self.clientID, joint_handle, self.block_mode)
            if _ != 0: raise Exception("Joint Data Logging failed")

        status = self.log_data(self.q, file)

        if status==0:
            return 0
        else:
            return 1

    def induce_random_noise(self, filenn, err_percent):
        '''Induce random noise in the data recorded from the demonstration to match real-life scenarios'''
        import csv
        import random

        try:
            with open(filenn, 'rb') as datafile:                                    # 'noisy_data.csv'

                self.noiseInducer = csv.reader(datafile)
                for row in self.noiseInducer:
                    for element in row:
                        element = int(element)*(1 + random.randrange(-err_percent, err_percent))
                    self.log_data(row, 'noisy_data.csv')

        except:
            print ("Error in inducing noise to the demonstration data")
