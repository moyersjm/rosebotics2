"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Liam.
"""


import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


class Returnvalue(object):

    def __init__(self):
        self.return_value = 0

    @staticmethod
    def update_return_value(num):
        update_gui(root, mqtt_client, num)


root = tkinter.Tk()
returnvalue = Returnvalue
mqtt_client = com.MqttClient(returnvalue)


def main():
    """ Constructs and runs a GUI for this program. """
    mqtt_client.connect_to_ev3()
    setup_gui(root, mqtt_client)

    root.mainloop()


def setup_gui(root_window, client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=10)
    frame.grid()

    distance_label = ttk.Label(frame, text='Distance Input:')
    distance = ttk.Entry(frame)
    numsweeps_label = ttk.Label(frame, text='Number of Sweeps Input:')
    numsweeps = ttk.Entry(frame)
    retrieve = ttk.Button(frame, text="Retrieve Object")

    distance_label.grid()
    distance.grid()
    numsweeps_label.grid()
    numsweeps.grid()
    retrieve.grid()

    retrieve['command'] = \
        lambda: sweep_plot(client, distance, numsweeps)


def update_gui(root_window, client, num):
    frame = ttk.Frame(root_window, padding=10)
    frame.grid()
    obj_print = ttk.Label(frame, text='Returned Value: ' + str(num))
    obj_print.grid()
    if num == 1:
        obj_status = ttk.Label(frame, text='Object Found')
        obj_status.grid()
        client.send_message('go_until_hit_color', [1, 100])
    if num == -1:
        obj_status = ttk.Label(frame, text='Object Not Found')
        obj_status.grid()
        client.send_message('go_until_hit_color', [0, 100])


def sweep_plot(client, distance, numsweeps):
    distance = distance.get()
    numsweeps = numsweeps.get()
    client.send_message('sweep_plot', [distance, numsweeps])
    print('Beginning sweep')


'''
def handle_go_forward(client, entrybox):
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """

    speed = entrybox.get()
    client.send_message('go_forward', [speed])
    print('Speed:' + speed)
    print('Robot moving forward')
'''

main()
