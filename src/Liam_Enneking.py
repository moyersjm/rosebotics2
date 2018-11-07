"""
  Capstone Project.  Code written by Liam Enneking.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time
import tkinter
import tkinter as ttk


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


def stop_robot_with_wave(seconds=15):
    robot = rb.Snatch3rRobot()
    start = time.time()
    sensor = robot.proximity_sensor
    robot.drive_system.start_moving()

    while True:
        print(sensor.get_distance_to_nearest_object_in_inches())
        if sensor.get_distance_to_nearest_object_in_inches() <= 5:
            robot.drive_system.stop_moving()
            break
        if time.time() - start > seconds:
            robot.drive_system.stop_moving()
            break

def move_on_button_press(seconds=15):
    robot = rb.Snatch3rRobot()
    root = tkinter.Tk()
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()
    my_entry_box = ttk.Entry(frame1)
    my_entry_box.grid()
    button1 = ttk.Button
    button1['command'] = (lambda: move_forward(my_entry_box.get()))


def move_forward(entry):
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(entry)

main()
