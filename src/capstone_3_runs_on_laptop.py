"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Jonathan Moyers.
"""

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


class Delegate:
    def __init__(self):
        self.return_value = 0

    @staticmethod
    def disp(message):
        update(root_win, message)


root_win = tkinter.Tk()
delegate = Delegate
mqtt_client = com.MqttClient(delegate)

def main():
    """ Constructs and runs a GUI for this program. """
    mqtt_client.connect_to_ev3()
    setup_gui(mqtt_client)

    root_win.mainloop()


def setup_gui(mqtt):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_win, padding=100)
    frame.grid()

    button1 = ttk.Button(frame, text="Follow the line")

    button1.grid()

    button1['command'] = \
        lambda: handle_go(mqtt, 'followcurved')


def update(root_win, message):
    frame = ttk.Frame(root_win, padding=10)
    frame.grid()
    label = ttk.Label(frame, text=message)
    label.grid()


def handle_go(mqtt, message):
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """
    print('sending...', end='')
    mqtt.send_message(message)
    print('Done')



main()
