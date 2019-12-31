from kivy.app import App
from kivy.lang import Builder


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


class PiWeatherGUI(App):
    presentation = Builder.load_file('piweather.kv')

    def __init__(self, network, **kwargs):
        super().__init__(**kwargs)
        self.network = network

    def build(self):
        return self.presentation

    def say_hello(self):
        # node = visitAllChildren(self.root)
        print("gui button callback")
        print(self.network.get_data())
