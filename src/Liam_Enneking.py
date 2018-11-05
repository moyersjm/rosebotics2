"""
  Capstone Project.  Code written by Liam Enneking.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    # stop_on_color(5)  # Red
    stop_robot_with_wave()


def stop_on_color(color, seconds=15):
    start = time.time()
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving()

    while True:
        if robot.color_sensor.get_color() == color:
            robot.drive_system.stop_moving()
            break
        if time.time() - start > seconds:
            robot.drive_system.stop_moving()
            break


def stop_robot_with_wave(seconds=5):
    start = time.time()
    robot = rb.Snatch3rRobot()
    sensor = robot.proximity_sensor()
    robot.drive_system.start_moving()

    while True:
        if sensor.get_distance_to_nearest_object() == 5:
            robot.drive_system.stop_moving()
        if time.time() - start > seconds:
            robot.drive_system.stop_moving()
            break


main()
