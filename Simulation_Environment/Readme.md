Contains the files to run the project in V-REP simulation environment using the Python Remote API

Updates

1. Pushed the robot model and the empty scene 
2. Initial helper function and test script to simulate arbitrary movements
3. Change the directory path to  "./vrep.sh" in the VrepHelper class to run on your machine


IK-ROS function guide:
The model communicates via rostopics with the help of a vrep-ros plugin. You can get this code to work as intended by following these steps:

1. clone this repository - https://github.com/CoppeliaRobotics/v_repExtRosInterface - and follow the instructions to build it [IMPORTANT: DO NOT CHANGE THE NAME OF THIS FOLDER]
2. Run roscore in separate terminal and keep it open
3. Test the working by running the scene named: rosInterfaceTopicPublisherAndSubscriber.ttt
4. If it works, go ahead and cut/paste this folder inside your vrep folder (do not change it's name)
5. Load the model "youbot_ros_modified.ttm"
6. Access the child-script (The little page icon next to YouBot object), go to line 61 and replace the file-open address to any address of your choice
7. Save the model and run the simulation
8. Run the python file "ros_vrep_communication.py" in a separate terminal. The robot should be reading the IK commands from your rostopic at this point.
