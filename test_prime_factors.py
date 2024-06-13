from unittest import TestCase

from prime_factors import PrimeFactor


class TestPrimeFactor(TestCase):
    def test_prime_factor_of_1(self):
        pf = PrimeFactor()
        self.assertEqual([], pf.of(1))

    def test_prime_factor_of_2(self):
        pf = PrimeFactor()
        self.assertEqual([2], pf.of(2))

