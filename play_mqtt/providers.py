import paho.mqtt.client as mqtt
from pytest_play.providers import BaseProvider


class MQTTProvider(BaseProvider):
    """ MQTT provider """

    def __init__(self, engine):
        super(MQTTProvider, self).__init__(engine)
        self.mqttc = mqtt.Client()

    def command_publish(self, command, **kwargs):
        """ Publish a MQTT message """
        self.mqttc.connect(
            command['host'],
            port=int(command['port']))

        self.mqttc.loop_start()

        try:
            self.mqttc.publish(
                command['endpoint'],
                command['payload'])
        finally:
            self.mqttc.loop_stop(force=False)
