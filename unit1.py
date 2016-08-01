#!/usr/bin/env python

# unit testing of mastermind1.py

import mastermind1 as ma
import unittest

class TestSequenceFunctions(unittest.TestCase):
    
    def test_combination(self):
        """
        unit testing of class combination

        combinaison == shall be tested with :
    
        1234 == 1234 => (4,0)
        1234 == 4321 => (0,4)
        1234 == 1242 => (2,1)
        1122 == 2111 => (1,2)
        1112 == 2221 => (0,2)
        3130 == 3120 => (3,0)
        """
        self.assertEqual(ma.Combination("1234")==ma.Combination("1234"), (4,0))
        self.assertEqual(ma.Combination("1234")==ma.Combination("4321"), (0,4))
        self.assertEqual(ma.Combination("1234")==ma.Combination("1242"), (2,1))
        self.assertEqual(ma.Combination("1122")==ma.Combination("2111"), (1,2))
        self.assertEqual(ma.Combination("1112")==ma.Combination("2221"), (0,2))
        self.assertEqual(ma.Combination("3130")==ma.Combination("3120"), (3,0))
        
        #combination length test
        with self.assertRaises(AssertionError):
            ma.Combination("A") == ma.Combination("AA")
            ma.Combination("") == ma.Combination("AA")
            ma.Combination("AA") == ma.Combination("")
                          

if __name__ == '__main__':
    unittest.main()
