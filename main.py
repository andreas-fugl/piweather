#!/usr/bin/env python3

from gui import PiWeatherGUI
from network import PiWeatherNetwork

if __name__ == '__main__':
    network = PiWeatherNetwork()
    gui = PiWeatherGUI(network)
    gui.run()
