"""
  Capstone Project.  Code written by Liam Enneking.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time
import ev3dev.ev3 as ev3


def main():
    """ Runs YOUR specific part of the project """
    # stop_on_color(5)  # Red
    robot_beep_with_wave()


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


def robot_beep_with_wave(seconds=15):
    robot = rb.Snatch3rRobot()
    start = time.time()
    sensor = robot.proximity_sensor

    while True:
        print(sensor.get_distance_to_nearest_object_in_inches())
        if sensor.get_distance_to_nearest_object_in_inches() <= 50:
            ev3.Sound.beep().wait()
            break
        if time.time() - start > seconds:
            robot.drive_system.stop_moving()
            break


main()
