import unittest
import damerau_levenshtien


class TestDamerau(unittest.TestCase):
    def test_deletion(self):
        res = damerau_levenshtien.calculate("aaaaa", "aaa")
        exp = 2
        self.assertEqual(res, exp)

    def test_that_did_not_work_in_first_version(self):
        res = damerau_levenshtien.calculate("stables", "aba")
        exp = 5
        self.assertEqual(res, exp)

    def test_equal(self):
        res = damerau_levenshtien.calculate("equal", "equal")
        exp = 0
        self.assertEqual(res, exp)

    # It doesn't pass, I don't know why
    def test_equal_2(self):
        res = damerau_levenshtien.calculate("Shit", "Python")
        exp = 5
        self.assertEqual(res, exp)

    def test_from_site(self):
        res = damerau_levenshtien.calculate("Levenshtien", "Frankenstein")
        exp = 7
        self.assertEqual(res, exp)

    def test_triple_transposition(self):
        res = damerau_levenshtien.calculate("ASAP", "SPAA")
        exp = 3
        self.assertEqual(res, exp)

    def test_empty_line(self):
        res = damerau_levenshtien.calculate("Not empty line", "")
        exp = 14
        self.assertEqual(res, exp)

    def test_empty_lines(self):
        res = damerau_levenshtien.calculate("", "")
        exp = 0
        self.assertEqual(res, exp)
