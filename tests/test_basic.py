# -*- coding: utf-8 -*-

from .context import scripts

import unittest

from scripts import get_bangs, get_dt

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True

    def test_getBang(self):
        self.assertEquals(get_bangs(), 'There can be only one bangs...', 'Should get the bangs')

    def test_shouldGetDT(self):
        self.assertNotEquals(get_dt(), 'Slime is not a dt', 'It should not get the dt')


if __name__ == '__main__':
    unittest.main()

