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
    ev3.Sound.beep()

    while True:
        time.sleep(0.01)  # For the delegate to do its work
        '''
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep().wait()
        if robot.beacon_button_sensor.is_top_blue_button_pressed():
            ev3.Sound.speak('Onward my comrades').wait()
        '''


def return_value_to_pc(return_value, mqtt_client=com.MqttClient()):
    mqtt_client.connect_to_pc()
    mqtt_client.send_message('update_return_value', [return_value])


class RemoteControlEct(object):

    def __init__(self, robot):
        self.robot = robot
        self.tracker = 0

    def check_for_item(self):
        sensor = self.robot.proximity_sensor
        print(sensor.get_distance_to_nearest_object_in_inches())
        if sensor.get_distance_to_nearest_object_in_inches() <= 50:
            self.robot.drive_system.stop_moving()
            self.robot.arm.raise_arm_and_close_claw()
            ev3.Sound.speak('Item Acquired')
            return_value_to_pc(1)
            return True
        else:
            return False

    def sweep_plot(self, distance_string, numsweeps_string):
        ev3.Sound.speak('Beginning Sweep')
        self.tracker = 0
        distance = int(distance_string)
        numsweeps = int(numsweeps_string)
        for k in range(numsweeps):
            if k % 2 != 1:
                self.robot.drive_system.go_straight_inches(distance)
                if self.check_for_item() is True:
                    break
                self.robot.drive_system.spin_in_place_degrees(90, 1)
                if self.check_for_item() is True:
                    break
                self.robot.drive_system.go_straight_inches(8)
                if self.check_for_item() is True:
                    break
                self.robot.drive_system.spin_in_place_degrees(90, 1)
                if self.check_for_item() is True:
                    break
                self.tracker = self.tracker + 1
                print(self.tracker)
            if k % 2 == 1:
                self.robot.drive_system.go_straight_inches(distance)
                if self.check_for_item() is True:
                    break
                self.robot.drive_system.spin_in_place_degrees(90, 2)
                if self.check_for_item() is True:
                    break
                self.robot.drive_system.go_straight_inches(8)
                if self.check_for_item() is True:
                    break
                self.robot.drive_system.spin_in_place_degrees(90, 2)
                if self.check_for_item() is True:
                    break
                self.tracker = self.tracker + 1
                print(self.tracker)
        if self.tracker == numsweeps:
            return_value_to_pc(-1)
        return

    def go_until_hit_color(self, calibrate_string, speed_string):
        calibrate = calibrate_string
        speed = speed_string
        self.robot.drive_system.start_moving(int(speed))

        while True:
            if self.robot.color_sensor.get_color() == 6:
                self.robot.drive_system.stop_moving()
                if calibrate == 1:
                    self.robot.arm.calibrate()
                break

    '''
    def go_forward(self, speed_string):
        speed = int(speed_string)
        print('Robot move')
        self.robot.drive_system.start_moving(speed, speed)
    '''


main()
