import unittest
import lab19.Evtushenko.palindrome as pal


class TestPalindrome(unittest.TestCase):
    def test_from_site_1(self):
        s = 'abca'
        res = pal.search(s)
        exp = 'aba'
        self.assertEqual(res, exp)

    def test_from_site_2(self):
        s = 'babcad'
        res = pal.search(s)
        exp = 'bab'
        self.assertEqual(res, exp)

    def test_empty(self):
        s = ''
        res = pal.search(s)
        exp = ''
        self.assertEqual(res, exp)

    def test_one_char(self):
        s = 'a'
        res = pal.search(s)
        exp = 'a'
        self.assertEqual(res, exp)

    def test_repeated_char_even(self):
        s = 'aaaaaaaa'
        res = pal.search(s)
        exp = 'aaaaaaaa'
        self.assertEqual(res, exp)

    def test_repeated_char_odd(self):
        s = 'aaaaaaa'
        res = pal.search(s)
        exp = 'aaaaaaa'
        self.assertEqual(res, exp)

    def test_palindrome(self):
        s = 'madam'
        res = pal.search(s)
        exp = 'madam'
        self.assertEqual(res, exp)


