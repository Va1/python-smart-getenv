Python smart getenv
===================

Since environment variables in os.environ are strings, it often appears inconvenient to store and retrieve other
data types such as bool or list. The package provides a single function that wraps os.getenv and allows
you to specify the desired variable type.

Tested and supported types: str, int, float, list. tuple, dict.

`PyPi page`_

Usage
-----

Install:

.. code:: bash

    $ pip install smart-getenv


Prepare the variables:

.. code:: bash

    $ export BOOLEAN=true
    $ export LIST=a,b,c
    $ export TRICKY_LIST=d:e:f
    $ export DICT="{'foo':'bar'}"

Get them:

.. code:: python

    >>> from smart_getenv import getenv
    >>>
    >>> getenv('BOOLEAN', type=str)
    'true'
    >>> getenv('BOOLEAN', type=bool)
    True
    >>> getenv('BOOLEAN', default=False)
    True
    >>> getenv('LIST', type=list)
    ['a', 'b', 'c']
    >>> getenv('LIST', default=[1, 2, 3])
    ['a', 'b', 'c']
    >>> getenv('LIST', type=tuple)
    ('a', 'b', 'c')
    >>> getenv('LIST', default=(1, 2, 3))
    ('a', 'b', 'c')
    >>> getenv('TRICKY_LIST', type=list, separator=':')
    ['d', 'e', 'f']
    >>> getenv('TRICKY_LIST', default=[1, 2, 3], separator=':')
    ['d', 'e', 'f']
    >>> getenv('DICT', type=dict)
    {'foo': 'bar'}
    >>> getenv('DICT', default={'key': 'value'})
    {'foo': 'bar'}
    >>> getenv('LOST', default='default value anyone?')
    'default value anyone?'

Run tests:

.. code:: bash

    $ python tests.py

.. _PyPi page: https://pypi.python.org/pypi/smart-getenv
