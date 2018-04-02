from VrepHelper import *
import vrep


def main():

    Vp = VrepHelper()
    Vp.start_vrep(10)
    Vp.initialize_env()
    Vp.simulation_setup()
    Vp.start_simulation()
    Vp.run_simulation(0)

if __name__ == '__main__':
    main()


