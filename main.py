#!/usr/bin/env python3

import paho.mqtt.client as mqtt
from kivy.app import App


def visitAllChildren(node):
    try:
        print(node.name)
        node.text = "*"
    except:
        pass

    try:
        node.text = "*"
    except:
        pass

    if len(node.children) == 0:
        return

    for child in node.children:
        visitAllChildren(child)


class PiWeatherApp(App):
    def on_message_callback(client, userdata, message):
        print("PiWeatherApp::on_message_callback")

    def on_connect(client, userdata, flags, rc):
        print("PiWeatherApp::on_connect rc=%s", str(rc))

    def on_disconnect(mqttc, userdata, rc):
        if rc != 0:
            print("Unexpected disconnection. Reconnecting...")
            # mqttc.reconnect()
        else:
            print("Disconnected successfully")

    mqttc = mqtt.Client(client_id="PiWeatherApp2")

    # setup callbacks
    mqttc.on_connect = on_connect
    mqttc.on_disconnect = on_disconnect
    mqttc.on_message = on_message_callback

    mqttc.connect("192.168.123.26")
    mqttc.loop_start()
    mqttc.subscribe("debugData")

    def say_hello(self):
        # node = visitAllChildren(self.root)
        print(self.mqttc.is_connected())


if __name__ == '__main__':
    PiWeatherApp().run()
