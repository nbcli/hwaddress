=========
hwaddress
=========

A lightweight EUI-48, EUI-64 based hardware address library.

.. contents::
    :local:


Factory Functions
-----------------

hwaddress.eui_address(address)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Return an EUI_48 or EUI_64 object depending on the address passed as an argument.

.. code:: python

    >>> eui_address('12:34:56:78:90:ab')
    EUI_48(12-34-56-78-90-ab)
    >>> eui_address(20015998341291)
    EUI_48(12-34-56-78-90-ab)
    >>> eui_address('12:34:56:78:90:ab:cd:ef')
    EUI_64(12-34-56-78-90-ab-cd-ef)
    >>> eui_address(1311768467294899695)
    EUI_64(12-34-56-78-90-ab-cd-ef)


hwaddress.wwn_address(address)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Return a WWN or WWNx object depending on the address passed as an argument.

.. code:: python

    >>> wwn_address('20:12:34:56:78:90:ab:cd')
    WWN(20:12:34:56:78:90:ab:cd)
    >>> wwn_address(2310967104789064653)
    WWN(20:12:34:56:78:90:ab:cd)
    >>> wwn_address('60:12:34:56:78:90:ab:cd:12:34:56:78:90:ab:cd:ef')
    WWNx(60-12-34-56-78-90-ab-cd-12-34-56-78-90-ab-cd-ef)
    >>> wwn_address(127700410475040014613822894157901581807)
    WWNx(60-12-34-56-78-90-ab-cd-12-34-56-78-90-ab-cd-ef)


hwaddress.ib_address(address)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Return an IB_LID, IB_GUID, or IB_GID object depending on the address passed as an argument.

.. code:: python

    >>> ib_address('00af')
    IB_LID(0x00af)
    >>> ib_address(175)
    IB_LID(0x00af)
    >>> ib_address('12:34:56:78:90:ab:cd:ef')
    IB_GUID(1234:5678:90ab:cdef)
    >>> ib_address(1311768467294899695)
    IB_GUID(1234:5678:90ab:cdef)
    >>> ib_address('12:34:56:78:90:ab:cd:ef:12:34:56:78:90:ab:cd:ef')
    IB_GID(1234:5678:90ab:cdef:1234:5678:90ab:cdef)
    >>> ib_address(24197857200151252728969465429440056815)
    IB_GID(1234:5678:90ab:cdef:1234:5678:90ab:cdef)


Base Hardware Address object
----------------------------

hwaddress.core.Base_HWA
~~~~~~~~~~~~~~~~~~~~~~~

Methods
+++++++

* format(delimiter=None, group=None, upper=None)

    Format address with given formatting options.

    If an option is not specified,
    the option defined by the class will be used

    Args:
        delimiter (str): character separating hex digits.
        group (int): how many hex digits in each group.
        upper (bool): True for uppercase, False for lowercase.
    

Properties
+++++++++

* int (Integer representation of address.)
* hex (Hexadecimal representation of address.)
* bin (Binary representation of address.)
* binary (Padded binary representation of each hex digit in address.)


hwaddress.core.EUI_Mixin
~~~~~~~~~~~~~~~~~~~~~~~~


hwaddress.core.WWN_Mixin
~~~~~~~~~~~~~~~~~~~~~~~~

