import csv
import matplotlib.pyplot as plt
from VrepHelper import *
from Imitation_Learn import *
from Manipulator_commands import *
import vrep
from evaluate_results import Evaluation

def main():

    filename = 'readdatalog.csv'
    # Create objects
    Vp = VrepHelper()
    Il = Imitation_Learn()
    Mc  = Manipulator_Commands()
    Eval = Evaluation()

    # Initializing the V-REP simulation environment
    Vp.start_vrep(10)
    Vp.initialize_env()
    Vp.simulation_setup()
    Vp.start_simulation()

    obtained_joint_angles = []

    # Parsing the existing demo file
    playback_cache = Il.parse_demo(filename)

    # Playback_cache is a list of lists: read element in the list to extract joint positions

    for positions in playback_cache:
        # Set joint value (position[num]) to respective joint handle
        for num,joint_handle in enumerate(Vp.joint_handles):
            Mc.set_joint_angle(joint_handle, positions[num])
            obtained_joint_angles.append(Mc.get_joint_angle(joint_handle)[1])

        # print ("Given angular positions \n", positions, "\t", type(positions), "\n" )
        # print ("Obtained angular positions \n", obtained_joint_angles, "\t", type(obtained_joint_angles), "\n")

        # Joint domain evaluation
        Eval.main(2, 0,0, positions, obtained_joint_angles)
        obtained_joint_angles = []

        # Cartesian domain evaluation -         SOME SECTIONS STILL UNFINISHED !!
        # p_tip_obs = Mc.get_link_pos(Vp.top_handle)
        # p_tip_des = somehow from the recorded data
        # Eval.main(1,p_tip_des, p_tip_obs)

        # print("Setting to joint positions: ", positions)

        '''Enables synchronous operation mode'''
        vrep.simxSynchronousTrigger(Vp.clientID)

    plt.show()

if __name__ == '__main__':
    main()
