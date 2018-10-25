"""
  Capstone Project.  Code written by Jonathan Moyers.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    go_along_line('left', 15)


def go_along_line(direction="left", seconds=30):
    robot = rb.Snatch3rRobot()
    start = time.time()
    while True:
        robot.drive_system.start_moving(100, 100)
        robot.color_sensor.wait_until_intensity_is_greater_than(5)
        if direction.lower() == "left":
            robot.drive_system.start_moving(-10, 100)
        else:
            robot.drive_system.start_moving(100, -10)
        robot.color_sensor.wait_until_intensity_is_less_than(5)
        if time.time() - start > seconds:
            robot.drive_system.stop_moving()
            break



main()
