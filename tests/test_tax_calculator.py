import os
import sys
import unittest

sys.path.insert(1, os.path.join(
    os.path.dirname(os.path.realpath(__file__)), os.pardir))

from tax_calculator import calc_tax  # noqa: E402


class 計算單人稅額(unittest.TestCase):
    """
    所得淨額 = 所得總額 - 免稅額 - 標準扣除額 - 特別扣除額
    """

    def setUp(self):
        免稅額 = 88000
        標準扣除額 = 90000
        特別扣除額 = 128000

        self.總免稅額 = 免稅額 + 標準扣除額 + 特別扣除額

    def test_所得總額不高於免稅額加各項扣除額時為免稅(self):
        income = self.總免稅額

        tax = calc_tax(income)

        self.assertEqual(tax, 0)

    def test_所得淨額為_1_課稅級距為_百分之五(self):
        income = self.總免稅額 + 1

        tax = calc_tax(income)

        self.assertEqual(tax, 0)

    def test_所得淨額為_540000_課稅級距為百分之五(self):
        income = self.總免稅額 + 540000

        tax = calc_tax(income)

        self.assertEqual(tax, 27000)

    def test_所得淨額為_540001_則超過_540000_的部份課稅級距為百分之十二(self):
        income = self.總免稅額 + 540001

        tax = calc_tax(income)

        self.assertEqual(tax, 27000)

    def test_所得淨額為_1210000_則超過_540000_的部份課稅級距為百分之十二(self):
        income = self.總免稅額 + 1210000

        tax = calc_tax(income)

        self.assertEqual(tax, 107400)

    def test_所得淨額為_1210001_則超過_1210000_的部份課稅級距為百分之二十(self):
        income = self.總免稅額 + 1210001

        tax = calc_tax(income)

        self.assertEqual(tax, 107400)

    def test_所得淨額為_2420000_則超過_1210000_的部份課稅級距為百分之二十(self):
        income = self.總免稅額 + 2420000

        tax = calc_tax(income)

        self.assertEqual(tax, 349400)

    def test_所得淨額為_2420001_則超過_2420000_的部份課稅級距為百分之三十(self):
        income = self.總免稅額 + 2420001

        tax = calc_tax(income)

        self.assertEqual(tax, 349400)

    def test_所得淨額為_4530000_則超過_2420000_的部份課稅級距為百分之三十(self):
        income = self.總免稅額 + 4530000

        tax = calc_tax(income)

        self.assertEqual(tax, 982400)

    def test_所得淨額為_4530001_則超過_4530000_的部份課稅級距為百分之四十(self):
        income = self.總免稅額 + 4530001

        tax = calc_tax(income)

        self.assertEqual(tax, 982400)

    def test_所得淨額為_10310000_則超過_4530000_的部份課稅級距為百分之四十(self):
        income = self.總免稅額 + 10310000

        tax = calc_tax(income)

        self.assertEqual(tax, 3294400)

    def test_所得淨額為_10310001_則超過_10310000_的部份課稅級距為百分之四十五(self):
        income = self.總免稅額 + 10310001

        tax = calc_tax(income)

        self.assertEqual(tax, 3294400)
