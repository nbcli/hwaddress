=========
hwaddress
=========

Lightweight python library for EUI-48, EUI-64 based hardware (MAC) addresses. 

.. contents::
    :local:


Quick start & Example usage
---------------------------

* Installing with pip

    .. code:: bash

        $ pip install hwaddress

* Import Generic hwaddress objects

    .. code:: python

        >>> from hwaddress import MAC, MAC_64, GUID

.. code:: python

    >>> MAC.verify('12:34:56:78:90:ab')
    True
    >>> MAC.verify('12-34-56-78-90-ab')
    False
    >>> mac = MAC('12:34:56:78:90:ab')
    >>> mac
    MAC(12:34:56:78:90:ab)
    >>> str(mac)
    '12:34:56:78:90:ab'
    >>> mac.format(delimiter='-')
    '12-34-56-78-90-ab'
    >>> mac.int
    20015998341291
    >>> mac.hex
    '0x1234567890ab'
    >>> mac.binary
    '0001 0010 0011 0100 0101 0110 0111 1000 1001 0000 1010 1011'

.. code:: python

    >>> MAC_64.verify('12:34:56:78:90:ab')
    False
    >>> MAC_64.verify('12:34:56:78:90:ab:cd:ef')
    True
    >>> MAC_64('0x1234567890abcdef').format(group=4, upper=True)
    '1234:5678:90AB:CDEF'

.. code:: python

    >>> GUID.verify('12345678-90ab-cdef-1234-567890abcdef')
    True
    >>> GUID.verify('1234-5678-90ab-cdef-1234-5678-90ab-cdef')
    False
    >>> guid = GUID('123-45678-90ab-cdef-1234-5678:90ab.cdef')
    >>> guid
    GUID(12345678-90ab-cdef-1234-567890abcdef)
    >>> guid.format(':', 4)
    '1234:5678:90ab:cdef:1234:5678:90ab:cdef'


Included Hardware Address Classes
---------------------------------

+---------+-------------------------------------------------+-----------------+
| Name    | Format                                          | Properties      |
+=========+=================================================+=================+
| MAC     | 12:34:56:78:90:ab                               |                 |
+---------+-------------------------------------------------+-----------------+
| MAC_64  | 12:34:56:78:90:ac:bd:ef                         |                 |
+---------+-------------------------------------------------+-----------------+
| GUID    | 12345678-90ab-cdef-1234-567890abcdef            |                 |
+---------+-------------------------------------------------+-----------------+
| EUI_48  | 12-34-56-78-90-ab                               | oui, oui36, cid |
+---------+-------------------------------------------------+-----------------+
| EUI_64  | 12-34-56-78-90-ab-cd-ef                         | oui, oui36, cid |
+---------+-------------------------------------------------+-----------------+
| WWN     | 12:34:56:78:90:ac:bd:ef                         | naa, oui        |
+---------+-------------------------------------------------+-----------------+
| WWNx    | 12:34:56:78:90:ac:bd:ef:12:34:56:78:90:ac:bd:ef | naa, oui        |
+---------+-------------------------------------------------+-----------------+
| IB_LID  | 0x12ab                                          |                 |
+---------+-------------------------------------------------+-----------------+
| IB_GUID | 1234:5678:90ab:cdef                             |                 |
+---------+-------------------------------------------------+-----------------+
| IB_GID  | 1234:5678:90ab:cdef:1432:5678:90ab:cdef         | prefix, guid    |
+---------+-------------------------------------------------+-----------------+


Common Classmethods/Methods/Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**All classes inheriting from MAC will have the following methods, classmethos, and properties.**

+--------------------------+-------------+---------+--------------------------------------------------------------+
| Name                     | Type        | Returns | Description                                                  |
+==========================+=============+=========+==============================================================+
| verify(address)          | classmethod | bool    | Verify that address conforms to formatting defined by class. |
+--------------------------+-------------+---------+--------------------------------------------------------------+
| | format(delimiter=None, | method      | str     | Format address with given formatting options.                |
| |        group=None,     |             |         |                                                              |
| |        upper=None)     |             |         | If an option is not specified,                               |
|                          |             |         | the option defined by the class will be used.                |
+--------------------------+-------------+---------+--------------------------------------------------------------+
| int                      | property    | int     | Integer representation of address.                           |
+--------------------------+-------------+---------+--------------------------------------------------------------+
| hex                      | property    | str     | Hexadecimal representation of address.                       |
+--------------------------+-------------+---------+--------------------------------------------------------------+
| binary                   | property    | str     | Padded binary representation of each hex digit in address.   |
+--------------------------+-------------+---------+--------------------------------------------------------------+


EUI Properties
~~~~~~~~~~~~~~

+-------+---------+--------------------------------------------+
| Name  | Returns | Description                                |
+=======+=========+============================================+
| oui   | OIU     | 24-bit Organizationally Unique Identifier. |
+-------+---------+--------------------------------------------+
| cid   | CID     | 24-bit Company ID.                         |
+-------+---------+--------------------------------------------+
| oui36 | OUI36   | 36-bit Organizationally Unique Identifier. |
+-------+---------+--------------------------------------------+


WWN Properties
~~~~~~~~~~~~~~

+------+---------+--------------------------------------------+
| Name | Returns | Description                                |
+======+=========+============================================+
| naa  | str     | Network Address Authority.                 |
+------+---------+--------------------------------------------+
| oui  | OUI     | 24-bit Organizationally Unique Identifier. |
+------+---------+--------------------------------------------+


IB_GID Properties
~~~~~~~~~~~~~~~~~

+--------+---------------+--------------------------+
| Name   | Returns       | Description              |
+========+===============+==========================+
| prefix | IB_GID_prefix | 64-bit IB_GID_prefix.    |
+--------+---------------+--------------------------+
| guid   | IB_GUID       | Embedded 64-bit IB_GUID. |
+--------+---------------+--------------------------+


Factory Functions
-----------------

new_hwaddress_class(name, length=48, delimiter=':', grouping=2, upper=False)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> from hwaddress import new_hwaddress_class

get_address_factory(\*args)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Return a hwaddress object from objs tuple
depending on the address passed as an argument.

.. code:: python

    >>> from hwaddress import get_address_factory, EUI_48, EUI_64
    >>>
    >>> hw_address = get_address_factory()
    >>>
    >>> hw_address('12:34:56:78:90:ab')
    MAC(12:34:56:78:90:ab)
    >>> hw_address('12:34:56:78:90:ab:cd:ef')
    MAC_64(12:34:56:78:90:ab:cd:ef)
    >>>
    >>> eui_address = get_address_factory(EUI_48, EUI_64)


get_verifier(\*args)
~~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> from hwaddress import MAC, EUI_48, get_verifier
    >>>
    >>> class MyMAC(MAC):
    ...     _len_ = 48
    ...     _del_ = '.'
    ...     _grp_ = 4
    ...
    >>>
    >>> my_verifier = get_verifier(MAC, EUI_48, MyMAC)
    >>>
    >>> my_verifier('12:34:56:78:90:ab')
    True
    >>> my_verifier('12-34-56-78-90-ab')
    True
    >>> my_verifier('1234.5678.90ab')
    True
    >>> my_verifier('12.34.56.78.90.ab')
    False
    >>> my_verifier('1234-5678-90ab')
    False

