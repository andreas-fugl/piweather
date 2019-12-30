#!/usr/bin/env python3

import kivy

from kivy.app import App

import paho.mqtt.client as mqtt


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
    mqttc = mqtt.Client(client_id="PiWeatherApp")
    mqttc.connect("192.168.123.26")
    mqttc.loop_start()
    mqttc.subscribe("debugData")

    def say_hello(self):
        node = visitAllChildren(self.root)


if __name__ == '__main__':
    PiWeatherApp().run()
