=========
play mqtt
=========


.. image:: https://img.shields.io/pypi/v/play_mqtt.svg
        :target: https://pypi.python.org/pypi/play_mqtt

.. image:: https://img.shields.io/travis/tierratelematics/play_mqtt.svg
        :target: https://travis-ci.org/tierratelematics/play_mqtt

.. image:: https://readthedocs.org/projects/play-mqtt/badge/?version=latest
        :target: https://play-mqtt.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/tierratelematics/play_mqtt/shield.svg
        :target: https://pyup.io/repos/github/tierratelematics/play_mqtt/
        :alt: Updates

.. image:: https://codecov.io/gh/tierratelematics/play_mqtt/branch/develop/graph/badge.svg
        :target: https://codecov.io/gh/tierratelematics/play_mqtt


``pytest-play`` support for MQTT support.

Thanks to ``play_mqtt`` you can test the integration between a mocked IoT
device that sends commands on MQTT and a reactive web application with UI checks.

You can also build a simulator that generates messages for you.

* Free software: Apache Software License 2.0
* Documentation: https://play-mqtt.readthedocs.io.


Features
--------


This project defines a new pytest-play_ command:

::

    {"provider": "mqtt",
     "type": "publish",
     "host": "$mqtt_host",
     "port": $mqtt_port,
     "endpoint": '$mqtt_endpoint',
     "payload": {
         "measure_id": [100],
         "obj_id_L": [0],
         "measureType": ["float"],
         "start_time": 1514911926114,
         "bin_value": [77251432]
     }
    }

You can add more commands adding new methods to the command provider implementation in ``providers.py`` module.

More info and examples on:

* pytest-play_, documentation
* cookiecutter-qa_, see ``pytest-play`` in action with a working example if you want to start hacking

Thanks to pytest-play_ you can drive your tests or simulators through a configuration file containing
an array of commands.

Credits
---------

This package was created with Cookiecutter_ and the cookiecutter-play-plugin_ (based on `audreyr/cookiecutter-pypackage`_ project template).

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`cookiecutter-play-plugin`: https://github.com/tierratelematics/cookiecutter-play-plugin
.. _pytest-play: https://github.com/tierratelematics/pytest-play
.. _cookiecutter-qa: https://github.com/tierratelematics/cookiecutter-qa

