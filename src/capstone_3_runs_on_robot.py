"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Jonathan Moyers.
"""

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


class Controller(object):

    def __init__(self, robot):
        """
        Stores a robot.
          :type robot: rb.Snatch3rRobot
        """
        self.robot = robot

    def forward(self, speedstr):
        speed = int(speedstr)
        self.robot.drive_system.left_wheel.start_spinning(speed)
        self.robot.drive_system.right_wheel.start_spinning(speed)
        time.sleep(5)
        self.robot.drive_system.left_wheel.stop_spinning()
        self.robot.drive_system.right_wheel.stop_spinning()

    def turnandgo(self):
        self.robot.drive_system.left_wheel.start_spinning(100)
        self.robot.drive_system.right_wheel.start_spinning(-100)
        while self.robot.beacon_sensor.get_heading_to_beacon() != 1:
            time.sleep(.01)
            print(self.robot.beacon_sensor.get_heading_to_beacon())
        self.robot.drive_system.right_wheel.start_spinning(100)
        while self.robot.beacon_sensor.get_distance_to_beacon() > 1:
            time.sleep(.01)
        self.robot.drive_system.right_wheel.stop_spinning()
        self.robot.drive_system.left_wheel.stop_spinning()
        return



def main():
    robot = rb.Snatch3rRobot()
    ev3.Sound.beep().wait()

    delegate = Controller(robot)
    mqtt_client = com.MqttClient(delegate)
    print('connecting to pc...', end='')
    mqtt_client.connect_to_pc()
    print('Done')
    while True:
        time.sleep(0.01)  # For the delegate to do its work
        """if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep().wait()
        if robot.beacon_button_sensor.is_top_blue_button_pressed():
            ev3.Sound.speak('You pressed the. Blue. Button on the. Top.').wait()"""


main()
