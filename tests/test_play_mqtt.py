#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `play_mqtt` package."""


def test_provider():
    from play_mqtt import providers
    print_provider = providers.MQTTProvider(None)
    assert print_provider.engine is None
    assert print_provider.command_publish
