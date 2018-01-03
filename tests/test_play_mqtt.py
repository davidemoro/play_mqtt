#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `play_mqtt` package."""


def test_provider():
    from play_mqtt import providers
    print_provider = providers.NewProvider(None)
    assert print_provider.engine is None
    print_provider.command_print(
        {'provider': 'play_mqtt',
         'type': 'print',
         'message': 'Hello, World!'})
