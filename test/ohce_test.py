import os
import unittest

from expressions import BIEN_DIT
from vérificationPalindrome import VérificationPalindrome


class PalindromeTest(unittest.TestCase):
    def test_miroir(self):
        """QUAND on saisit une chaîne ALORS celle-ci est renvoyée en miroir"""
        for chaîne in ["test", "epsi"]:
            with self.subTest(chaîne):
                résultat = VérificationPalindrome.vérifier(chaîne)

                attendu = chaîne[::-1]
                self.assertEqual(attendu, résultat)

    def test_palindrome(self):
        """QUAND on saisit un palindrome ALORS celui-ci est renvoyé et Bien dit ! est envoyé ensuite"""
        palindrome = "radar"
        résultat = VérificationPalindrome.vérifier(palindrome)

        self.assertEqual(palindrome + os.linesep + BIEN_DIT, résultat)


if __name__ == '__main__':
    unittest.main()
