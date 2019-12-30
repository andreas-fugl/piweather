from paho.mqtt import client as mqtt


class PiWeatherNetwork(object):
    BROKER_ADDRESS = "192.168.123.26"

    def on_message(self, client, userdata, msg):
        print("PiWeatherApp::on_message_callback, message = ", msg.payload)

    def on_connect(self, client, userdata, flags, rc):
        print("PiWeatherApp::on_connect rc=", str(rc))

    def on_disconnect(self, client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnection. Reconnecting...")
        else:
            print("Disconnected successfully")

    def __init__(self):
        self.mqttc = mqtt.Client(client_id="PiWeatherApp2")

        # setup callbacks
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_disconnect = self.on_disconnect
        self.mqttc.on_message = self.on_message

        self.mqttc.connect(self.BROKER_ADDRESS)
        self.mqttc.subscribe("debugData")
        self.mqttc.loop_start()
