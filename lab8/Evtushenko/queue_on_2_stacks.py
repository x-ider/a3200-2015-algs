__label__ = 'push, pop and two smoking stacks'


class Queue:
    def pop(self):
        pass

    def push(self, n):
        pass

    def size(self):
        pass


class StacksQueueWithMaxElement(Queue):
    def __init__(self):
        self._pop_arr = []
        self._push_arr = []
        self._max_push = []
        self._max_pop = []

    def push(self, n):
        self._push_arr.append(n)
        if len(self._max_push) == 0:
            self._max_push.append(n)
        else:
            if n > self._max_push[len(self._max_push) - 1]:
                self._max_push.append(n)
            else:
                self._max_push.append(self._max_push[len(self._max_push) - 1])
        return 'ok'

    def pop(self):
        if len(self._pop_arr) == 0:
            if len(self._push_arr) == 0:
                return 'empty'
            else:
                self._pop_arr = self._push_arr[::-1]
                self._push_arr.clear()
                self._max_push.clear()
                self._max_pop.append(self._pop_arr[0])
                for i in range(1, len(self._pop_arr)):
                    if self._pop_arr[i] > self._max_pop[i - 1]:
                        self._max_pop.append(self._pop_arr[i])
                    else:
                        self._max_pop.append(self._max_pop[i - 1])
        self._max_pop.pop()
        return self._pop_arr.pop()

    def size(self):
        return len(self._push_arr) + len(self._pop_arr)

    def max(self):
        if len(self._max_push) == 0 and len(self._max_pop) == 0:
            return 'empty'
        elif len(self._max_push) != 0 and len(self._max_pop) == 0:
            return self._max_push[len(self._max_push) - 1]
        elif len(self._max_push) == 0 and len(self._max_pop) != 0:
            return self._max_pop[len(self._max_pop) - 1]
        else:
            return max(self._max_push[len(self._max_push) - 1], self._max_pop[len(self._max_pop) - 1])


if __name__ == '__main__':
    queue = StacksQueueWithMaxElement()
    s = [str(i) for i in input().split()]
    # functions = {'push': queue.push(int(s[1])), 'pop': queue.pop(), 'size': queue.size()}
    while s:
        command = s[0]
        if command == 'push':
            print(queue.push(int(s[1])))
        elif command == 'pop':
            print(queue.pop())
        elif command == 'size':
            print(queue.size())
        elif command == 'max':
            print(queue.max())
        else:
            print('Unknown command!')
        # print(functions.get(command, 'Unknown command!'))
        s = [str(i) for i in input().split()]
