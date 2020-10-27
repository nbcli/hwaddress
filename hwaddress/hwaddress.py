"""Lightweight EUI-48, EUI-64 based hardware address library."""


class _HW_Opts_:
    """Define available options for Base_HWA class and sub-classes."""

    grp_opts = range(1, 5)
    del_opts = ('-', ':', '.', ' ', '')


class Base_HWA():
    """Base class for Hardware Addresses.

    Represent a single Hardware Address.
    """

    _len_ = 48      # length of address in bits. multiple of 4
    _grp_ = 2       # default group size of hex digits, (1, 2, 3, 4)
    _del_ = '-'     # default delimiter, ('-', ':', '.', ' ', '')
    _upper_ = False

    def __init__(self, address):
        """Initialize address object.

        Args:
            address: A string or integer representing the Hardware Address

                Integers must fit into the bit length defined by cls._len_

                Address string does not have to conform to any format.
                '-', ':', '.', ' ', '', and '0x' will be removed from the
                string. All remaining characters must be hexadecimal digits
                of length cls._len_ / 4

        Raises:
            AttributeError: If private attribute do not conform to restraints.
            TypeError: If address is not str or int type.
            ValueError if address is int and can not fit in self._len_ bits.
        """
        # check that self._len_ is evenly divisible by 4
        if self._len_ % 4 != 0:
            raise AttributeError(f'{self._len_} is not divisible by 4')

        # check that self._grp_ is in (1, 2, 4)
        grp_opts = _HW_Opts_.grp_opts
        if self._grp_ not in grp_opts:
            raise AttributeError(f'group must be in {grp_opts}')

        # check that self._del_ is in ('-', ':', '.', ' ', '')
        del_opts = _HW_Opts_.del_opts
        if self._del_ not in del_opts:
            raise AttributeError(f'{self._del_} not in {del_opts}')

        # check that self._upper_ is True or False
        if self._upper_ not in (True, False):
            raise AttributeError('_upper_ must be True or False')

        if isinstance(address, int):
            if address.bit_length() > self._len_:
                raise ValueError(f'{address} can not fit in {self._len_} bits')
            hexstr = hex(address)[2:]
            self._proc_string_(hexstr.zfill(int(self._len_ / 4)))
        elif isinstance(address, str):
            self._proc_string_(address)
        else:
            raise TypeError("'address' must be an integer or string.")

    def _proc_string_(self, string):

        hws = string.lower()

        stripchar = list(_HW_Opts_.del_opts) + ["0x"]
        for char in stripchar:
            hws = hws.replace(char, "")

        if len(hws) != int(self._len_ / 4):
            raise ValueError

        if self._upper_:
            hws = hws.upper()

        try:
            int(hws, 16)
        except ValueError:
            raise ValueError(f"'{string}' contains non hexadecimal digits.")

        self._digits_ = tuple(hws)

    def __iter__(self):

        return self._digits_.__iter__()

    def __getitem__(self, item):

        return self._digits_[item]

    def __len__(self):

        return len(self._digits_)

    def __lt__(self, other):

        return self.int < other.int

    def __repr__(self):

        return f'{self.__class__.__name__}({str(self)})'

    def __str__(self):

        if self._del_ == '':
            return self.hex

        grp = self._grp_
        cnt = len(self)
        parts = [''.join(self[i:i+grp]) for i in range(0, cnt, grp)]

        return self._del_.join(parts)

    @property
    def int(self):
        """Integer representation of this address."""
        return int(self.hex, 16)

    @property
    def hex(self):
        """Hexadecimal representation of this address."""
        return f'0x{"".join(self)}'

    @property
    def bin(self):
        """Binary representation of this address."""
        return bin(self.int)

    @property
    def binary(self):
        """Binary representation of each hex digit in this address.

        Binary groups are padded with '0's to be 4 bits long,
        and are separated with a space to improve readability.
        """
        return ' '.join([bin(int(d, 16))[2:].zfill(4) for d in self])

    def format(self, delimiter=None, group=None, upper=None):
        """Format address with given formatting options.

        If an option is not specified,
        the option defined by the class will be used

        Args:
            delimiter (str): character separating hex digits.
            group (int): how many hex digits in each group.
            upper (bool): True for uppercase, False for lowercase.
        """
        if delimiter is None:
            delimiter = self._del_

        if upper not in (True, False):
            upper = self._upper_

        prop = dict(_del_=delimiter,
                    _grp_=group or self._grp_,
                    _upper_=upper)

        if delimiter == '':
            prop['_del_'] = delimiter

        obj = type('_', (self.__class__,), prop)(self.hex)

        return str(obj)


class EUI_Mixin():

    @property
    def oui(self):

        obj = type('OUI', (Base_HWA,), dict(_len_=24))
        return obj(''.join(self[:6]))

    @property
    def cid(self):

        obj = type('CID', (Base_HWA,), dict(_len_=24))
        return obj(''.join(self[:6]))

    @property
    def oui36(self):

        obj = type('OUI36', (Base_HWA,), dict(_len_=36))
        return obj(''.join(self[:9]))


class EUI_48(Base_HWA, EUI_Mixin):

    _len_ = 48


class EUI_64(Base_HWA, EUI_Mixin):

    _len_ = 64


class WWN_Mixin():

    @property
    def naa(self):

        return self[0]

    @property
    def oui(self):

        obj = type('OUI', (Base_HWA,), dict(_len_=24))

        if self.naa in ('1', '2'):
            return obj(''.join(self[4:10]))
        elif self.naa in ('5', '6'):
            return obj(''.join(self[1:7]))
        else:
            raise RuntimeError('WWN(x) NAA must be 1, 2, 5, or 6')


class WWN(Base_HWA, WWN_Mixin):

    _len_ = 64
    _del_ = ':'

    def __init__(self, address):

        super().__init__(address)
        if self[0] not in ('1', '2', '5'):
            raise ValueError('First hex digit for WWN must be 1, 2, or 5')


class WWNx(Base_HWA, WWN_Mixin):

    _len_ = 128

    def __init__(self, address):

        super().__init__(address)
        if self[0] != '6':
            raise ValueError('First hex digit for WWNx must be 6')


class IB_LID(Base_HWA):

    _len_ = 16
    _del_ = ''
    _grp_ = 4


class IB_GUID(EUI_64):

    _len_ = 64
    _del_ = ':'
    _grp_ = 4


class IB_GID(Base_HWA):

    _len_ = 128
    _del_ = ':'
    _grp_ = 4

    @property
    def prefix(self):

        prop = dict(_len_=64,
                    _del_=':',
                    _grp_=4)

        obj = type('IB_GID_prefix', (Base_HWA,), prop)
        return obj(''.join(self[:16]))

    @property
    def guid(self):

        return IB_GUID(''.join(self[16:]))


def eui_address(address):

    try:
        return EUI_48(address)
    except (TypeError, ValueError):
        pass

    try:
        return EUI_64(address)
    except (TypeError, ValueError):
        pass

    raise ValueError(f'{address} is not a EUI-48 or EUI-64 ID.')


def wwn_address(address):

    try:
        return WWN(address)
    except (TypeError, ValueError):
        pass

    try:
        return WWNx(address)
    except (TypeError, ValueError):
        pass

    raise ValueError(f'{address} is not a WWN ID.')


def ib_address(address):

    try:
        return IB_LID(address)
    except (TypeError, ValueError):
        pass

    try:
        return IB_GUID(address)
    except (TypeError, ValueError):
        pass

    try:
        return IB_GID(address)
    except (TypeError, ValueError):
        pass

    raise ValueError(f'{address} is not an IB LID, GUID, or GID.')
