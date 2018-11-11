"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Grant Duchars.
"""

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    robot = rb.Snatch3rRobot()

    rc = RemoteControlEtc(robot)

    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()
    
    while True:
        time.sleep(0.01)  # For the delegate to do its work

        # Tests for color and plays a tone with specific frequency based on color
        if robot.color_sensor.get_color() == 5 and rc.song_active == 1:
            ev3.Sound.tone(rc.notes_list[0],500)
        elif robot.color_sensor.get_color() == 3 and rc.song_active == 1:
            ev3.Sound.tone(rc.notes_list[1],500)
        elif robot.color_sensor.get_color() == 2 and rc.song_active == 1:
            ev3.Sound.tone(rc.notes_list[2],500)
        elif robot.color_sensor.get_color() == 4 and rc.song_active == 1:
            ev3.Sound.tone(rc.notes_list[3],500)
        elif robot.color_sensor.get_color() == 7 and rc.song_active == 1:
            ev3.Sound.tone(rc.notes_list[4],500)
        elif robot.color_sensor.get_color() == 1 and rc.song_active == 1:
            ev3.Sound.tone(rc.notes_list[5],500)

        # Tests for an object in front of the robot and stops if within 2 inches
        if robot.proximity_sensor.get_distance_to_nearest_object_in_inches() <= 2:
            robot.drive_system.stop_moving()
            rc.song_active = 0

class RemoteControlEtc(object):

    def __init__(self, robot):
        """
        Stores a robot.
          :type robot: rb.Snatch3rRobot
        """

    def set_notes(self, note1Str, note2Str, note3Str, note4Str, note5Str, note6Str):
        """Sets values for six notes and stores them into a list to be called upon later"""
        note1 = int(note1Str)
        note2 = int(note2Str)
        note3 = int(note3Str)
        note4 = int(note4Str)
        note5 = int(note5Str)
        note6 = int(note6Str)
        self.notes_list = [note1,note2,note3,note4,note5,note6]

    def go_forward(self, speed_string):
        """Makes the robot move forward until stopped elsewhere"""
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)
        self.song_active = 1
    
    def stop_robot(self):
        """Stops the robot"""
        self.robot.drive_system.stop_moving()
        self.song_active = 0


main()