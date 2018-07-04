import unittest
from syntax import *

class SyntaxTest(unittest.TestCase):

    def test_rätt_molekyl(self):
        """ Testar korrekt syntax"""
        self.assertEqual(kolla_molekyl("H2"),"Formeln är syntaktiskt korrekt")
        self.assertEqual(kolla_molekyl("Mn4"),"Formeln är syntaktiskt korrekt")

    def test_storbokstav(self):
        """ Testar fel med stor bokstav """
        self.assertEqual(kolla_molekyl("cr12"),"Saknar stor bokstav")

    def test_radslut(self):
        """ Testar fel vid siffra """
        self.assertEqual(kolla_molekyl("Cr0"),"För litet tal vid radslut")
        self.assertEqual(kolla_molekyl("Pb1"),"För litet tal vid radslut")

if __name__ == '__main__':
    unittest.main()