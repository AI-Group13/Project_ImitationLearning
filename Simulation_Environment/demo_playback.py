import csv

from VrepHelper import *
from Imitation_Learn import *
from Manipulator_commands import *
import vrep

def main():

    filename = 'readdatalog.csv'
    # Create objects
    Vp = VrepHelper()
    Il = Imitation_Learn()
    Mc  = Manipulator_Commands()

    # Initializing the V-REP simulation environment
    Vp.start_vrep(10)
    Vp.initialize_env()
    Vp.simulation_setup()
    Vp.start_simulation()

    '''Parsing the existing demo file'''
    playback_cache = Il.parse_demo(filename)

    '''Playback_cache is a list of lists: read element in the list to extract joint positions'''
    for positions in playback_cache:
        '''Set joint value (position[num]) to respective joint handle'''
        for num,joint_handle in enumerate(Vp.joint_handles):
            vrep.simxSetJointPosition(Vp.clientID, joint_handle, positions[num], vrep.simx_opmode_oneshot)
        print("Setting to joint positions: ", positions)

        '''Enables synchronous operation mode'''
        vrep.simxSynchronousTrigger(Vp.clientID)

if __name__ == '__main__':
    main()
