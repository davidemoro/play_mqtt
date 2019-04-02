import paho.mqtt.client as mqtt
from pytest_play.providers import BaseProvider


class MQTTProvider(BaseProvider):
    """ MQTT provider """

    def command_publish(self, command, **kwargs):
        """ Publish a MQTT message """
        mqttc = mqtt.Client()
        mqttc.connect(
            command['host'],
            port=int(command['port']))

        mqttc.loop_start()

        try:
            mqttc.publish(
                command['endpoint'],
                command['payload'])
        finally:
            mqttc.loop_stop(force=False)

    def command_subscribe(self, command, **kwargs):
        """ Subscribe to a topic or list of topics """
        topic = command['topic']
        encoding = command.get('encoding', 'utf-8')
        if not hasattr(self.engine, '_mqtt'):
            self.engine._mqtt = {}
        self.engine.variables[topic] = []

        def on_connect(client, userdata, flags, rc):
            client.subscribe(topic)

        def on_message(client, userdata, msg):
            userdata.append(msg.payload.decode(encoding))
        self.engine._mqtt[topic] = client = mqtt.Client(
            userdata=self.engine.variables[topic])
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(
            command['host'],
            port=int(command['port'])
        )
        client.loop_start()
        self.engine.register_teardown_callback(
            client.loop_stop)
