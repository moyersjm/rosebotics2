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
import math


class Controller(object):

    def __init__(self, robot):
        """
        Stores a robot.
          :type robot: rb.Snatch3rRobot
        """
        self.robot = robot
        self.direction = 2
        self.mqtt_send = com.MqttClient()
        self.mqtt_send.connect_to_pc()

    def forward(self, speedstr):
        speed = int(speedstr)
        self.robot.drive_system.left_wheel.start_spinning(speed)
        self.robot.drive_system.right_wheel.start_spinning(speed)
        time.sleep(5)
        self.robot.drive_system.left_wheel.stop_spinning()
        self.robot.drive_system.right_wheel.stop_spinning()

    """def turnandgo(self):
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
        return"""

    def followcurved(self):

        self.mqtt_send.send_message('disp', ["Let's go!"])
        while True:
            self.robot.drive_system.start_moving(100, 100)

            # will wait until the robot leaves the line or encounters object
            while self.robot.color_sensor.get_reflected_intensity() < 15:
                print(self.robot.color_sensor.get_reflected_intensity())
                time.sleep(.01)
                if self.robot.proximity_sensor.get_distance_to_nearest_object_in_inches() < 30:
                    self.go_around()

            # does this if off the track
            if self.direction == 1:
                self.robot.drive_system.start_moving(-50, 100)
            if self.direction == 2:
                self.robot.drive_system.start_moving(100, -50)

            start = time.time()
            # in case it was the opposite turn the whole time, the robot does not go backwards
            while True:
                if self.direction == 1 and time.time() - start >= 0.5:
                    self.robot.drive_system.start_moving(100, -50)
                    self.robot.color_sensor.wait_until_intensity_is_less_than(15)
                    self.direction = 2
                    break
                if self.direction == 2 and time.time() - start >= 0.5:
                    self.robot.drive_system.start_moving(-50, 100)
                    self.robot.color_sensor.wait_until_intensity_is_less_than(15)
                    self.direction = 1
                    break
                if self.robot.color_sensor.get_reflected_intensity() <= 15:
                    break

    def go_around(self):
        # does this if object is in the way
        self.mqtt_send.send_message('disp', ['Object detected!'])
        self.robot.drive_system.start_moving(-100, -100)
        time.sleep(.5)
        self.robot.drive_system.left_wheel.reset_degrees_spun()
        self.robot.drive_system.stop_moving()
        self.robot.drive_system.turn_degrees(30, 1)
        self.robot.drive_system.start_moving(100, 100)
        time.sleep(2)
        self.robot.drive_system.stop_moving()
        self.robot.drive_system.turn_degrees(75, 2)
        self.robot.drive_system.start_moving(100, 100)
        self.robot.color_sensor.wait_until_intensity_is_less_than(15)
        self.robot.drive_system.stop_moving()
        self.robot.drive_system.turn_degrees(30, 1)
        self.mqtt_send.send_message('disp', ['Crisis averted!'])
        self.robot.drive_system.start_moving(100, 100)

    def stopall(self):
        self.robot.drive_system.stop_moving()
        ev3.Sound.beep().wait()
        print('Program aborted')
        exit()


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
