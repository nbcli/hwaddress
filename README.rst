=========
hwaddress
=========

Lightweight python library for EUI-48, EUI-64 based hardware (MAC) addresses. 

.. contents::
    :local:


Common Methods/Classmethos/Properties
-------------------------------------

**All classes inheriting from MAC will have the following methods, classmethos, and properties.**

+--------------------------+-------------+---------+--------------------------------------------------------------+
| Name                     | Type        | Returns | Description                                                  |
+--------------------------+-------------+---------+--------------------------------------------------------------+
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


Generic Hardware Address Classes
--------------------------------

+--------+------------------------+--------------------------------------+
| MAC    | | bit-length: 48       | ff:ff:ff:ff:ff:ff                    |
|        | | delimiter: ':'       |                                      |
|        | | grouping: 2          |                                      |
+--------+------------------------+--------------------------------------+
| MAC_64 | | bit-length: 64       | ff:ff:ff:ff:ff:ff:ff:ff              |
|        | | delimiter: ':'       |                                      |
|        | | grouping: 2          |                                      |
+--------+------------------------+--------------------------------------+
| GUID   | | bit-length: 128      | ffffffff-ffff-ffff-ffff-ffffffffffff |
|        | | delimiter: '-'       |                                      |
|        | | grouping: 8-4-4-4-12 |                                      |
+--------+------------------------+--------------------------------------+


MAC, MAC_64, GUID Example usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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



EUI Address Classes
-------------------

+--------+------------------------+--------------------------------+
| EUI_48 | | bit-length: 48       | ff-ff-ff-ff-ff-ff              |
|        | | delimiter: '-'       |                                |
|        | | grouping: 2          |                                |
+--------+------------------------+--------------------------------+
| EUI_64 | | bit-length: 64       | ff-ff-ff-ff-ff-ff-ff-ff        |
|        | | delimiter: '-'       |                                |
|        | | grouping: 2          |                                |
+--------+------------------------+--------------------------------+


Common EUI Properties
~~~~~~~~~~~~~~~~~~~~~

+------+----------+---------+----------------------------------------+
| Name | Type     | Returns | Description                            |
+------+----------+---------+----------------------------------------+
| oui  | property | str     | Integer representation of address.     |
+------+----------+---------+----------------------------------------+
| cid  | property | str     | Hexadecimal representation of address. |
+------+----------+---------+----------------------------------------+
| cid  | property | str     | Hexadecimal representation of address. |
+------+----------+---------+----------------------------------------+


EUI_48, EUI_64 Example usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> from hwaddress import EUI_48, EUI_64

.. code:: python

    >>> EUI_48.verify('12:34:56:78:90:ab')
    False
    >>> EUI_48.verify('12-34-56-78-90-ab')
    True
    >>> eui = EUI_48('12:34:56:78:90:ab')
    >>> eui
    EUI_48(12-34-56-78-90-ab)
    >>> str(eui)
    '12-34-56-78-90-ab'
    >>> eui.oui
    OUI(12:34:56)
    >>> eui.cid
    CID(12:34:56)
    >>> eui.oui36
    OUI36(12:34:56:78:9)

.. code:: python

    >>> EUI_64.verify('12-34-56-78-90-ab')
    False
    >>> EUI_64.verify('12-34-56-78-90-ab-cd-ef')
    True
    >>> EUI_64('ab-cd-56-78-90-ab-cd-ef').oui
    OUI(ab:cd:56)


WWN Address Classes
-------------------

+------+-------------------+-------------------------------------------------+
| WWN  | | bit-length: 64  | ff:ff:ff:ff:ff:ff:ff:ff                         |
|      | | delimiter: ':'  |                                                 |
|      | | grouping: 2     |                                                 |
+------+-------------------+-------------------------------------------------+
| WWNx | | bit-length: 128 | ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff |
|      | | delimiter: '-'  |                                                 |
|      | | grouping: 2     |                                                 |
+------+-------------------+-------------------------------------------------+


Common WWN Properties
~~~~~~~~~~~~~~~~~~~~~

+------+----------+---------+----------------------------------------+
| Name | Type     | Returns | Description                            |
+------+----------+---------+----------------------------------------+
| naa  | property | str     | Integer representation of address.     |
+------+----------+---------+----------------------------------------+
| oui  | property | str     | Hexadecimal representation of address. |
+------+----------+---------+----------------------------------------+


WWN, WWNx Example usage
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> from hwaddress import WWN, WWNx


IB Address Classes
------------------

+---------+------------------------+-----------------------------------------+
| IB_LID  | | bit-length: 16       | 0xffff                                  |
|         | | delimiter: ''        |                                         |
|         | | grouping: 4          |                                         |
+---------+------------------------+-----------------------------------------+
| IB_GUID | | bit-length: 64       | ffff:ffff:ffff:ffff                     |
|         | | delimiter: ':'       |                                         |
|         | | grouping: 4          |                                         |
+---------+------------------------+-----------------------------------------+
| IB_GID  | | bit-length: 128      | ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff |
|         | | delimiter: ';'       |                                         |
|         | | grouping: 4          |                                         |
+---------+------------------------+-----------------------------------------+

IB_GID Properties
~~~~~~~~~~~~~~~~~

+--------+----------+---------+----------------------------------------+
| Name   | Type     | Returns | Description                            |
+--------+----------+---------+----------------------------------------+
| prefix | property | str     | Integer representation of address.     |
+--------+----------+---------+----------------------------------------+
| guid   | property | str     | Hexadecimal representation of address. |
+--------+----------+---------+----------------------------------------+


IB_LID, IB_GUID, IB_GID Example usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> from hwaddress import IB_LID, IB_GUID, IB_GID


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

