from paho.mqtt import client as mqtt


class PiWeatherNetwork(object):
    CLIENT_ID = "PiWeatherApp2"
    BROKER_ADDRESS = "192.168.123.26"

    TOPICS = ["debugData", "debugData1"]

    def get_data(self):
        return self.msg_map

    def __on_message(self, client, userdata, msg):
        print("PiWeatherApp::on_message_callback, message = ", msg.payload)
        # self.msg_payload = msg.payload
        self.msg_map[msg.topic] = msg.payload

    def __on_connect(self, client, userdata, flags, rc):
        print("PiWeatherApp::on_connect rc=", str(rc))

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

        self.mqttc.connect(self.BROKER_ADDRESS)

        for topic in self.TOPICS:
            self.mqttc.subscribe(topic)
        self.mqttc.loop_start()

        # data members
        self.msg_payload = None
        self.msg_map = {}
