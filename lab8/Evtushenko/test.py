import unittest

from queue_on_2_stacks as queue


class TestQueue(unittest.TestCase):
    def interpreter(self, q: queue.StacksQueueWithMaxElement(), inp: list) -> list:
        res = []
        i = 0
        while i != len(inp):
            if inp[i] == 'push':
                i += 1
                res.append(q.push(inp[i]))
            elif inp[i] == 'pop':
                res.append(q.pop())
            elif inp[i] == 'size':
                res.append(q.size())
            elif inp[i] == 'max':
                res.append(q.max())
            i += 1
        return res

    def test_from_site(self):
        q = queue.StacksQueueWithMaxElement()
        inp = ['push', 3, 'push', 1, 'max', 'pop', 'max', 'pop', 'pop', 'max']
        exp = ['ok', 'ok', 3, 3, 1, 1, 'empty', 'empty']
        res = self.interpreter(q, inp)
        self.assertEqual(res, exp)

    def test_too_many_pops(self):
        q = queue.StacksQueueWithMaxElement()
        inp = ['pop', 'push', 10, 'push', 2, 'push', 3, 'push', 4, 'pop', 'pop', 'max', 'pop', 'pop', 'pop']
        exp = ['empty', 'ok', 'ok', 'ok', 'ok', 10, 2, 4, 3, 4, 'empty']
        res = self.interpreter(q, inp)
        self.assertEqual(res, exp)

    def test_common(self):
        q = queue.StacksQueueWithMaxElement()
        inp = ['pop', 'push', 5, 'push', 4, 'max', 'pop', 'push', 3, 'max', 'size', 'pop', 'max', 'pop', 'size', 'max']
        exp = ['empty', 'ok', 'ok', 5, 5, 'ok', 4, 2, 4, 3, 3, 0, 'empty']
