from VrepHelper import *


class Manipulator_Commands(VrepHelper):

    def __init__(self):
        VrepHelper.__init__(self)

    def set_joint_angle(self, j_handle, j_angle):
        '''Set the position of a joint to a particular angle
        Currently operating in one-shot mode only
        '''
        vrep.simxSetJointPosition(self.clientID, j_handle, j_angle, vrep.simx_opmode_oneshot)

    def get_joint_angle(self, j_handle):
        '''Get the joint angle value for a particular angle
        Currently operating in one-shot mode only
        '''
        return (vrep.simxGetJointPosition(self.clientID, j_handle, vrep.simx_opmode_oneshot))

    def get_link_pos(self, link_handle, base_frame=-1):
        '''Get the position of the object/link using its handle, in the global frame
        Currently operating in one-shot mode only
        and
        with all the position references in the global frame, so base_frame = -1
        '''
        return (vrep.simxGetObjectPosition(self.clientID, link_handle, base_frame, vrep.simx_opmode_oneshot))

    def display_status_message(self, message):
        '''Display a message in the status bar'''
        vrep.simxAddStatusbarMessage(self.clientID, message, vrep.simx_opmode_oneshot)

    def call_other_scripts(self):
        ''' Call any other script, probably from Lua for the IK service '''

        # vrep.simxCallScriptFunction(self.clientID, scriptDescription=1, scriptHandleOrType, fun )

    def set_object_position(self, j_hanlde1, j_handle2, pos):
        '''Attempt at setting a position for the last joint's handle and then the End-Effector would eventually go there'''

        vrep.simxSetObjectPosition(self.clientID, j_hanlde1, j_handle2, pos, vrep.simx_opmode_oneshot)

