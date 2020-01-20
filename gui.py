from kivy.app import App
from kivy.lang import Builder
from kivy.logger import Logger as log
from kivy.clock import Clock


def build_node_dictionary(node, dictionary):
    """Recursively builds a dictionary of names for node and its children"""
    try:
        dictionary[node.name] = node
    except AttributeError:
        # TODO: For some reason this error detection actually does not work for buttons!
        log.warn("gui.py: " + str(node) + " does not have the 'name' attribute. Will not be accessible")

    for child in node.children:
        build_node_dictionary(child, dictionary)


class PiWeatherGUI(App):
    nodes = {}

    def __init__(self, network, **kwargs):
        super().__init__(**kwargs)
        self.network = network

    def build(self):
        return Builder.load_file('piweather.kv')

    def update_gui_nodes(self):
        self.nodes["m2leftbutton"].text = str(self.network.get_data())

    def on_timer(self, dt):
        """Timer handler"""
        self.update_gui_nodes()

    def on_start(self):
        """Event handler fired after kivy.App.build()"""
        build_node_dictionary(self.root, self.nodes)

        self.update_gui_nodes()

        Clock.schedule_interval(self.on_timer, 1.0)

    def on_button_press(self, instance):
        """Event handler for button press"""
        log.debug("onButton: " + str(instance.name))
