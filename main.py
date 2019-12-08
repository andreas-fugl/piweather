import kivy
kivy.require('1.1.1')

from kivy.app import App
from kivy.clock import Clock

import bme280

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
        (chip_id, chip_version) = bme280.readBME280ID()
        print("Chip ID     :", chip_id)
        print("Version     :", chip_version)

        temperature,pressure,humidity = bme280.readBME280All()


        print("Temperature : ", temperature, "C")
        print("Pressure : ", pressure, "hPa")
        print("Humidity : ", humidity, "%")



if __name__ == '__main__':
    PiWeatherApp().run()


