from fractions import Fraction
import unittest


class TestFractionsValues(unittest.TestCase):

    def test_fraction_creating(self):

        fract = Fraction(1, 2)
        self.assertEqual(fract.num, 1)
        self.assertEqual(fract.dem, 2)

    def test_zero_dem_returns_error(self):

        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)

    def test_wrong_value_returns_error(self):

        with self.assertRaises(TypeError):
            Fraction('5', '8')

    def test_adding_fractions(self):

        a = Fraction(1, 6)
        b = Fraction(2, 3)
        c = b + a
        d = Fraction(1, 3)

        self.assertEqual((b+d).num, 1)
        self.assertEqual(c.num, 5)
        self.assertEqual(c.dem, 6)

    def test_adding_negative_values(self):

        a = Fraction(1, -6)
        b = Fraction(2, 3)
        c = a + b

        self.assertEqual(c.num, 1)
        self.assertEqual(c.dem, 2)

    def test_sub_fractions(self):

        a = Fraction(1, 6)
        b = Fraction(2, 3)
        c = a - b

        self.assertEqual(c.num, Fraction(-3, 6).num)
        self.assertEqual(c.dem, Fraction(-3, 6).dem)

    def test_fraction_euqals(self):

        a = Fraction(1, 3)
        b = Fraction(1, 6)
        c = Fraction(2, 6)
        d = Fraction(-2, 6)

        self.assertTrue(a == a)
        self.assertTrue(a == c)
        self.assertFalse(a == b)
        self.assertFalse(c == d)

    def test_comparing_fractions(self):

        a = Fraction(1, 3)
        b = Fraction(1, 6)
        c = Fraction(-1, 3)
        d = Fraction(1, -6)

        self.assertTrue(a > b); self.assertTrue(b < a); self.assertTrue(b > c); self.assertTrue(b > d)
        self.assertFalse(c > b)

    def test_string_representation(self):

        a = Fraction(1, 5)
        b = Fraction(3, 9)

        self.assertEqual(a.__str__(), "1/5")
        self.assertEqual(b.__str__(), '1/3')