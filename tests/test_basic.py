# -*- coding: utf-8 -*-

from .context import scripts

import unittest

from scripts import get_welcome, get_dt, get_rules

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True

    def test_getWelcome(self):
        self.assertEquals(get_welcome(), 'RPSLS - Rock, Paper, Scissor, Lizard, Spock' \
           '\nPlease choose from the list below:', 'Should get the welcome message')

    def test_shouldGetDT(self):
        self.assertNotEquals(get_dt(), 'Not dt', 'It should not get the dt')

    def test_getRules(self):
        self.assertEqual(get_rules(),
            '1. Scissors cuts paper'
            '2. Paper covers rock'
            '3. Rock crushes lizard'
            '4. Lizard poisons Spock'
            '5. Spock smashes scissors'
            '6. Scissors decapitates lizard'
            '7. Lizard eats paper'
            '8. Paper disproves Spock'
            '9. Spock vaporizes rock'
            '10. Rock crushes scissors', 'Should get rules of game')


if __name__ == '__main__':
    unittest.main()

