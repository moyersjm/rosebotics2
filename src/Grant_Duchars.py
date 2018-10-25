"""
  Capstone Project.  Code written by Grant Duchars.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    robot.drive_system.left_wheel.reset_degrees_spun()
    robot.drive_system.right_wheel.reset_degrees_spun()
    robot.drive_system.spin_in_place_degrees(90)
    leftDegrees = robot.drive_system.left_wheel.get_degrees_spun()
    rightDegrees = robot.drive_system.right_wheel.get_degrees_spun()
    print(leftDegrees, rightDegrees)

main()
