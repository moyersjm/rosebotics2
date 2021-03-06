"""
  Capstone Project.  Code written by Grant Duchars.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb, time
from ev3dev import ev3


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    robot.drive_system.spin_in_place_degrees(360)
    polygon_drive(robot, 5)
    # run_test_arm(robot)

def polygon_drive(robot, n):
    """Makes the robot drive in a polygon shape with n sides"""
    angle = 360 / n
    for k in range(n):
      robot.drive_system.go_straight_inches(10)
      robot.drive_system.spin_in_place_degrees(angle)

def run_test_arm(robot):
    robot.arm.calibrate()
    time.sleep(1)
    robot.arm.raise_arm_and_close_claw()
    time.sleep(1)
    robot.arm.move_arm_to_position(300)
    time.sleep(1)
    robot.arm.calibrate()


main()
