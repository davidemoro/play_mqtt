=========
play mqtt
=========


.. image:: https://img.shields.io/pypi/v/play_mqtt.svg
        :target: https://pypi.python.org/pypi/play_mqtt

.. image:: https://travis-ci.org/davidemoro/play_mqtt.svg?branch=develop
       :target: https://travis-ci.org/davidemoro/play_mqtt

.. image:: https://readthedocs.org/projects/play-mqtt/badge/?version=latest
        :target: https://play-mqtt.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://codecov.io/gh/davidemoro/play_mqtt/branch/develop/graph/badge.svg
        :target: https://codecov.io/gh/davidemoro/play_mqtt


``pytest-play`` support for MQTT support.

Thanks to ``play_mqtt`` you can test the integration between a mocked IoT
device that sends commands on MQTT and a reactive web application with UI checks.

You can also build a simulator that generates messages for you.

More info and examples on:

* pytest-play_, documentation
* cookiecutter-qa_, see ``pytest-play`` in action with a working example if you want to start hacking


Features
========

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

Twitter
=======

``pytest-play`` tweets happens here:

* `@davidemoro`_

Credits
=======

This package was created with Cookiecutter_ and the cookiecutter-play-plugin_ (based on `audreyr/cookiecutter-pypackage`_ project template).

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`cookiecutter-play-plugin`: https://github.com/davidemoro/cookiecutter-play-plugin
.. _pytest-play: https://github.com/davidemoro/pytest-play
.. _cookiecutter-qa: https://github.com/davidemoro/cookiecutter-qa
.. _`@davidemoro`: https://twitter.com/davidemoro
