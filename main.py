import kivy

from kivy.app import App

class PiWeatherApp(App):
    def say_hello(self):
        print "hello!"       

if __name__ == '__main__':
    PiWeatherApp().run()
