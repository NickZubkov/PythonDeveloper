

class StepValueError(ValueError):
    pass

class Iterator:

    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        self.iterator_checker = self._get_iterator_checker_by_sign()

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        self.pointer += self.step
        self.iterator_checker()
        return self.pointer

    def _positive_iter(self):
        if self.pointer > self.stop:
            raise StopIteration()

    def _negative_iter(self):
        if self.pointer < self.stop:
            raise StopIteration()

    def _wrong_iter(self):
        print("Ой")
        raise StopIteration()

    def _get_iterator_checker_by_sign(self):
        if self.start < self.stop and self.step > 0:
            return self._positive_iter
        elif self.start > self.stop and self.step < 0:
            return self._negative_iter
        else:
            return self._wrong_iter

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as e:
    print(f'Шаг указан неверно: {e}')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()