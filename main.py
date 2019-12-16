#!/usr/bin/env python3

import kivy

from kivy.app import App
from kivy.clock import Clock

import paho.mqtt.publish as publish

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
    def say_hello(self):
        node = visitAllChildren(self.root)
        print("Callback called")
        publish.single("piweatherApp", "0", hostname="192.168.123.26")

if __name__ == '__main__':
    PiWeatherApp().run()


