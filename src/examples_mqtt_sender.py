""" A simple example of using MQTT for SENDING messages. """

import mqtt_remote_method_calls as com
import time


def main():
    name1 = input("Bob: ")
    name2 = input("David: ")

    mqtt_client = com.MqttClient()
    mqtt_client.connect(name1, name2)
    time.sleep(1)  # Time to allow the MQTT setup.

    while True:
        s = input("Enter a message: ")
        mqtt_client.send_message("say_it", [s])


main()
