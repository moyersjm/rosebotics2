"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Liam.
"""

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():

    robot = rb.Snatch3rRobot()
    rc = RemoteControlEct(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()


    while True:


        # ----------------------------------------------------------------------
        # TODO: 7. Add code that makes the robot beep if the top-red button
        # TODO:    on the Beacon is pressed.  Add code that makes the robot
        # TODO:    speak "Hello. How are you?" if the top-blue button on the
        # TODO:    Beacon is pressed.  Test.  When done, delete this TODO.
        # ----------------------------------------------------------------------
        time.sleep(0.01)  # For the delegate to do its work


class RemoteControlEct(object):
    """
    Stores a robot.
     :type robot: rb.Snatch3rRobot
    """

    def __init__(self, robot):
        self.robot = robot

    def go_forward(self, speed_string):
        speed = int(speed_string)
        print('Robot move')
        self.robot.drive_system.start_moving(speed, speed)


main()