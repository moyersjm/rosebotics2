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
        self.direction = 1

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
        while True:
            self.robot.drive_system.start_moving(100, 100)

            # will wait until the robot leaves the line or encounters object
            while self.robot.color_sensor.get_reflected_intensity() > 95:
                time.sleep(.01)
                if self.robot.proximity_sensor.get_distance_to_nearest_object_in_inches() < 3:
                    self.go_around(self.robot.proximity_sensor.get_distance_to_nearest_object_in_inches())

            # does this if off the track
            if self.direction == 1:
                self.robot.drive_system.right_wheel.reset_degrees_spun()
                self.robot.drive_system.start_moving(-10, 100)
            if self.direction == 2:
                self.robot.drive_system.left_wheel.reset_degrees_spun()
                self.robot.drive_system.start_moving(100, -10)
            self.robot.color_sensor.wait_until_intensity_is_greater_than(90)

            # in case it was the opposite turn the whole time, the robot does not go backwards
            if self.direction == 1:
                if self.robot.drive_system.right_wheel.get_degrees_spun() > 170:
                    self.robot.drive_system.start_moving(-10, 100)
                    self.robot.color_sensor.wait_until_intensity_is_less_than(90)
                    self.robot.color_sensor.wait_until_intensity_is_greater_than(90)
                    self.direction = 2
            elif self.direction == 2:
                if self.robot.drive_system.left_wheel.get_degrees_spun() > 170:
                    self.robot.drive_system.start_moving(100, -10)
                    self.robot.color_sensor.wait_until_intensity_is_less_than(90)
                    self.robot.color_sensor.wait_until_intensity_is_greater_than(90)
                    self.direction = 1

    def go_around(self, distance):
        # does this if object is in the way
        print('Object sighted {dist} inches away!').format(distance)
        self.robot.drive_system.go_straight_inches(-3)
        self.robot.drive_system.left_wheel.reset_degrees_spun()
        while self.robot.proximity_sensor.get_distance_to_nearest_object_in_inches() < 10:
            self.robot.drive_system.start_moving(100, -100)
        deg = self.robot.drive_system.left_wheel.get_degrees_spun()
        hypotenuse = distance * math.cos(deg)
        self.robot.drive_system.go_straight_inches(hypotenuse)
        self.robot.drive_system.spin_in_place_degrees(-deg)
        self.robot.drive_system.go_straight_inches(1)
        self.robot.drive_system.spin_in_place_degrees(-deg)
        self.robot.drive_system.start_moving(100, 100)
        self.robot.color_sensor.wait_until_intensity_is_less_than(5)
        self.robot.drive_system.turn_degrees(deg)
        print('Crisis averted!')
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
