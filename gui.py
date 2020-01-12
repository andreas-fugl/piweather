from kivy.app import App
from kivy.lang import Builder


# TODO for reasom not all nodes are traversed
def find_leaf_nodes(node, dictionary):
    try:
        print(node.name)
        dictionary[node.name] = node
        node.text = "*"
    except:
        pass

    for child in node.children:
        find_leaf_nodes(child, dictionary)

    if len(node.children) == 0:
        return node


class PiWeatherGUI(App):
    leaf_nodes = {}

    def __init__(self, network, **kwargs):
        super().__init__(**kwargs)
        self.network = network

    def build(self):
        return Builder.load_file('piweather.kv')

    def on_start(self):
        # Event handler fired after build()
        print("on start called")

        find_leaf_nodes(self.root, self.leaf_nodes)
        print(self.leaf_nodes)

    def onButton(self, instance):
        # node = visitAllChildren(self.root)
        # print(str(instance.name))
        instance.text = str(self.network.get_data())
