syaml - YAML parser that environment variable is expanded
=========================================================

.. image:: https://travis-ci.org/TakesxiSximada/syaml.svg?branch=master
   :target: https://travis-ci.org/TakesxiSximada/syaml
   :alt: TravisCI Status

.. image:: https://circleci.com/gh/TakesxiSximada/syaml/tree/master.svg?style=svg
   :target: https://circleci.com/gh/TakesxiSximada/syaml/tree/master
   :alt: CircleCI Status

.. image:: https://drone.io/github.com/TakesxiSximada/syaml/status.png
   :target: https://drone.io/github.com/TakesxiSximada/syaml/status.png
   :alt: drone.io Status

.. image:: https://requires.io/github/TakesxiSximada/syaml/requirements.svg?branch=master
   :target: https://requires.io/github/TakesxiSximada/syaml/requirements/?branch=master
   :alt: Requirements Status

Install
-------

::

   $ pip install syaml

How to use it
-------------

A syaml is YAML parser that environment variable is expanded.
It can use the `path`, `name`, `here` and environment variable in YAML file.
It described in syntax of mako template. See http://www.makotemplates.org/ .

A `path` is absolute path to YAML file, and `name` is file name of YAML file,
and `here` is absolute directory path the YAML file stored.

For example.

/path/to/test.yaml::

  - ${here}
  - ${name}
  - ${path}

The above file is equivalent to the following a file. ::

  - /path/to/
  - test.yaml
  - /path/to/test.yaml

And, it can use environment variable in YAML file too.

/path/to/test.yaml::

  - email: ${EMAIL}

If `test@example.com` the environment variable `EMAIL` is set, the above file is equivalent to the following a file. ::

  - email: test@example.com

Other
-----

- PyPI: https://pypi.python.org/pypi/syaml
- Github: https://github.com/TakesxiSximada/syaml
- CircleCI: https://circleci.com/gh/TakesxiSximada/syaml/
- drone.io: https://drone.io/github.com/TakesxiSximada/syaml
- coveralls: https://coveralls.io/github/TakesxiSximada/syaml/
- requires.io: https://requires.io/github/TakesxiSximada/syaml/requirements/
