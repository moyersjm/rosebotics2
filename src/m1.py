"""
  Capstone Project.  Code written by Jonathan Moyers.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    touch = rb.TouchSensor
    touch.wait_until_pressed()
    print(1)
    touch.wait_until_released()
    print(0)


main()
