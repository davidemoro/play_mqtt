#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `play_mqtt` package."""
import pytest


@pytest.fixture
def fake_engine():
    import mock
    engine = mock.MagicMock()
    engine.variables = {}
    return engine


def test_provider_command_publish(fake_engine):
    import mock
    with mock.patch('play_mqtt.providers.mqtt') as mock_mqtt:
        from play_mqtt import providers
        provider = providers.MQTTProvider(fake_engine)

        command = {
            'type': 'publish',
            'provider': 'mqtt',
            'comment': 'a comment',
            'host': 'host',
            'port': 10,
            'endpoint': 'some/endpoint',
            'payload': '{"foo": "bar"}'
        }
        provider.command_publish(command)

        assert mock_mqtt.Client.assert_called_once_with() is None
        assert mock_mqtt \
            .Client \
            .return_value \
            .connect \
            .assert_called_with(
                command['host'], port=int(command['port'])) is None
        assert mock_mqtt \
            .Client \
            .return_value \
            .loop_start \
            .assert_called_once_with() is None
        assert mock_mqtt \
            .Client \
            .return_value \
            .loop_stop \
            .assert_called_once_with(
                force=False) is None
        assert mock_mqtt \
            .Client \
            .return_value \
            .publish \
            .assert_called_once_with(
                command['endpoint'], command['payload']) is None


@pytest.mark.parametrize("command", [
    {
        'type': 'subscribe',
        'provider': 'mqtt',
        'host': 'host',
        'port': 10,
        'name': 'some_endpoint_messages',
        'topic': 'some/endpoint',
    },
    {
        'type': 'subscribe',
        'provider': 'mqtt',
        'host': 'host',
        'port': 10,
        'name': 'some_endpoint_messages',
        'topic': ("my/topic", 1)
    },
    {
        'type': 'subscribe',
        'provider': 'mqtt',
        'host': 'host',
        'port': 10,
        'name': 'some_endpoint_messages',
        'topic': [("my/topic", 0), ("another/topic", 2)]
    },
])
def test_provider_command_subscribe(fake_engine, command):
    import mock
    with mock.patch('play_mqtt.providers.mqtt') as mock_mqtt:
        from play_mqtt import providers
        provider = providers.MQTTProvider(fake_engine)

        assert fake_engine.variables == {}
        provider.command_subscribe(command)

        assert provider.engine.variables[command['name']] == []
        assert mock_mqtt.Client.assert_called_once_with(
            userdata=[]) is None
        assert mock_mqtt \
            .Client \
            .return_value \
            .connect \
            .assert_called_with(
                command['host'], port=int(command['port'])) is None
        assert mock_mqtt \
            .Client \
            .return_value \
            .loop_start \
            .assert_called_once_with() is None
        assert mock_mqtt \
            .Client \
            .return_value \
            .loop_stop \
            .called is False
        mock_mqtt.Client.return_value.on_connect(
            mock_mqtt.Client.return_value, None, None, None)
        assert mock_mqtt \
            .Client \
            .return_value \
            .subscribe \
            .assert_called_once_with(
                command['topic']) is None
        assert fake_engine \
            .register_teardown_callback \
            .assert_called_once_with(
                mock_mqtt.Client.return_value.loop_stop) is None
        import collections
        Message = collections.namedtuple("Message", ["payload"])
        mock_mqtt.Client.return_value.on_message(
            mock_mqtt.Client.return_value,
            fake_engine.variables[command['name']],
            Message(payload=b'foo'))
        assert provider.engine.variables[
            command['name']] == ['foo']
