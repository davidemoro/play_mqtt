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
        name = command['name']
        if not hasattr(self.engine, '_mqtt'):
            self.engine._mqtt = {}
        self.engine.variables[name] = []

        def on_message(client, userdata, msg):
            userdata.append(msg.payload.decode(encoding))
        self.engine._mqtt[name] = client = mqtt.Client(
            userdata=self.engine.variables[name])
        client.on_message = on_message
        client.connect(
            command['host'],
            port=int(command['port'])
        )
        client.subscribe(topic)
        client.loop_start()
        self.engine.register_teardown_callback(
            client.loop_stop)
