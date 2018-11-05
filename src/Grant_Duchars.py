"""
  Capstone Project.  Code written by Grant Duchars.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb, time
from ev3dev import ev3


def main():
    """ Runs YOUR specific part of the project """
    # polygon_drive(5)
    run_test_arm()

def polygon_drive(n):
    """Makes the robot drive in a polygon shape with n sides"""
    robot = rb.Snatch3rRobot()
    angle = 360 / n
    for k in range(n):
      robot.drive_system.go_straight_inches(10)
      robot.drive_system.spin_in_place_degrees(angle)

def run_test_arm():
    print('Start Arm Tests')
    print('')
    print('Start Initial Calibrate')
    robot = rb.Snatch3rRobot()
    ev3.Sound.beep().wait()
    print('Finish Initial Calibrate')
    time.sleep(1)
    print('Start Test Calibrate')
    robot.arm.calibrate()
    ev3.Sound.beep().wait()
    print('Finish Test Calibrate')
    time.sleep(1)
    print('Start Raise and Close')
    robot.arm.raise_arm_and_close_claw()
    ev3.Sound.beep().wait()
    print('Finish Raise and Close')
    time.sleep(1)
    print('Start Move to Position')
    robot.arm.move_arm_to_position(300)
    ev3.Sound.beep().wait()
    print('Finish Move to Position')
    print('')
    print('Finished Tests')


main()
