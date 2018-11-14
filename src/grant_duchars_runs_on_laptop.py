"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Grant Duchars.
"""

# Video URL: https://youtu.be/y4b5jkECDXg

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()
    setup_gui(root,mqtt_client)
    root.mainloop()


def setup_gui(root_window, client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=50)
    frame.grid()

    # Speed entry for robot movement
    speed_entry_box = ttk.Entry(frame)
    speed_lable = ttk.Label(frame,text='Speed')
    # Play button to start moving robot
    play_button = ttk.Button(frame, text="Play Song")
    # Stop button to stop the robot
    stop_button = ttk.Button(frame, text='Stop')
    # Set Notes button for send note values to robot
    set_notes_button = ttk.Button(frame, text="Set Notes")

    # Entry boxes with a lable for each of the six notes
    # (Entry boxes are filled with default values for C major)
    note1_entry_box = ttk.Entry(frame)
    note1_entry_box.insert(0, '261.63')
    note1_lable = ttk.Label(frame,text='Note 1')
    note2_entry_box = ttk.Entry(frame)
    note2_entry_box.insert(0, '293.665')
    note2_lable = ttk.Label(frame,text='Note 2')
    note3_entry_box = ttk.Entry(frame)
    note3_entry_box.insert(0, '329.628')
    note3_lable = ttk.Label(frame,text='Note 3')
    note4_entry_box = ttk.Entry(frame)
    note4_entry_box.insert(0, '349.228')
    note4_lable = ttk.Label(frame,text='Note 4')
    note5_entry_box = ttk.Entry(frame)
    note5_entry_box.insert(0, '391.995')
    note5_lable = ttk.Label(frame,text='Note 5')
    note6_entry_box = ttk.Entry(frame)
    note6_entry_box.insert(0, '440')
    note6_lable = ttk.Label(frame,text='Note 6')
    
    # Draws the elements on the screen in specific rows and columns
    speed_entry_box.grid(row=8,column=0)
    speed_lable.grid(row=7,column=0)
    play_button.grid(row=8,column=1)
    stop_button.grid(row=9,column=1)
    set_notes_button.grid(row=6,column=1)

    note1_lable.grid(row=0,column=0)
    note1_entry_box.grid(row=1,column=0)
    note2_lable.grid(row=0,column=1)
    note2_entry_box.grid(row=1,column=1)
    note3_lable.grid(row=2,column=0)
    note3_entry_box.grid(row=3,column=0)
    note4_lable.grid(row=2,column=1)
    note4_entry_box.grid(row=3,column=1)
    note5_lable.grid(row=4,column=0)
    note5_entry_box.grid(row=5,column=0)
    note6_lable.grid(row=4,column=1)
    note6_entry_box.grid(row=5,column=1)
    
    # Gives buttons fuctions the robot can perform
    play_button['command'] = \
        lambda: handle_go_forward(speed_entry_box, client)
    
    stop_button['command'] = \
        lambda: handle_stop_robot(client)

    set_notes_button['command'] = \
        lambda: handle_set_notes(note1_entry_box,
                                  note2_entry_box,
                                  note3_entry_box,
                                  note4_entry_box,
                                  note5_entry_box,
                                  note6_entry_box,
                                  client)


def handle_go_forward(entry, client):
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """
    speed = entry.get()
    client.send_message('go_forward',[speed])
    print('Sending go_forward to the robot with a speed:',speed)

def handle_stop_robot(client):
    """
    Tells the robot to stop.
    """
    client.send_message('stop_robot')
    print('Sending stop_robot to the robot')
    
def handle_set_notes(entry1,entry2,entry3,entry4,entry5,entry6, client):
    """
    Tells the robot to set the notes with the given values from the notes' entry boxes.
    """
    note1 = entry1.get()
    note2 = entry2.get()
    note3 = entry3.get()
    note4 = entry4.get()
    note5 = entry5.get()
    note6 = entry6.get()
    client.send_message('set_notes',[note1,note2,note3,note4,note5,note6])
    print('Sending set_notes to the robot with the notes:',note1,note2,note3,note4,note5,note6)

main()
