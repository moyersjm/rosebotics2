"""
  Capstone Project.  Code written by Grant Duchars.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    polygon_drive(5)

def polygon_drive(n):
    """Makes the robot drive in a polygon shape with n sides"""
    robot = rb.Snatch3rRobot()
    angle = 180 - (360 / n)
    for k in range(n):
      robot.drive_system.go_straight_inches(10)
      robot.drive_system.spin_in_place_degrees(angle)


main()
