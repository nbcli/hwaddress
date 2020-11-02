"""unittests for hwaddresses factory functions."""

from random import choice, choices
from string import hexdigits
import unittest
from hwaddress import MAC, MAC_64, GUID, EUI_48, EUI_64, WWN, WWNx, \
                      IB_LID, IB_GUID, IB_GID, get_address_factory

# create factories for eui, wwn, and ib
hw_address = get_address_factory()
eui_address = get_address_factory(EUI_48, EUI_64)
wwn_address = get_address_factory(WWN, WWNx)
ib_address = get_address_factory(IB_LID, IB_GUID, IB_GID)


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


class EuiFactory(unittest.TestCase):
    """Test eui_address factory function."""

    def test_eui_rand_hex(self):
        """Test given hex strings returns correct EUI object."""
        self.assertTrue(isinstance(eui_address(getrandhex(48)), EUI_48))
        self.assertTrue(isinstance(eui_address(getrandhex(64)), EUI_64))


class WwnFactory(unittest.TestCase):
    """Test wwn_address factory function."""

    def test_wwn_rand_hex(self):
        """Test given hex strings returns correct WWN object."""
        wwnhex = choice(('1', '2', '5')) + getrandhex(60)
        wwnxhex = '6' + getrandhex(124)
        self.assertTrue(isinstance(wwn_address(wwnhex), WWN))
        self.assertTrue(isinstance(wwn_address(wwnxhex), WWNx))


class IbFactory(unittest.TestCase):
    """Test ib_address factory function."""

    def test_ib_rand_hex(self):
        """Test given hex strings returns correct IB object."""
        self.assertTrue(isinstance(ib_address(getrandhex(16)), IB_LID))
        self.assertTrue(isinstance(ib_address(getrandhex(64)), IB_GUID))
        self.assertTrue(isinstance(ib_address(getrandhex(128)), IB_GID))
