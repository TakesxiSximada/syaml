syaml - YAML parser that environment variable is expanded
=========================================================

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

Load file and Load string
^^^^^^^^^^^^^^^^^^^^^^^^^^

Example file /path/to/syaml/example.yml::

  general:
    - ${here}
    - ${name}
    - ${path}

Load file object::

   >>> import syaml
   >>> with open('example.yml', 'rb') as fp:
   ...     syaml.load(fp)
   ...
   {'general': ['/path/to/syaml', 'example.yml', '/path/to/syaml/example.yml']}

Load byte string object::

   >>> syaml.loads(b'general:\n  - ${here}\n  - ${name}\n  - ${path}\n')
   {'general': ['', '', '']}

Load string object::

   >>> syaml.loads('general:\n  - ${here}\n  - ${name}\n  - ${path}\n')
   {'general': ['', '', '']}
   >>>

`name` and `path` and `here`  will replace to empty string If you passed a string to syaml.loads function.
They are for a file object. A string like object don't have file path.


Use command line tool
^^^^^^^^^^^^^^^^^^^^^^

syaml render
~~~~~~~~~~~~

It render the SAYML file.

example.yml::

   general:
     - ${here}
     - ${name}
     - ${path}

Execute syaml render command::

   $ syaml render example.yml
   general:
   - /path/to/syaml
   - example.yml
   - /path/to/syaml/example.yml

Execute syaml render command json style::

   $ syaml render example.yml --json
   {"general": ["/path/to/syaml", "example.yml", "/path/to/syaml/example.yml"]}

Execute syaml render command pre process only::

  $ syaml render example.yml --pre
  general:
    - /path/to/syaml
    - example.yml
    - /path/to/syaml/example.yml


Unittest
--------

This section describes the tools and tips used when unittest.
Run these tests with the following command::

  $ python -m unittest discover src

If all tests pass, you will see the following output::

  ....
  ----------------------------------------------------------------------
  Ran 4 tests in 0.018s

  OK

The number of tests performed may be higher than described in this document.


Test with docker
----------------

Build docker image::

  $ docker buildx build -t syaml .

Run test::

  $ docker run -it --rm --workdir="/app" --volume "$(pwd):/app" --name="syaml" syaml tox


Release flow
------------

- Bump version. Edit setup.cfg file.
- Generate distribution files. `python -m build`.
- Check distribution files. `twine check dist/*`.
   - You need to make sure there are no "errors" displayed on the console.
- Upload distribution files. `twine upload dist/*`.


Other
-----

- PyPI: https://pypi.python.org/pypi/syaml
- Github: https://github.com/TakesxiSximada/syaml
