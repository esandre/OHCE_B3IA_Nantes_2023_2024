import unittest

from vérificationPalindrome import VérificationPalindrome


class PalindromeTest(unittest.TestCase):
    def test_miroir(self):
        """QUAND on saisit une chaîne ALORS celle-ci est renvoyée en miroir"""
        for chaîne in ["test", "epsi"]:
            with self.subTest(chaîne):
                résultat = VérificationPalindrome.vérifier(chaîne)

                attendu = chaîne[::-1]
                self.assertEqual(attendu, résultat)


if __name__ == '__main__':
    unittest.main()
