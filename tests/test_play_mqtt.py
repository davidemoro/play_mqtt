#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `play_mqtt` package."""

import mock
import json


def test_provider():
    from play_mqtt import providers
    provider = providers.MQTTProvider(None)
    assert provider.engine is None
    assert provider.command_publish


def test_provider_command():
    from play_mqtt import providers
    with mock.patch('play_mqtt.providers.mqtt') as mock_mqtt:
        provider = providers.MQTTProvider(None)
        assert mock_mqtt.Client.assert_called_with() is None
        assert provider.mqttc is mock_mqtt.Client.return_value

        command = {
            'type': 'publish',
            'provider': 'mqtt',
            'comment': 'a comment',
            'host': 'host',
            'port': 10,
            'endpoint': 'some/endpoint',
            'payload': {'foo': 'bar'}
        }
        provider.command_publish(command)

        assert provider.mqttc.connect.assert_called_with(
            command['host'], port=int(command['port'])) is None
        assert provider.mqttc.loop_start.assert_called_once_with() is None
        assert provider.mqttc.loop_stop.assert_called_once_with(
            force=False) is None
        assert provider.mqttc.publish.assert_called_once_with(
            command['endpoint'], json.dumps(command['payload'])) is None
