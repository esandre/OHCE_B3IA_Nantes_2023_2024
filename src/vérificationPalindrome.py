import os

from expressions import BIEN_DIT


class VérificationPalindrome:
    @classmethod
    def vérifier(cls, chaîne):
        miroir = chaîne[::-1]

        if miroir == chaîne:
            return miroir + os.linesep + BIEN_DIT

        return miroir

