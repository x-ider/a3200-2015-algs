import unittest
import damerau_levenshtiein


class TestDamerau(unittest.TestCase):
    def test_equal(self):
        res = damerau_levenshtiein.calculate("equal", "equal")
        exp = 0
        self.assertEqual(res, exp)

    # It doesn't pass, I don't know why
    def test_equal_2(self):
        res = damerau_levenshtiein.calculate("Shit", "Python")
        exp = 0
        self.assertEqual(res, exp)

    def test_from_site(self):
        res = damerau_levenshtiein.calculate("Levenshtien", "Frankenstein")
        exp = 7
        self.assertEqual(res, exp)

    def test_triple_transposition(self):
        res = damerau_levenshtiein.calculate("ASAP", "SPAA")
        exp = 3
        self.assertEqual(res, exp)

    def test_empty_line(self):
        res = damerau_levenshtiein.calculate("Not empty line", "")
        exp = 14
        self.assertEqual(res, exp)

    def test_empty_lines(self):
        res = damerau_levenshtiein.calculate("", "")
        exp = 0
        self.assertEqual(res, exp)