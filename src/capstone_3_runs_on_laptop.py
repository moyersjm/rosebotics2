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


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()
    setup_gui(root, mqtt_client)

    root.mainloop()


def setup_gui(root_window, mqtt):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=100)
    frame.grid()

    button1 = ttk.Button(frame, text="Follow the line")
    button2 = ttk.Button(frame, text="Abort")

    button1.grid()
    button2.grid()

    button1['command'] = \
        lambda: handle_go(mqtt, 'followcurved')
    button2['command'] = \
        lambda: handle_go(mqtt, 'stopall')


def handle_go(mqtt, message):
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """
    print('sending...', end='')
    mqtt.send_message(message)
    print('Done')



main()
