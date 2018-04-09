from VrepHelper import *
from Imitation_Learn import *
from Manipulator_commands import *
import vrep

def main(simTime):

    # Create objects
    Vp = VrepHelper()
    Il = Imitation_Learn()
    Mc  = Manipulator_Commands()

    # Initializing the V-REP simulation environment
    Vp.start_vrep(10)
    Vp.initialize_env()
    Vp.simulation_setup()
    Vp.start_simulation()

    p, count = 0, 0

    while count < simTime:  # run for 1 simulated second

        Vp.q = np.zeros(len(Vp.joint_handles))
        Vp.dq = np.zeros(len(Vp.joint_handles))
        Vp.pos = np.zeros(len(Vp.joint_handles))

        print("t= %f" % (count))
        for ii, joint_handle in enumerate(Vp.joint_handles):

            # get the joint angles
            _, Vp.q[ii] = vrep.simxGetJointPosition(Vp.clientID, joint_handle, Vp.block_mode)
            if _ != 0: raise Exception()

            # get the joint velocity
            # _, Vp.dq[ii] = vrep.simxGetObjectFloatParameter(Vp.clientID, joint_handle, 2012,
            #                                                   Vp.block_mode)  # ID for angular velocity of the joint
            # if _ != 0: raise Exception()

            vrep.simxSetJointPosition(Vp.clientID, joint_handle, p, vrep.simx_opmode_oneshot)

        # print (Vp.joint_handles)

        Il.log_data(Vp.q.tolist(), 'readdatalog.csv')
        # if _ != 0: raise Exception ("Data logging failed in main code")

        print("Joint Positions in ", Vp.q * (180 / 3.14))
        count = count + Vp.dt

        print("Time Elapsed in simulation", count)
        p = p + (3.14 / 180) * 5
        print("p is %f" % (p))

        vrep.simxSynchronousTrigger(Vp.clientID)

    # stop our simulation
    print("simulation shutting down")

if __name__ == '__main__':
    main(1)









