from paho.mqtt import client as mqtt


class PiWeatherNetwork(object):
    CLIENT_ID = "PiWeatherApp2"
    BROKER_ADDRESS = "192.168.123.44"

    TOPICS = ["weather/#", "zigbee2mqtt/#"]

    def get_data(self):
        return self.msg_map

    def __on_message(self, client, userdata, msg):
        self.msg_map[msg.topic] = msg.payload

    def __on_connect(self, client, userdata, flags, rc):
        pass

    def __on_disconnect(self, client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnection. Reconnecting...")
        else:
            print("Disconnected successfully")

    def __init__(self):
        self.mqttc = mqtt.Client(client_id=self.CLIENT_ID)

        # setup callbacks
        self.mqttc.on_connect = self.__on_connect
        self.mqttc.on_disconnect = self.__on_disconnect
        self.mqttc.on_message = self.__on_message

        # connect to the broker and subscribe to topics
        for i in range(3):
            try:
                print("Connecting to broker at: '" + self.BROKER_ADDRESS + "'")
                self.mqttc.connect(self.BROKER_ADDRESS)

                for topic in self.TOPICS:
                    print("Subscribing to " + topic)
                    self.mqttc.subscribe(topic)

                self.mqttc.loop_start()
            except:
                print("Connection failed")

        # data members
        self.msg_payload = None
        self.msg_map = {}
