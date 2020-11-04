"""unittest to test that expected errors get raised."""

import unittest
from hwaddress import MAC, new_hwaddress_class, \
                      get_verifier, get_address_factory


class RaiseError(unittest.TestCase):

    class AttrErr(MAC):

        _len_ = 'Potato'


    def test_attr_error(self):

        modellist=[('_', 47, '.', 2, False),
                   ('_', 48, 3, 2, False),
                   ('_', 48, '.', '2', False),
                   ('_', 48, '.', 2, 'Potato')]

        for model in modellist:
            self.assertRaises(AttributeError, new_hwaddress_class, *model)

        self.assertRaises(AttributeError, self.AttrErr, '12:34:56:78:90:ab')

    def test_type_error(self):

        strerrlist = [1, True, 4.4, {}, (), [], MAC]
        interrlist = strerrlist[2:] + ['str']
        macerrlist = strerrlist[:-1]

        for ei in strerrlist:
            self.assertRaises(TypeError, MAC, ei)

        for ei in strerrlist:
            self.assertRaises(TypeError, MAC.verify, ei)

        for ei in interrlist:
            self.assertRaises(TypeError, new_hwaddress_class, '_', length=ei)

        for ei in macerrlist:
            self.assertRaises(TypeError, get_verifier, ei)

        for ei in macerrlist:
            self.assertRaises(TypeError, get_address_factory, ei)

    def test_value_error(self):

        self.assertRaises(ValueError, get_address_factory(), 'abcd')
        self.assertRaises(ValueError, MAC, '12:34:56:78:90:ag')
