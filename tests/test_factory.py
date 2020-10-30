"""unittests for hwaddresses factory functions."""

from functools import partial
from random import choice, choices, getrandbits, randint
from string import hexdigits
import unittest
from hwaddress import MAC, MAC_64, GUID, EUI_48, EUI_64, WWN, WWNx, \
                      IB_LID, IB_GUID, IB_GID, hw_address

# create factories for eui, wwn, and ib
eui_address = partial(hw_address, objs=(EUI_48, EUI_64))
wwn_address = partial(hw_address, objs=(WWN, WWNx))
ib_address = partial(hw_address, objs=(IB_LID, IB_GUID, IB_GID))

# Max int that can be held in bit length
B16 = 65535
B48 = 281474976710655
B64 = 18446744073709551615
B128 = 340282366920938463463374607431768211455

# Define 'floor' and 'ceiling' int values for NAA 1, 2, 5, and 6
N12f = 1152921504606846976
N12c = 3458764513820540927
N5f = 5764607523034234880
N5c = 6917529027641081855
N6f = 127605887595351923798765477786913079296
N6c = 148873535527910577765226390751398592511


def getrandhex(n):
    """Generate hex string representing bit length defined by n."""
    n = int(n / 4)
    return ''.join(choices(hexdigits, k=n))


class GenericFactory(unittest.TestCase):
    """Test default factory function."""

    def test_hw_rand_hex(self):
        """Test given hex strings returns correct MAC/GUID object."""
        self.assertTrue(isinstance(hw_address(getrandhex(48)), MAC))
        self.assertTrue(isinstance(hw_address(getrandhex(64)), MAC_64))
        self.assertTrue(isinstance(hw_address(getrandhex(128)), GUID))

    def test_hw_rand_int(self):
        """Test given int returns correct MAC/GUID object."""
        self.assertTrue(isinstance(hw_address(getrandbits(48)), MAC))
        self.assertTrue(isinstance(hw_address(getrandbits(64)), MAC_64))
        self.assertTrue(isinstance(hw_address(getrandbits(128)), GUID))

    def test_hw_limits(self):
        """Test ints near bit length limit returns correct MAC/GUID object."""
        self.assertTrue(isinstance(hw_address(0), MAC))
        self.assertTrue(isinstance(hw_address(B48), MAC))
        self.assertTrue(isinstance(hw_address(B48 + 1), MAC_64))
        self.assertTrue(isinstance(hw_address(B64), MAC_64))
        self.assertTrue(isinstance(hw_address(B64 + 1), GUID))
        self.assertTrue(isinstance(hw_address(B128), GUID))


class EuiFactory(unittest.TestCase):
    """Test eui_address factory function."""

    def test_eui_rand_hex(self):
        """Test given hex strings returns correct EUI object."""
        self.assertTrue(isinstance(eui_address(getrandhex(48)), EUI_48))
        self.assertTrue(isinstance(eui_address(getrandhex(64)), EUI_64))

    def test_eui_rand_int(self):
        """Test given int returns correct EUI object."""
        self.assertTrue(isinstance(eui_address(getrandbits(48)), EUI_48))
        self.assertTrue(isinstance(eui_address(getrandbits(64)), EUI_64))

    def test_eui_limits(self):
        """Test ints near bit length limit returns correct EUI object."""
        self.assertTrue(isinstance(eui_address(0), EUI_48))
        self.assertTrue(isinstance(eui_address(B48), EUI_48))
        self.assertTrue(isinstance(eui_address(B48 + 1), EUI_64))
        self.assertTrue(isinstance(eui_address(B64), EUI_64))


class WwnFactory(unittest.TestCase):
    """Test wwn_address factory function."""

    def test_wwn_rand_hex(self):
        """Test given hex strings returns correct WWN object."""
        wwnhex = choice(('1', '2', '5')) + getrandhex(60)
        wwnxhex = '6' + getrandhex(124)
        self.assertTrue(isinstance(wwn_address(wwnhex), WWN))
        self.assertTrue(isinstance(wwn_address(wwnxhex), WWNx))

    def test_wwn_rand_int(self):
        """Test given int returns correct WWN object."""
        self.assertTrue(isinstance(wwn_address(randint(N12f, N12c)), WWN))
        self.assertTrue(isinstance(wwn_address(randint(N5f, N5c)), WWN))
        self.assertTrue(isinstance(wwn_address(randint(N6f, N6c)), WWNx))

    def test_wwn_limits(self):
        """Test ints near bit length limit returns correct WWN object."""
        self.assertTrue(isinstance(wwn_address(N12f), WWN))
        self.assertTrue(isinstance(wwn_address(N12c), WWN))
        self.assertTrue(isinstance(wwn_address(N5f), WWN))
        self.assertTrue(isinstance(wwn_address(N5c), WWN))
        self.assertTrue(isinstance(wwn_address(N6f), WWNx))
        self.assertTrue(isinstance(wwn_address(N6c), WWNx))


class IbFactory(unittest.TestCase):
    """Test ib_address factory function."""

    def test_ib_rand_hex(self):
        """Test given hex strings returns correct IB object."""
        self.assertTrue(isinstance(ib_address(getrandhex(16)), IB_LID))
        self.assertTrue(isinstance(ib_address(getrandhex(64)), IB_GUID))
        self.assertTrue(isinstance(ib_address(getrandhex(128)), IB_GID))

    def test_ib_rand_int(self):
        """Test given int returns correct IB object."""
        self.assertTrue(isinstance(ib_address(getrandbits(16)), IB_LID))
        self.assertTrue(isinstance(ib_address(getrandbits(64)), IB_GUID))
        self.assertTrue(isinstance(ib_address(getrandbits(128)), IB_GID))

    def test_ib_limits(self):
        """Test ints near bit length limit returns correct IB object."""
        self.assertTrue(isinstance(ib_address(0), IB_LID))
        self.assertTrue(isinstance(ib_address(B16), IB_LID))
        self.assertTrue(isinstance(ib_address(B16 + 1), IB_GUID))
        self.assertTrue(isinstance(ib_address(B64), IB_GUID))
        self.assertTrue(isinstance(ib_address(B64 + 1), IB_GID))
        self.assertTrue(isinstance(ib_address(B128), IB_GID))
