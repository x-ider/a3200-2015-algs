import unittest
import radix_sort


class TestSorting(unittest.TestCase):
    def test_empty(self):
        arr = []
        res = radix_sort.radix_sort(arr)
        exp = []
        self.assertEqual(exp, res)

    def test_sorted(self):
        arr = [5, 123, 352, 456, 1235, 1236, 1237, 1238]
        res = radix_sort.radix_sort(arr)
        self.assertEqual(arr, res)

    def test_common(self):
        arr = [123, 43, 54536565, 134, 220, 562, 6, 54, 0, 87, 4547585756456, 555, 100, 555, 555, 777, 777, 777, 776]
        res = radix_sort.radix_sort(arr)
        exp = [0, 6, 43, 54, 87, 100, 123, 134, 220, 555, 555, 555, 562, 776, 777, 777, 777, 54536565, 4547585756456]
        self.assertEqual(exp, res)