"""Lightweight EUI-48, EUI-64 based hardware (MAC) address library."""


class MAC():
    """Base class for Hardware Addresses.

    Represent a single Hardware Address.
    """

    _del_opts_ = ('-', ':', '.', ' ', '')

    _len_ = 48      # length of address in bits. multiple of 4
    _grp_ = 2       # default group size of hex digits, (1, 2, 3, 4)
    _del_ = ':'     # default delimiter, ('-', ':', '.', ' ', '')
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
        if (not isinstance(self._len_, int)) or (self._len_ % 4 != 0):
            raise AttributeError(f'length must be an int divisible by 4')

        # check that self._grp_ is in (1, 2, 4)
        if not isinstance(self._grp_, (int, tuple)):
            raise AttributeError(f'group must be an int or tuple.')

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
            
        self._restrict_()

    def _proc_string_(self, string):

        hws = string.lower()

        stripchar = list(self._del_opts_) + ["0x"]
        for char in stripchar:
            hws = hws.replace(char, "")

        if len(hws) != int(self._len_ / 4):
            raise ValueError


        try:
            int(hws, 16)
        except ValueError:
            raise ValueError(f"'{string}' contains non hexadecimal digits.")

        self._digits_ = tuple(hws)

    def _restrict_(self):

        pass

    def __iter__(self):

        return self._digits_.__iter__()

    def __getitem__(self, item):

        return self._digits_[item]

    def __len__(self):

        return len(self._digits_)

    def __lt__(self, other):

        return self.int < other.int

    def __eq__(self, other):

        return self.__class__ == other.__class__ and self.int == other.int

    def __hash__(self):

        return hash(f'{self.__class__}{self._digits_}')

    def __repr__(self):

        return f'{self.__class__.__name__}({str(self)})'

    def __str__(self):

        grp = self._grp_

        if isinstance(grp, int):
            parts = [''.join(self[i:i+grp]) for i in range(0, len(self), grp)]
        elif isinstance(grp, tuple):
            parts = []
            s = 0
            for i in grp:
                parts.append(''.join(self[s:s+i]))
                s += i

        string = self._del_.join(parts) 

        if self._upper_:
            string = string.upper()

        if self._del_ == '':
            return f'0x{string}'

        return string

    @property
    def int(self):
        """Integer representation of address."""
        return int(self.hex, 16)

    @property
    def hex(self):
        """Hexadecimal representation of address."""
        return f'0x{"".join(self)}'

    @property
    def bin(self):
        """Binary representation of address."""
        return bin(self.int)

    @property
    def binary(self):
        """Padded binary representation of each hex digit in address.

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


class MAC_64(MAC):

    _len_ = 64


class GUID(MAC):

    _len_ = 128
    _grp_ = (8, 4, 4, 4, 12)
    _del_ = '-'


class EUI_Mixin():

    @property
    def oui(self):

        obj = type('OUI', (MAC,), dict(_len_=24))
        return obj(''.join(self[:6]))

    @property
    def cid(self):

        obj = type('CID', (MAC,), dict(_len_=24))
        return obj(''.join(self[:6]))

    @property
    def oui36(self):

        obj = type('OUI36', (MAC,), dict(_len_=36))
        return obj(''.join(self[:9]))


class EUI_48(MAC, EUI_Mixin):

    _del_ = '-'


class EUI_64(MAC, EUI_Mixin):

    _len_ = 64
    _del_ = '-'


class WWN_Mixin():

    @property
    def naa(self):

        return self[0]

    @property
    def oui(self):

        obj = type('OUI', (MAC,), dict(_len_=24))

        if self.naa in ('1', '2'):
            return obj(''.join(self[4:10]))
        elif self.naa in ('5', '6'):
            return obj(''.join(self[1:7]))
        else:
            raise RuntimeError('WWN(x) NAA must be 1, 2, 5, or 6')


class WWN(MAC, WWN_Mixin):

    _len_ = 64

    def _restrict_(self):

        if self[0] not in ('1', '2', '5'):
            raise ValueError('First hex digit for WWN must be 1, 2, or 5')


class WWNx(MAC, WWN_Mixin):

    _len_ = 128

    def _restrict_(self):

        if self[0] != '6':
            raise ValueError('First hex digit for WWNx must be 6')


class IB_LID(MAC):

    _len_ = 16
    _del_ = ''
    _grp_ = 4


class IB_GUID(EUI_64):

    _len_ = 64
    _del_ = ':'
    _grp_ = 4


class IB_GID(MAC):

    _len_ = 128
    _del_ = ':'
    _grp_ = 4

    @property
    def prefix(self):

        prop = dict(_len_=64,
                    _del_=':',
                    _grp_=4)

        obj = type('IB_GID_prefix', (MAC,), prop)
        return obj(''.join(self[:16]))

    @property
    def guid(self):

        return IB_GUID(''.join(self[16:]))


def hw_address(address, objs=(MAC, MAC_64, GUID)):

    for obj in objs:
        try:
            return obj(address)
        except (TypeError, ValueError):
            pass

    raise ValueError(f'{address} does not seem to be any of {objs}.')
