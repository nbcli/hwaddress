=========
hwaddress
=========

Lightweight python library for EUI-48, EUI-64 based hardware (MAC) addresses. 

.. contents::
    :local:


Factory Functions
-----------------

hwaddress.hw_address(address)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Return an EUI_48 or EUI_64 object depending
on the address passed as an argument.

.. code:: python

    >>> eui_address('12:34:56:78:90:ab')
    EUI_48(12-34-56-78-90-ab)
    >>> eui_address(20015998341291)
    EUI_48(12-34-56-78-90-ab)
    >>> eui_address('12:34:56:78:90:ab:cd:ef')
    EUI_64(12-34-56-78-90-ab-cd-ef)
    >>> eui_address(1311768467294899695)
    EUI_64(12-34-56-78-90-ab-cd-ef)


Base Hardware Address objects
-----------------------------33333333333

hwaddress.MAC(address)
~~~~~~~~~~~~~~~~~~~~~~

::

    bit-length: 48
    delimiter: ':'
    grouping: 2

.. code:: python 

    >>> mac = MAC('12:34:56:78:90:ab')
    >>> mac
    mac(12:34:56:78:90:ab)
    >>> str(mac)
    '12:34:56:78:90:ab'

Methods
+++++++

* format(delimiter=None, group=None, upper=None)

    ::

        Format address with given formatting options.

        If an option is not specified,
        the option defined by the class will be used

        Args:
            delimiter (str): character separating hex digits.
            group (int): how many hex digits in each group.
            upper (bool): True for uppercase, False for lowercase.

        Returns: str

    .. code:: python

        >>> mac.format('-')
        '12-34-56-78-90-ab'
        >>> mac.format('.', 4, True)
        '1234.5678.90AB'


Properties
++++++++++

* int

    ::

        Integer representation of address.

        Returns: int

    .. code:: python

        >>> mac.int
        20015998341291

* hex

    ::

        Hexadecimal representation of address.

        Returns: str

    .. code:: python

        >>> mac.hex
        '0x1234567890ab'

* bin

    ::

        Binary representation of address.

        Returns: str

    .. code:: python

        >>> mac.bin
        '0b100100011010001010110011110001001000010101011'

* binary

    ::

        Padded binary representation of each hex digit in address.

        Returns: str

    .. code:: python

        >>> mac.binary
        '0001 0010 0011 0100 0101 0110 0111 1000 1001 0000 1010 1011'


EUI Address objects
-------------------

hwaddress.core.EUI_Mixin
~~~~~~~~~~~~~~~~~~~~~~~~

Properties
++++++++++

* oui
* cid
* oui36

hwaddress.EUI_48(address)
~~~~~~~~~~~~~~~~

Inherits from: MAC, EUI_Mixin

::

    bit-length: 48
    delimiter: '-'
    grouping: 2

hwaddress.EUI_64(address)
~~~~~~~~~~~~~~~~

Inherits from: MAC, EUI_Mixin

::

    bit-length: 64
    delimiter: '-'
    grouping: 2


WWN Address objects
-------------------

hwaddress.core.WWN_Mixin
~~~~~~~~~~~~~~~~~~~~~~~~

Properties
++++++++++

* naa
* oui

hwaddress.WWN(address)
~~~~~~~~~~~~~

Inherits from: MAC, WWN_Mixin

::

    bit-length: 64
    delimiter: ':'
    grouping: 2

hwaddress.WWNx(address)
~~~~~~~~~~~~~~

Inherits from: MAC, WWN_Mixin

::

    bit-length: 128
    delimiter: ':'
    grouping: 2


IB Address objects
-------------------

hwaddress.IB_LID(address)
~~~~~~~~~~~~~~~~

Inherits from: MAC

::

    bit-length: 16
    delimiter: ''
    grouping: 4

hwaddress.IB_GUID(address)
~~~~~~~~~~~~~~~~~

Inherits from: EUI_64

::

    bit-length: 64
    delimiter: ':'
    grouping: 4

hwaddress.IB_GID(address)
~~~~~~~~~~~~~~~~

Inherits from: MAC

::

    bit-length: 128
    delimiter: ':'
    grouping: 4

Properties
++++++++++

* prefix
* guid


