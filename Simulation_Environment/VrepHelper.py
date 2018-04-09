import vrep
import numpy as np
import os
import time
import subprocess
import sys
import math

class VrepHelper():

   def __init__(self):

       self.simTime = 1
       self.modelPath = os.getcwd() + "/models/KUKA YouBot.ttm"
       self.scenePath = os.getcwd() + "/scenes/emptyScene.ttt"
       self.vrepPath = '/home/onkar-trivedi/V-REP/V-REP_PRO_EDU_V3_5_0_Linux/vrep.sh'
       self.clientID = 0
       self.block_mode = vrep.simx_opmode_blocking
       self.joint_handles = []
       self.start_process = 0
       self.q = None
       self.dq = None
       self.pos = None

   def start_vrep(self, waitTime):

        self.start_process = subprocess.Popen([self.vrepPath])
        time.sleep(waitTime)

   def initialize_env(self):

        # close any open connections
        vrep.simxFinish(-1)

        # Connect to the V-REP continuous server
        self.clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 500, 5)

        if self.clientID != -1: # if we connected successfully
            print ('Connected to remote API server')

        err_model = vrep.simxLoadModel(self.clientID, self.modelPath, False, self.block_mode)

        if err_model != vrep.simx_return_ok:
            print ("Error is ", err_model)

        if err_model == (0, 16):
            print ('Taking some more time')
            time.sleep(10)

   def simulation_setup(self):

        # # --------------------- Setup the simulation

        vrep.simxSynchronous(self.clientID,True)

        # Mentioning the joint names to later extract joint handles for the same
        joint_names = ['youBotArmJoint0', 'youBotArmJoint1', 'youBotArmJoint2', 'youBotArmJoint3', 'youBotArmJoint4',\
                       'youBotGripperJoint1', 'youBotGripperJoint2']

        # joint target velocities discussed below
        joint_target_velocities = np.ones(len(joint_names)) * 10000000.0

        # get the handles for each joint and set up streaming
        self.joint_handles = [vrep.simxGetObjectHandle(self.clientID,name, self.block_mode)[1] for name in joint_names]

        self.dt = 0.02
        vrep.simxSetFloatingParameter(self.clientID, vrep.sim_floatparam_simulation_time_step, self.dt, vrep.simx_opmode_oneshot) # specify a simulation time step

    # --------------------- Start the simulation

   def start_simulation(self):

       # start our simulation in lockstep with our code
       vrep.simxStartSimulation(self.clientID,vrep.simx_opmode_blocking)
       vrep.simxSetJointPosition(self.clientID, self.joint_handles[1], 1.57, vrep.simx_opmode_oneshot)


   def run_simulation(self, simTime):

        count = simTime
        p = 0
        while count < 1: # run for 1 simulated second

            self.q = np.zeros(len(self.joint_handles))
            self.dq = np.zeros(len(self.joint_handles))
            self.pos = np.zeros(len(self.joint_handles))

            print ("t= %f" %(count))
            for ii, joint_handle in enumerate(self.joint_handles):

                # get the joint angles
                _, self.q[ii] = vrep.simxGetJointPosition(self.clientID, joint_handle, self.block_mode)
                if _ !=0 : raise Exception()

                # get the joint velocityp
                _, self.dq[ii] = vrep.simxGetObjectFloatParameter(self.clientID, joint_handle, 2012, self.block_mode)  # ID for angular velocity of the joint
                if _ !=0 : raise Exception()

                vrep.simxSetJointPosition(self.clientID,joint_handle, p, vrep.simx_opmode_oneshot)

            print (self.joint_handles)
            self.record_demo("Abc.csv")
            print ("Joint Positions in ", self.q*(180/3.14))
            count = count + self.dt
            print ("Time Elapsed in simulation", count)
            p = p + (3.14/180)*5
            print ("p is %f" %(p))

            vrep.simxSynchronousTrigger(self.clientID)

        # stop our simulation
        print ("simulation shutting down")
        vrep.simxStopSimulation(self.clientID,vrep.simx_opmode_blocking)


   def set_joint_angle(self, j_handle, j_angle):

       '''Set the position of a joint to a particular angle

       Currently operating in one-shot mode only
       '''
       vrep.simxSetJointPosition(self.clientID, j_handle, j_angle, vrep.simx_opmode_oneshot)

   def end_vrep(self):
        self.start_process.terminate()
